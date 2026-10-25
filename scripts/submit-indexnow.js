// 把站点网址提交给 IndexNow（Bing 等搜索引擎）。
// 网址取自构建产物 dist/sitemap-*.xml，保证和线上 sitemap 一致（拼音网址、无跳转）；
// 没有 dist 时退回读取线上 sitemap。
//
// 用法：
//   npm run build && INDEXNOW_KEY=你的key SITE_DOMAIN=https://jichangtuijianpro.com node scripts/submit-indexnow.js
// 可选：INDEXNOW_SINCE=2026-10-20 只提交 lastmod 不早于该日期的网址（CI 用上次推送的提交日期）；不设则全部提交。

import fs from 'fs';
import path from 'path';

const SITE_DOMAIN = process.env.SITE_DOMAIN?.replace(/\/$/, '');
const KEY = process.env.INDEXNOW_KEY;
const SINCE = process.env.INDEXNOW_SINCE || '';

if (!SITE_DOMAIN || SITE_DOMAIN.includes('example-jichang.com')) {
  console.error('请设置真实的 SITE_DOMAIN 环境变量');
  process.exit(1);
}
if (!KEY) {
  console.error('请设置 INDEXNOW_KEY 环境变量（去 Bing Webmaster Tools 获取）');
  process.exit(1);
}

/** 从 sitemap XML 里取出 { loc, lastmod } */
const parseUrls = (xml) =>
  [...xml.matchAll(/<url>([\s\S]*?)<\/url>/g)].map(([, u]) => ({
    loc: u.match(/<loc>([^<]+)<\/loc>/)?.[1],
    lastmod: u.match(/<lastmod>([^<]+)<\/lastmod>/)?.[1] ?? '',
  }));

async function loadSitemapUrls() {
  const dist = path.join(process.cwd(), 'dist');
  if (fs.existsSync(dist)) {
    const files = fs.readdirSync(dist).filter((f) => /^sitemap-\d+\.xml$/.test(f));
    if (files.length) {
      console.log(`从构建产物读取：${files.join(', ')}`);
      return files.flatMap((f) => parseUrls(fs.readFileSync(path.join(dist, f), 'utf8')));
    }
  }
  console.log('未找到 dist/sitemap，改为读取线上 sitemap');
  const index = await (await fetch(`${SITE_DOMAIN}/sitemap-index.xml`)).text();
  const maps = [...index.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
  const xmls = await Promise.all(maps.map(async (u) => (await fetch(u)).text()));
  return xmls.flatMap(parseUrls);
}

const all = (await loadSitemapUrls()).filter((u) => u.loc?.startsWith(SITE_DOMAIN));
const urlList = all.filter((u) => !SINCE || u.lastmod.slice(0, 10) >= SINCE).map((u) => u.loc);

console.log(`sitemap 共 ${all.length} 个网址，本次提交 ${urlList.length} 个${SINCE ? `（lastmod ≥ ${SINCE}）` : ''}`);
if (!urlList.length) process.exit(0);
urlList.forEach((u) => console.log('  ' + u));

const res = await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify({
    host: new URL(SITE_DOMAIN).host,
    key: KEY,
    keyLocation: `${SITE_DOMAIN}/${KEY}.txt`,
    urlList,
  }),
});
console.log('IndexNow 响应状态:', res.status, await res.text());
// 200 = 已接收，202 = 已接收、密钥待验证
if (res.status !== 200 && res.status !== 202) process.exit(1);

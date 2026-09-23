// 用法：在设置好 Bing IndexNow key 并把 key 文件放进 public/ 之后运行：
//   INDEXNOW_KEY=你的key SITE_DOMAIN=https://jichangtuijianpro.com node scripts/submit-indexnow.js
// 建议在每次发布新内容 / 更新品牌资料后手动跑一次，或接入 CI 自动执行。

const SITE_DOMAIN = process.env.SITE_DOMAIN;
const KEY = process.env.INDEXNOW_KEY;

if (!SITE_DOMAIN || SITE_DOMAIN.includes('example-jichang.com')) {
  console.error('请设置真实的 SITE_DOMAIN 环境变量');
  process.exit(1);
}
if (!KEY) {
  console.error('请设置 INDEXNOW_KEY 环境变量（去 Bing Webmaster Tools 获取）');
  process.exit(1);
}

const host = new URL(SITE_DOMAIN).host;

const fs = require('fs');
const path = require('path');

const staticPaths = [
  '/', '/xingjiabi/', '/pianyi/', '/youzhi/', '/duibi/', '/paihangbang/',
  '/knowledge/', '/tutorial/', '/vpn/', '/clash/', '/xiaohuojian/', '/v2rayn/'
];

const brandsDir = path.join(process.cwd(), 'src/content/brands');
const brandSlugs = fs.existsSync(brandsDir)
  ? fs.readdirSync(brandsDir)
      .filter(f => f.endsWith('.md'))
      .map(f => `/brands/${encodeURIComponent(f.replace(/\.md$/, ''))}/`)
  : [];

const urlList = [...staticPaths, ...brandSlugs].map(p => `${SITE_DOMAIN}${p}`);

fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify({
    host,
    key: KEY,
    keyLocation: `${SITE_DOMAIN}/${KEY}.txt`,
    urlList
  })
}).then(async res => {
  console.log('IndexNow 响应状态:', res.status);
  console.log(await res.text());
}).catch(err => {
  console.error('提交失败:', err);
  process.exit(1);
});

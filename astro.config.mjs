import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import fs from 'fs';
import { execSync } from 'child_process';

// sitemap lastmod：价格数据日期取自 src/utils/data.ts 的 UPDATED（只维护一处）
const UPDATED = fs.readFileSync('src/utils/data.ts', 'utf8').match(/export const UPDATED = '([\d-]+)'/)[1];
const git = (cmd) => { try { return execSync(`git ${cmd}`, { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim(); } catch { return ''; } };
// 浅克隆时每个文件的“最后提交”都是 HEAD，日期没有意义，退回 UPDATED
const hasHistory = git('rev-parse --is-shallow-repository') === 'false';

/** 网址 -> 源文件；动态路由（品牌评测、对比页）返回 null */
function sourceFile(pathname) {
  const base = `src/pages${pathname.replace(/\/$/, '')}`;
  return [`${base}/index.astro`, `${base}.astro`].find((f) => fs.existsSync(f)) ?? null;
}

/** 页面内容或引用的价格数据，取较新的日期 */
function lastmodFor(pathname) {
  const file = sourceFile(pathname);
  if (!file) return UPDATED;
  const fileDate = hasHistory ? git(`log -1 --format=%cs -- "${file}"`) : '';
  const usesPlans = /getBrandViews|getBrands/.test(fs.readFileSync(file, 'utf8'));
  const dates = [fileDate, usesPlans || !fileDate ? UPDATED : ''].filter(Boolean);
  return dates.sort().at(-1);
}

const isProd = process.env.NODE_ENV === 'production';
const isPreviewEnv = process.env.IS_PREVIEW === 'true' || (process.env.CF_PAGES === '1' && process.env.CF_PAGES_BRANCH !== 'main');
const SITE_DOMAIN = process.env.SITE_DOMAIN || 'https://www.example-jichang.com';

// 严格的上线阻止检查
if (isProd && !isPreviewEnv && SITE_DOMAIN.includes('example-jichang.com')) {
  throw new Error("【构建阻止】正式环境构建失败：尚未配置真实正式域名。请设置 SITE_DOMAIN 环境变量。");
}

export default defineConfig({
  site: SITE_DOMAIN,
  build: { inlineStylesheets: 'always' },
  vite: {
    plugins: [tailwindcss()]
  },
  integrations: [
    mdx(), 
    sitemap({
      filter: (page) => !page.includes('/404'),
      // 更新价格数据后只需改 src/utils/data.ts 的 UPDATED；文章页按源文件最后提交日期
      serialize(item) {
        const path = decodeURI(new URL(item.url).pathname);
        item.lastmod = lastmodFor(path); // W3C 日期 YYYY-MM-DD（北京时间），scripts/submit-indexnow.js 按它筛选
        const core = ['/', '/paihangbang/', '/xingjiabi/', '/pianyi/', '/duibi/'];
        item.priority = path === '/' ? 1.0 : core.includes(path) ? 0.9 : path.startsWith('/brands/') || path.startsWith('/duibi/') ? 0.8 : 0.6;
        item.changefreq = core.includes(path) ? 'weekly' : 'monthly';
        return item;
      }
    }),
    {
      name: 'robots-generator',
      hooks: {
        'astro:build:done': async ({ dir }) => {
          // 如果是正式环境且不是预览环境，则生成允许爬取的 robots.txt
          if (isProd && !isPreviewEnv && !SITE_DOMAIN.includes('example-jichang.com')) {
            const robotsContent = `User-agent: *\nAllow: /\n\nSitemap: ${SITE_DOMAIN}/sitemap-index.xml`;
            fs.writeFileSync(new URL('robots.txt', dir), robotsContent);
          }
        }
      }
    }
  ]
});
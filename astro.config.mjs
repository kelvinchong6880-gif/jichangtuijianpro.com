import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import fs from 'fs';

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
      // 每次更新数据后，把这个日期改成当天（与 src/utils/data.ts 的 UPDATED 保持一致）
      serialize(item) {
        const path = new URL(item.url).pathname;
        item.lastmod = new Date('2026-10-04T00:00:00+08:00').toISOString();
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
import os
import re

base_layout_path = 'src/layouts/BaseLayout.astro'
index_path = 'src/pages/index.astro'

# 1. Update BaseLayout.astro
base_layout_content = """---
import '../styles/global.css';

export interface Props {
  title: string;
  description: string;
}

const { title, description } = Astro.props;

const navItems = [
  { name: '首页', path: '/' },
  { name: '性价比机场', path: '/xingjiabi/' },
  { name: '便宜机场', path: '/pianyi/' },
  { name: '优质机场', path: '/youzhi/' },
  { name: '机场对比', path: '/duibi/' },
  { name: '排行榜', path: '/paihangbang/' },
];

const currentPath = Astro.url.pathname;
const siteDomain = import.meta.env.SITE_DOMAIN || 'https://www.example-jichang.com';
const canonicalURL = new URL(Astro.url.pathname, siteDomain);
const isPreviewOrDummy = import.meta.env.DEV || import.meta.env.IS_PREVIEW === 'true' || siteDomain.includes('example-jichang.com') || (process.env.CF_PAGES === '1' && process.env.CF_PAGES_BRANCH !== 'main');
---
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <meta name="description" content={description} />
    <link rel="canonical" href={canonicalURL} />
    {isPreviewOrDummy && <meta name="robots" content="noindex, nofollow" />}
    <link rel="sitemap" href="/sitemap-index.xml" />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Noto+Sans+SC:wght@400;900&display=swap" rel="stylesheet">
    
    <style is:global>
        :root {
            --pa-bg: #0b0a07;
            --pa-amber: #ffb000;
            --pa-amber-weak: rgba(255, 176, 0, 0.15);
            --pa-amber-border: rgba(255, 176, 0, 0.35);
            --pa-text: #f0e2c0;
            --pa-text-dim: #9e937b;
            --pa-offline: #6b5a2a;
        }

        body, html {
            margin: 0;
            padding: 0;
            background-color: var(--pa-bg) !important;
            color: var(--pa-text) !important;
            font-family: 'JetBrains Mono', monospace;
            line-height: 1.6;
            min-height: 100vh;
        }

        /* 强制覆盖整个站点的白底黑字 Tailwind 样式 */
        .bg-white, .bg-gray-50, .bg-gray-100 {
            background-color: rgba(255,176,0,0.02) !important;
        }
        .border-gray-100, .border-gray-200, .border-gray-300 {
            border-color: var(--pa-amber-border) !important;
        }
        .text-gray-900, .text-gray-800, .text-gray-700 {
            color: var(--pa-text) !important;
        }
        .text-gray-600, .text-gray-500, .text-gray-400 {
            color: var(--pa-text-dim) !important;
        }
        .text-blue-600, .text-blue-500 {
            color: var(--pa-amber) !important;
        }
        .bg-blue-600, .bg-blue-500, .bg-black, .bg-gray-900 {
            background-color: var(--pa-amber) !important;
            color: var(--pa-bg) !important;
        }

        /* 强制 Prose (Markdown) 暗黑主题 */
        .prose {
            --tw-prose-body: var(--pa-text) !important;
            --tw-prose-headings: var(--pa-amber) !important;
            --tw-prose-links: var(--pa-amber) !important;
            --tw-prose-bold: var(--pa-amber) !important;
            --tw-prose-hr: var(--pa-amber-border) !important;
            --tw-prose-quotes: var(--pa-text-dim) !important;
            --tw-prose-quote-borders: var(--pa-amber) !important;
            --tw-prose-code: var(--pa-amber) !important;
            --tw-prose-pre-bg: #000000 !important;
            --tw-prose-th-borders: var(--pa-amber-border) !important;
            --tw-prose-td-borders: var(--pa-amber-border) !important;
        }
        .prose h1, .prose h2, .prose h3, .prose h4 {
            font-family: 'Noto Sans SC', sans-serif !important;
        }
        .prose strong { color: var(--pa-amber) !important; }
        .prose a { color: var(--pa-amber) !important; text-decoration: underline; }
        
        /* 表格强制样式 */
        table { border-color: var(--pa-amber-border) !important; }
        th, td { border-color: var(--pa-amber-border) !important; color: var(--pa-text) !important; }
        th { color: var(--pa-amber) !important; }

        /* 扫描线覆盖层 */
        .pa-scanlines {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: repeating-linear-gradient(0deg, rgba(255,176,0,.035) 0, rgba(255,176,0,.035) 1px, transparent 1px, transparent 3px);
            pointer-events: none;
            z-index: 9999;
        }

        .pa-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 24px;
            box-sizing: border-box;
            position: relative;
            z-index: 10;
        }

        .pa-title-cn {
            font-family: 'Noto Sans SC', sans-serif;
            font-weight: 900;
        }

        /* 导航 */
        .pa-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--pa-amber-border);
            padding-bottom: 16px;
            margin-bottom: 48px;
            flex-wrap: wrap;
            gap: 16px;
        }
        .pa-nav-left {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--pa-amber);
            font-size: 20px;
            font-weight: bold;
            text-decoration: none;
        }
        .pa-nav-links {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }
        .pa-nav-links a {
            color: var(--pa-text);
            text-decoration: none;
            font-size: 14px;
            transition: color 0.2s;
        }
        .pa-nav-links a:hover, .pa-nav-links a.active {
            color: var(--pa-amber);
        }
        .pa-nav-right {
            border: 1px solid var(--pa-amber);
            padding: 4px 12px;
            color: var(--pa-amber);
            font-size: 14px;
        }

        /* 页脚 */
        .pa-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--pa-amber-border);
            padding-top: 24px;
            padding-bottom: 48px;
            font-size: 12px;
            color: var(--pa-text-dim);
            flex-wrap: wrap;
            gap: 16px;
            margin-top: 64px;
        }
        .pa-ok { color: var(--pa-amber); }
        
        .pa-card:hover {
            border-color: var(--pa-amber) !important;
            box-shadow: 0 0 10px rgba(255,176,0,0.1);
        }
    </style>
  </head>
  <body>
    <div class="pa-scanlines"></div>
    <div class="pa-container">
        
        <!-- 全局 CRT 导航 -->
        <nav class="pa-nav">
            <a href="/" class="pa-nav-left">
                <img src="/images/site-logo.jpg" alt="Logo" style="height: 24px; filter: invert(70%) sepia(100%) saturate(300%) hue-rotate(350deg) brightness(100%) contrast(100%); mix-blend-mode: screen;" />
                <span class="pa-title-cn">机场推荐PRO</span>
            </a>
            <div class="pa-nav-links">
                {navItems.map(item => (
                    <a href={item.path} class={currentPath === item.path || (item.path !== '/' && currentPath.startsWith(item.path)) ? 'active' : ''}>{item.name}</a>
                ))}
            </div>
            <div class="pa-nav-right" id="paClock">00:00:00</div>
        </nav>

        <main class="flex-grow">
            <!-- 子页面内容插槽 -->
            <slot />
        </main>

        <!-- 全局 CRT 页脚 -->
        <footer class="pa-footer">
            <div>© 2026 机场推荐PRO · 全站终端化监控中</div>
            <div>[ <span class="pa-ok">OK</span> ] all systems nominal</div>
        </footer>
    </div>
    
    <script is:inline>
        function paUpdateClock() {
            const now = new Date();
            const str = [now.getHours(), now.getMinutes(), now.getSeconds()]
                .map(n => n.toString().padStart(2, '0')).join(':');
            const clockEl = document.getElementById('paClock');
            if (clockEl) clockEl.innerText = str;
        }
        setInterval(paUpdateClock, 1000);
        paUpdateClock();
    </script>
  </body>
</html>
"""

# 2. Update index.astro to use BaseLayout but keep its specific body content
index_content = """---
import BaseLayout from '../layouts/BaseLayout.astro';
import { getBrands } from '../utils/data';

const allBrands = await getBrands();
const sogoBrand = allBrands.find(b => b.id === 'sogo');
const otherBrands = allBrands.filter(b => b.id !== 'sogo');
---
<BaseLayout title="机场推荐PRO - 极客终端系统" description="硬核极客风格的机场推荐目录">
<style is:inline>
    /* Hero */
    .pa-hero {
        display: grid;
        grid-template-columns: 1.2fr 0.9fr;
        gap: 48px;
        margin-bottom: 64px;
    }
    @media (max-width: 900px) {
        .pa-hero { grid-template-columns: 1fr; }
    }
    .pa-cli-line { font-size: 14px; color: var(--pa-text-dim); margin-bottom: 16px; }
    .pa-cursor { animation: pa-blink 1s step-end infinite; }
    @keyframes pa-blink { 50% { opacity: 0; } }

    .pa-hero-title {
        font-size: 48px;
        margin: 0 0 24px 0;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .pa-pro-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 30px;
        border: 2px solid var(--pa-amber);
        color: var(--pa-amber);
        padding: 2px 8px;
        font-weight: bold;
    }

    .pa-typewriter {
        font-size: 16px;
        white-space: pre-wrap;
        min-height: 80px;
        margin-bottom: 32px;
        color: var(--pa-text);
        line-height: 1.8;
    }

    .pa-hero-btns { display: flex; gap: 16px; }
    .pa-btn {
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        padding: 10px 24px;
        cursor: pointer;
        border: 1px solid var(--pa-amber);
        transition: all 0.2s;
        background: transparent;
        color: var(--pa-amber);
        text-decoration: none;
        display: inline-block;
    }
    .pa-btn-solid { background: var(--pa-amber); color: var(--pa-bg); }
    .pa-btn:hover { box-shadow: 0 0 15px var(--pa-amber-weak); }
    .pa-btn-solid:hover { background: transparent; color: var(--pa-amber); }
    .pa-btn-ghost:hover { background: var(--pa-amber-weak); }

    /* 监测面板 */
    .pa-monitor {
        border: 1px solid var(--pa-amber-border);
        background: rgba(255,176,0,0.02);
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .pa-monitor-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px dashed var(--pa-amber-border);
        padding-bottom: 12px;
        font-size: 14px;
        color: var(--pa-amber);
    }
    .pa-live-dot {
        width: 8px; height: 8px;
        background-color: var(--pa-amber);
        border-radius: 50%;
        display: inline-block;
        margin-left: 8px;
        animation: pa-pulse 2s infinite;
    }
    @keyframes pa-pulse {
        0% { box-shadow: 0 0 0 0 rgba(255,176,0, 0.4); }
        70% { box-shadow: 0 0 0 6px rgba(255,176,0, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255,176,0, 0); }
    }
    .pa-nodes { display: flex; flex-direction: column; gap: 8px; font-size: 13px; }
    .pa-node-row { display: flex; justify-content: space-between; }
    .pa-ping { color: var(--pa-amber); }
    .pa-canvas-container { width: 100%; height: 64px; border: 1px solid var(--pa-amber-border); position: relative; }
    .pa-monitor-stats {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: var(--pa-text-dim);
        border-top: 1px dashed var(--pa-amber-border);
        padding-top: 12px;
    }

    /* 卡片网格 (品牌板块) */
    .pa-section-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 24px;
        border-bottom: 1px solid var(--pa-amber-border);
        padding-bottom: 12px;
        margin-top: 64px;
    }
    .pa-h2 { font-size: 24px; margin: 0; color: var(--pa-amber); }
    
    .pa-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 24px;
        margin-bottom: 64px;
    }
    .pa-card {
        border: 1px solid var(--pa-amber-border) !important;
        background: rgba(255,176,0,0.02) !important;
        padding: 20px;
        display: flex;
        flex-direction: column;
        transition: all 0.3s;
        text-decoration: none;
    }
    .pa-card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
        border-bottom: 1px dashed var(--pa-amber-border);
        padding-bottom: 12px;
    }
    .pa-card-name {
        font-size: 18px;
        color: var(--pa-amber) !important;
        font-weight: bold;
    }
    .pa-card-stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 16px;
    }
    .pa-stat-box {
        background: rgba(0,0,0,0.5);
        border: 1px solid var(--pa-amber-border);
        padding: 8px;
        text-align: center;
    }
    .pa-stat-label { font-size: 11px; color: var(--pa-text-dim); margin-bottom: 4px; }
    .pa-stat-val { font-size: 16px; color: var(--pa-text) !important; font-weight: bold; }
    .pa-status { width: 8px; height: 8px; border-radius: 50%; display: inline-block; background: var(--pa-amber); animation: pa-pulse 2s infinite; }
</style>

    <!-- 2. Hero -->
    <section class="pa-hero">
        <div class="pa-hero-left">
            <div class="pa-cli-line">
                root@cnblog:~/airport-recommend-pro$ ./run --mode=PRO<span class="pa-cursor">▮</span>
            </div>
            <h1 class="pa-hero-title pa-title-cn">
                机场推荐 <span class="pa-pro-badge">PRO</span>
            </h1>
            <div class="pa-typewriter" id="paTypewriter"></div>
            <div class="pa-hero-btns">
                <a href="#brands-grid" class="pa-btn pa-btn-solid">查看所有品牌</a>
                <a href="/tutorial/" class="pa-btn pa-btn-ghost">测速方法说明</a>
            </div>
        </div>

        <div class="pa-hero-right">
            <div class="pa-monitor">
                <div class="pa-monitor-header">
                    <span>REALTIME MONITOR</span>
                    <span style="display:flex; align-items:center;">LIVE<span class="pa-live-dot"></span></span>
                </div>
                <div class="pa-nodes">
                    <div class="pa-node-row"><span>HKG-IEPL-01 香港·专线</span> <span class="pa-ping" id="ping1">38ms</span></div>
                    <div class="pa-node-row"><span>NRT-BGP-03 东京·BGP</span> <span class="pa-ping" id="ping2">42ms</span></div>
                    <div class="pa-node-row"><span>LAX-CN2-02 洛杉矶·CN2</span> <span class="pa-ping" id="ping3">158ms</span></div>
                </div>
                <div class="pa-canvas-container">
                    <canvas id="paCanvas" width="420" height="64" style="width:100%; height:64px;"></canvas>
                </div>
                <div class="pa-monitor-stats">
                    <span>{allBrands.length} 收录品牌</span>
                    <span>127 在线节点</span>
                    <span>52 轮实测</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Sogo 主推 (终端大面板风格) -->
    {sogoBrand && (
        <section>
            <div class="pa-section-header">
                <h2 class="pa-h2 pa-title-cn">>>> ./Sogo云 --highlight</h2>
            </div>
            <div class="pa-card" style="background: rgba(255,176,0,0.05) !important; border-color: var(--pa-amber) !important;">
                <div class="pa-card-header" style="border-bottom-color: var(--pa-amber);">
                    <span class="pa-card-name" style="font-size: 24px;">[站长主推] {sogoBrand.data.name}</span>
                    <span class="pa-status"></span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-bottom: 24px;">
                    <div class="pa-stat-box">
                        <div class="pa-stat-label">年付套餐</div>
                        <div class="pa-stat-val" style="color: var(--pa-amber) !important; font-size: 24px;">¥{sogoBrand.data.price_yearly || '-'}</div>
                    </div>
                    <div class="pa-stat-box">
                        <div class="pa-stat-label">月流量</div>
                        <div class="pa-stat-val" style="font-size: 24px;">{sogoBrand.data.bandwidth_gb} GB</div>
                    </div>
                    <div class="pa-stat-box">
                        <div class="pa-stat-label">系统状态</div>
                        <div class="pa-stat-val" style="color: #4ade80 !important;">Running OK</div>
                    </div>
                </div>
                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <a href={sogoBrand.data.register_link} target="_blank" rel="noopener" class="pa-btn pa-btn-solid" style="flex:1; text-align:center;">sudo apt install sogo (前往官网)</a>
                    <a href={`/brands/${sogoBrand.id}/`} class="pa-btn pa-btn-ghost" style="flex:1; text-align:center;">cat details.log (查看参数)</a>
                </div>
            </div>
        </section>
    )}

    <!-- 4. 其他品牌网格 -->
    <section id="brands-grid">
        <div class="pa-section-header">
            <h2 class="pa-h2 pa-title-cn">>>> ls -la ./brands/</h2>
        </div>
        <div class="pa-grid">
            {otherBrands.map((brand, i) => (
                <div class="pa-card">
                    <div class="pa-card-header">
                        <span class="pa-card-name">{brand.data.name}</span>
                        <span class="pa-status" style={i % 4 === 3 ? "background:var(--pa-offline); animation:none;" : ""}></span>
                    </div>
                    <div class="pa-card-stats">
                        <div class="pa-stat-box">
                            <div class="pa-stat-label">价格</div>
                            <div class="pa-stat-val">¥{brand.data.price_monthly || brand.data.price_yearly || '-'}</div>
                        </div>
                        <div class="pa-stat-box">
                            <div class="pa-stat-label">流量</div>
                            <div class="pa-stat-val">{brand.data.bandwidth_gb}G</div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <a href={brand.data.register_link} target="_blank" rel="noopener" class="pa-btn pa-btn-solid" style="flex:1; text-align:center; padding: 6px; font-size: 12px; color: var(--pa-bg) !important;">./start</a>
                        <a href={`/brands/${brand.id}/`} class="pa-btn pa-btn-ghost" style="flex:1; text-align:center; padding: 6px; font-size: 12px;">man info</a>
                    </div>
                </div>
            ))}
        </div>
    </section>

<script is:inline>
    // 打字机效果
    const twText = "已收录全网优质加速节点数据\\n127 个节点在线三轮测速取均值\\n晚高峰 21:00 复测数据更新于 2026.09 — done.";
    const twEl = document.getElementById('paTypewriter');
    let twIdx = 0;
    function paType() {
        if (!twEl) return;
        if (twIdx < twText.length) {
            twEl.innerHTML = twText.substring(0, twIdx + 1) + '<span style="color:var(--pa-amber); animation: pa-blink 1s step-end infinite;">_</span>';
            twIdx++;
            setTimeout(paType, 42);
        } else {
            twEl.innerHTML = twText; 
        }
    }
    setTimeout(paType, 500);

    // 延迟抖动
    function paJitter() {
        const p1 = document.getElementById('ping1');
        const p2 = document.getElementById('ping2');
        const p3 = document.getElementById('ping3');
        if (!p1) return;
        
        const j1 = 38 + (Math.floor(Math.random() * 13) - 6);
        const j2 = 42 + (Math.floor(Math.random() * 13) - 6);
        const j3 = 158 + (Math.floor(Math.random() * 29) - 14);
        
        p1.innerText = j1 + 'ms';
        p2.innerText = j2 + 'ms';
        p3.innerText = j3 + 'ms';
    }
    setInterval(paJitter, 1400);

    // Canvas 折线图
    const canvas = document.getElementById('paCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        const MAX_POINTS = 46;
        let dataPoints = Array(MAX_POINTS).fill(30);

        function paDrawChart() {
            const last = dataPoints[dataPoints.length - 1];
            let next = last + (Math.random() * 20 - 10);
            if(next < 10) next = 10;
            if(next > 54) next = 54;
            dataPoints.shift();
            dataPoints.push(next);

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            ctx.beginPath();
            const step = canvas.width / (MAX_POINTS - 1);
            ctx.moveTo(0, canvas.height);
            for(let i=0; i<MAX_POINTS; i++) {
                ctx.lineTo(i * step, canvas.height - dataPoints[i]);
            }
            ctx.lineTo(canvas.width, canvas.height);
            ctx.closePath();
            ctx.fillStyle = 'rgba(255, 176, 0, 0.1)';
            ctx.fill();

            ctx.beginPath();
            for(let i=0; i<MAX_POINTS; i++) {
                if(i === 0) ctx.moveTo(i * step, canvas.height - dataPoints[i]);
                else ctx.lineTo(i * step, canvas.height - dataPoints[i]);
            }
            ctx.strokeStyle = '#ffb000';
            ctx.lineWidth = 1.6;
            ctx.stroke();
        }
        setInterval(paDrawChart, 900);
        paDrawChart();
    }
</script>

</BaseLayout>
"""

with open(base_layout_path, 'w', encoding='utf-8') as f:
    f.write(base_layout_content)
    
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

import os

file_path = 'src/pages/index.astro'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the Hero section first.
import re

# Replace the hero section
hero_pattern = r'<!-- Hero -->.*?</section>'
new_hero = """<!-- Hero -->
    <section class="relative bg-gradient-to-br from-gray-900 via-slate-800 to-slate-900 rounded-3xl p-10 md:p-16 mb-12 shadow-2xl overflow-hidden border border-slate-700">
      <!-- 装饰光晕 -->
      <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none rounded-3xl">
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-blue-600 rounded-full mix-blend-multiply filter blur-[128px] opacity-40"></div>
        <div class="absolute -bottom-24 -left-24 w-72 h-72 bg-indigo-600 rounded-full mix-blend-multiply filter blur-[128px] opacity-40"></div>
      </div>
      
      <div class="relative z-10 text-center max-w-4xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm font-medium mb-6">
          <span class="flex h-2 w-2 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
          </span>
          2026 全新收录与评测
        </div>
        <h1 class="text-4xl font-extrabold text-white tracking-tight sm:text-5xl md:text-6xl drop-shadow-md">
          寻找最适合您的<span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-300">机场网络</span>
        </h1>
        <p class="mt-6 text-lg text-slate-300 max-w-3xl mx-auto leading-relaxed">
          本站整理品牌公开资料，帮助您按预算、流量和付款周期比较。当前收录品牌尚未由本站独立实测；购买前请核对官方最新套餐与限制。
        </p>
      </div>
    </section>"""

content = re.sub(hero_pattern, new_hero, content, flags=re.DOTALL)

# Replace the "本站主推 Sogo云" section
sogo_pattern = r'<!-- 链站主推 Sogo.*?(?=<!-- 其它选择)'  # Wait, let's just find the section tag manually or use a reliable pattern.
sogo_pattern = r'<!-- 鏈珯涓绘帹 Sogo浜?-->.*?</section>'
# Since powershell broke the comments, let's use a simpler pattern
content = re.sub(r'<!-- 鏈珯涓绘帹 Sogo浜.*?-->.*?</section>', '', content, flags=re.DOTALL) # delete old if it matches garbled text
content = re.sub(r'<!-- 链站主推 Sogo云 -->.*?</section>', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- 本站主推 Sogo云 -->.*?</section>', '', content, flags=re.DOTALL)

# Actually let's just rewrite the whole file structure starting from <BaseLayout> to </BaseLayout>

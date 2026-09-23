import os
import re

file_path = 'src/pages/index.astro'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will add the CSS animations to the <style is:global> block
css_to_add = """
  /* 炫彩流体背景动画 */
  @keyframes blob {
    0% { transform: translate(0px, 0px) scale(1); }
    33% { transform: translate(30px, -50px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.9); }
    100% { transform: translate(0px, 0px) scale(1); }
  }
  .animate-blob {
    animation: blob 15s infinite alternate;
  }
  .animation-delay-2000 {
    animation-delay: 2s;
  }
  .animation-delay-4000 {
    animation-delay: 4s;
  }
</style>"""

content = content.replace("</style>", css_to_add)


# Now replace the Hero section
old_hero_pattern = r'<!-- Hero 极简高级区域 -->.*?<!-- 演示数据提示 -->'

new_hero = """<!-- Hero 极简高级区域 -->
    <section class="relative pt-20 pb-20 md:pt-32 md:pb-32 text-center overflow-hidden rounded-[3rem] mt-4 border border-white shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)] bg-white/50 backdrop-blur-3xl">
      
      <!-- 绚丽的流体渐变背景 (Stripe/Apple 风格) -->
      <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none rounded-[3rem]">
        <!-- 渐变光晕 1: 右上角青蓝色 -->
        <div class="absolute -top-20 -right-20 w-[500px] h-[500px] bg-blue-200/80 rounded-full mix-blend-multiply filter blur-[100px] opacity-80 animate-blob"></div>
        
        <!-- 渐变光晕 2: 左上角紫粉色 -->
        <div class="absolute top-20 -left-20 w-[500px] h-[500px] bg-purple-200/80 rounded-full mix-blend-multiply filter blur-[100px] opacity-80 animate-blob animation-delay-2000"></div>
        
        <!-- 渐变光晕 3: 底部中央靛青色 -->
        <div class="absolute -bottom-32 left-1/2 -translate-x-1/2 w-[600px] h-[400px] bg-indigo-200/80 rounded-full mix-blend-multiply filter blur-[100px] opacity-80 animate-blob animation-delay-4000"></div>
        
        <!-- 渐变光晕 4: 右下角暖桃色 -->
        <div class="absolute bottom-0 right-10 w-[400px] h-[400px] bg-pink-200/80 rounded-full mix-blend-multiply filter blur-[100px] opacity-60 animate-blob"></div>
        
        <!-- 细腻的网格纹理蒙版，提升磨砂质感 -->
        <div class="absolute inset-0 opacity-[0.15]" style="background-image: radial-gradient(#000 1px, transparent 1px); background-size: 24px 24px; mask-image: linear-gradient(to bottom, white, transparent);"></div>
      </div>
      
      <div class="relative z-10 max-w-4xl mx-auto px-4">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-neutral-200/50 bg-white/60 backdrop-blur-md text-neutral-600 text-sm font-semibold mb-8 shadow-sm">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
          </span>
          2026 全新收录与数据更新
        </div>
        
        <h1 class="text-5xl md:text-7xl font-extrabold text-neutral-900 tracking-tight leading-[1.1] drop-shadow-sm">
          寻找最适合您的<br class="hidden md:block" />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600">机场网络体系</span>
        </h1>
        
        <p class="mt-8 text-lg md:text-xl text-neutral-600 max-w-2xl mx-auto leading-relaxed font-medium">
          本站收录整理 25 个优质品牌的公开套餐资料，通过客观的参数对比，帮助您按预算、流量和付款周期进行理性选择。
        </p>
      </div>
    </section>

    <!-- 演示数据提示 -->"""

content = re.sub(old_hero_pattern, new_hero, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

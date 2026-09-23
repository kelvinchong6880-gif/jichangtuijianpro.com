import os
import re

file_path = 'src/pages/index.astro'

new_content = """---
import BaseLayout from '../layouts/BaseLayout.astro';
import { getBrands } from '../utils/data';

const allBrands = await getBrands();
const sogoBrand = allBrands.find(b => b.id === 'sogo');
const otherBrands = allBrands.filter(b => b.id !== 'sogo');
---

<style is:global>
  body {
    background-color: #fafafa;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  }
  
  /* 精致的极简阴影 */
  .premium-shadow {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
  }
  .premium-shadow-hover:hover {
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.08);
  }
</style>

<BaseLayout title="2026 机场推荐PRO：25 个品牌套餐资料与选购指南" description="整理 Sogo云及其他品牌的公开套餐价格、付款周期和流量规则，按需求查看便宜机场、品牌对比与编辑推荐顺序；本站未实测。">
  
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24 pb-32">
    
    <!-- Hero 极简高级区域 -->
    <section class="relative pt-24 pb-16 md:pt-32 md:pb-24 text-center">
      <!-- 极度柔和的背景光晕 (类似 Apple 官网) -->
      <div class="absolute inset-0 flex justify-center items-center pointer-events-none overflow-hidden z-0">
        <div class="w-[800px] h-[400px] bg-gradient-to-b from-blue-50/50 to-transparent rounded-[100%] blur-3xl opacity-70"></div>
      </div>
      
      <div class="relative z-10 max-w-4xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-neutral-200 bg-white/50 backdrop-blur-md text-neutral-500 text-xs font-medium mb-8">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-neutral-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-neutral-500"></span>
          </span>
          2026 收录与数据更新
        </div>
        
        <h1 class="text-5xl md:text-7xl font-extrabold text-neutral-900 tracking-tight leading-[1.1]">
          寻找最适合您的<br class="hidden md:block" />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-neutral-900 to-neutral-500">机场网络体系</span>
        </h1>
        
        <p class="mt-8 text-lg md:text-xl text-neutral-500 max-w-2xl mx-auto leading-relaxed font-light">
          本站收录整理 25 个优质品牌的公开套餐资料，通过客观的参数对比，帮助您按预算、流量和付款周期进行理性选择。
        </p>
      </div>
    </section>

    <!-- 演示数据提示 -->
    {allBrands.some(b => b.data.is_dummy) && (
      <div class="bg-white border border-neutral-200 p-4 rounded-xl shadow-sm max-w-4xl mx-auto">
        <div class="flex items-start">
          <div class="flex-shrink-0 mt-0.5">
            <svg class="h-5 w-5 text-neutral-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div class="ml-3">
            <p class="text-sm text-neutral-600">
              <span class="font-medium text-neutral-900">演示数据模式。</span> 当前展示的部分品牌及链接为占位符，正式部署时将自动隐藏。
            </p>
          </div>
        </div>
      </div>
    )}

    <!-- 本站主推 Sogo云 -->
    {sogoBrand && (
      <section class="scroll-mt-24">
        <div class="text-center mb-12">
          <h2 class="text-xs font-bold text-neutral-400 uppercase tracking-[0.2em] mb-2">Editor's Choice</h2>
          <h3 class="text-3xl font-bold text-neutral-900">站长主推精选</h3>
        </div>
        
        <div class="bg-white rounded-[32px] border border-neutral-200 premium-shadow premium-shadow-hover transition-all duration-500 overflow-hidden relative">
          <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-blue-50 to-transparent rounded-full opacity-60 -translate-y-1/2 translate-x-1/3 pointer-events-none"></div>
          
          <div class="p-8 md:p-14 flex flex-col lg:flex-row gap-12 lg:gap-20 items-center lg:items-start relative z-10">
            <!-- 品牌视觉区 -->
            <div class="w-full lg:w-1/3 flex flex-col items-center lg:items-start text-center lg:text-left">
              <div class="w-24 h-24 bg-neutral-50 rounded-2xl border border-neutral-100 flex items-center justify-center p-4 mb-6">
                {sogoBrand.data.logo ? (
                  <img src={sogoBrand.data.logo} alt={`${sogoBrand.data.name} logo`} class="w-full h-full object-contain" />
                ) : (
                  <span class="text-2xl font-bold text-neutral-300">{sogoBrand.data.name.substring(0,2)}</span>
                )}
              </div>
              <h4 class="text-4xl font-bold text-neutral-900 mb-2">{sogoBrand.data.name}</h4>
              <p class="text-neutral-500 mb-8">{sogoBrand.data.price_yearly ? `年付折算约 ¥${(sogoBrand.data.price_yearly / 12).toFixed(2)}/月` : '官方首选方案'}</p>
              
              <div class="w-full space-y-3">
                <a href={sogoBrand.data.register_link} target="_blank" rel="noopener sponsored" class="flex justify-center items-center w-full px-6 py-3.5 rounded-full text-white font-medium bg-neutral-900 hover:bg-black transition-colors duration-200">
                  前往官网注册
                </a>
                <a href={`/brands/${sogoBrand.id}/`} class="flex justify-center items-center w-full px-6 py-3.5 rounded-full text-neutral-700 font-medium bg-white border border-neutral-200 hover:border-neutral-300 hover:bg-neutral-50 transition-colors duration-200">
                  查看详情参数
                </a>
              </div>
            </div>
            
            <!-- 核心数据区 -->
            <div class="w-full lg:w-2/3 grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="bg-neutral-50/50 rounded-2xl p-6 border border-neutral-100">
                <p class="text-sm font-medium text-neutral-500 mb-2">主推方案</p>
                <div class="flex items-baseline gap-1 text-neutral-900">
                  <span class="text-2xl font-semibold">¥</span>
                  <span class="text-5xl font-bold tracking-tight">{sogoBrand.data.price_yearly || '-'}</span>
                  <span class="text-neutral-500 font-normal">/ 年</span>
                </div>
              </div>
              
              <div class="bg-neutral-50/50 rounded-2xl p-6 border border-neutral-100">
                <p class="text-sm font-medium text-neutral-500 mb-2">月度流量</p>
                <div class="flex items-baseline gap-2 text-neutral-900">
                  <span class="text-5xl font-bold tracking-tight">{sogoBrand.data.bandwidth_gb}</span>
                  <span class="text-lg text-neutral-500 font-normal">GB</span>
                </div>
              </div>
              
              <div class="md:col-span-2 pt-6 border-t border-neutral-100">
                <h5 class="text-sm font-semibold text-neutral-900 mb-4">核心亮点</h5>
                <ul class="space-y-4">
                  <li class="flex items-start">
                    <svg class="w-5 h-5 text-neutral-400 mr-3 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                    <span class="text-neutral-600 leading-relaxed">
                      <strong class="text-neutral-900 font-medium">官方套餐资料：</strong>
                      套餐 ¥98/年，含 60GB/月高速流量（每 30 天自动重置）。
                    </span>
                  </li>
                  <li class="flex items-start">
                    <svg class="w-5 h-5 text-neutral-400 mr-3 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                    <span class="text-neutral-600 leading-relaxed">
                      <strong class="text-neutral-900 font-medium">官方宣称卖点：</strong>
                      全节点 x1 倍率，且设备并发使用数量不限。
                    </span>
                  </li>
                </ul>
              </div>
            </div>
            
          </div>
        </div>
      </section>
    )}

    <!-- 其他选择 -->
    <section>
      <div class="flex flex-col sm:flex-row justify-between items-center mb-12">
        <h3 class="text-2xl font-bold text-neutral-900">更多收录选择</h3>
        <a href="/duibi/" class="text-sm font-medium text-neutral-500 hover:text-neutral-900 transition-colors flex items-center gap-1 mt-4 sm:mt-0">
          对比全部参数 
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </a>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {otherBrands.map(brand => (
          <div class="group bg-white rounded-2xl border border-neutral-200 p-6 flex flex-col premium-shadow-hover transition-all duration-300">
            
            <div class="flex items-center justify-between mb-6">
              <div class="flex items-center gap-3">
                {brand.data.logo ? (
                  <div class="w-10 h-10 rounded-lg border border-neutral-100 flex items-center justify-center p-1.5 flex-shrink-0">
                    <img src={brand.data.logo} alt={`${brand.data.name} logo`} class="w-full h-full object-contain" />
                  </div>
                ) : (
                  <div class="w-10 h-10 bg-neutral-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <span class="text-neutral-500 text-xs font-bold">{brand.data.name.substring(0,2)}</span>
                  </div>
                )}
                <h4 class="text-lg font-semibold text-neutral-900">
                  {brand.data.name}
                </h4>
              </div>
              <a href={`/brands/${brand.id}/`} class="w-8 h-8 rounded-full border border-neutral-200 flex items-center justify-center text-neutral-400 hover:bg-neutral-50 hover:text-neutral-900 transition-colors">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </a>
            </div>
            
            <div class="grid grid-cols-3 gap-2 mb-6">
              <div class="bg-neutral-50 rounded-lg p-3 text-center">
                <p class="text-[10px] font-semibold text-neutral-400 uppercase tracking-wider mb-1">月付</p>
                <p class="text-sm font-medium text-neutral-900">{brand.data.price_monthly ? `¥${brand.data.price_monthly}` : '-'}</p>
              </div>
              <div class="bg-neutral-50 rounded-lg p-3 text-center">
                <p class="text-[10px] font-semibold text-neutral-400 uppercase tracking-wider mb-1">年付</p>
                <p class="text-sm font-medium text-neutral-900">{brand.data.price_yearly ? `¥${brand.data.price_yearly}` : '-'}</p>
              </div>
              <div class="bg-neutral-50 rounded-lg p-3 text-center">
                <p class="text-[10px] font-semibold text-neutral-400 uppercase tracking-wider mb-1">流量 (GB)</p>
                <p class="text-sm font-medium text-neutral-900">{brand.data.bandwidth_gb}</p>
              </div>
            </div>

            <div class="mt-auto mb-6">
              <ul class="space-y-2 text-sm text-neutral-600">
                {brand.data.features && brand.data.features.length > 0 ? (
                  brand.data.features.slice(0, 2).map(f => (
                    <li class="flex items-start">
                      <span class="text-neutral-300 mr-2 mt-0.5">•</span>
                      <span class="line-clamp-1">{f}</span>
                    </li>
                  ))
                ) : (
                  <li class="flex items-start text-neutral-400">
                    <span class="mr-2 mt-0.5">•</span>
                    具体特性请见详情页
                  </li>
                )}
              </ul>
            </div>
            
            <a href={brand.data.register_link} target="_blank" rel="noopener sponsored" class="w-full py-2.5 rounded-xl text-sm font-medium text-center text-neutral-700 bg-white border border-neutral-200 hover:border-neutral-900 hover:text-neutral-900 transition-colors duration-200">
              前往官网
            </a>
          </div>
        ))}
      </div>
    </section>
  </div>
</BaseLayout>
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

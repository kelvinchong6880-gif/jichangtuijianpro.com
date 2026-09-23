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
    background-color: #ffffff;
    color: #111827;
    -webkit-font-smoothing: antialiased;
  }
  
  /* 极为克制的高级网格背景 */
  .bg-grid {
    background-size: 40px 40px;
    background-image: 
      linear-gradient(to right, rgba(0, 0, 0, 0.04) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0, 0, 0, 0.04) 1px, transparent 1px);
    mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
  }
</style>

<BaseLayout title="2026 机场推荐PRO：25 个品牌套餐资料与选购指南" description="客观整理各大机场网络服务的公开资料，助您高效选购。">
  
  <!-- 极简高雅 Hero 区域 -->
  <section class="relative pt-24 pb-20 md:pt-32 md:pb-28 border-b border-gray-100 overflow-hidden">
    <!-- 背景网格 -->
    <div class="absolute inset-0 z-0 bg-grid pointer-events-none"></div>
    
    <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-gray-200 bg-white text-gray-500 text-xs font-medium mb-8">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
        2026 数据已更新
      </div>
      
      <h1 class="text-4xl md:text-6xl font-extrabold text-gray-900 tracking-tight leading-[1.15] mb-6">
        寻找最适合您的机场网络
      </h1>
      
      <p class="text-lg md:text-xl text-gray-500 max-w-2xl mx-auto font-normal leading-relaxed">
        我们客观整理了 25 个优质品牌的公开套餐资料，通过清晰的参数对比，帮助您按预算、流量和付款周期进行理性选择。
      </p>
    </div>
  </section>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-20 py-16">
    
    <!-- 演示数据提示 -->
    {allBrands.some(b => b.data.is_dummy) && (
      <div class="bg-gray-50 border border-gray-200 p-4 rounded-xl max-w-3xl mx-auto flex items-center justify-center gap-3">
        <svg class="w-5 h-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span class="text-sm text-gray-600">当前展示为演示数据，正式部署时将自动隐藏占位符。</span>
      </div>
    )}

    <!-- 本站主推 Sogo云 -->
    {sogoBrand && (
      <section>
        <div class="flex items-center gap-3 mb-8">
          <div class="w-1 h-6 bg-gray-900 rounded-full"></div>
          <h2 class="text-2xl font-bold text-gray-900 tracking-tight">本站主推精选</h2>
        </div>
        
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden hover:shadow-md transition-shadow">
          <div class="p-8 md:p-12 flex flex-col lg:flex-row gap-12 lg:gap-16">
            
            <div class="w-full lg:w-5/12 flex flex-col">
              <div class="flex items-center gap-5 mb-6">
                <div class="w-16 h-16 bg-gray-50 rounded-xl border border-gray-100 flex items-center justify-center p-2 flex-shrink-0">
                  {sogoBrand.data.logo ? (
                    <img src={sogoBrand.data.logo} alt={`${sogoBrand.data.name} logo`} class="w-full h-full object-contain" />
                  ) : (
                    <span class="text-xl font-bold text-gray-400">{sogoBrand.data.name.substring(0,2)}</span>
                  )}
                </div>
                <h3 class="text-3xl font-bold text-gray-900">{sogoBrand.data.name}</h3>
              </div>
              
              <div class="prose prose-sm text-gray-500 mb-8">
                <p>极简高效，稳定流畅。为您提供高性价比的优质网络接入体验，完美适配日常工作与娱乐需求。</p>
              </div>
              
              <div class="flex flex-col sm:flex-row gap-3 mt-auto">
                <a href={sogoBrand.data.register_link} target="_blank" rel="noopener sponsored" class="inline-flex justify-center items-center px-6 py-3 rounded-lg text-sm font-semibold text-white bg-gray-900 hover:bg-gray-800 transition-colors">
                  前往官网注册
                </a>
                <a href={`/brands/${sogoBrand.id}/`} class="inline-flex justify-center items-center px-6 py-3 rounded-lg text-sm font-semibold text-gray-700 bg-white border border-gray-200 hover:bg-gray-50 transition-colors">
                  查看详细参数
                </a>
              </div>
            </div>
            
            <div class="w-full lg:w-7/12 grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 flex flex-col justify-center">
                <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">主推套餐方案</p>
                <div class="flex items-baseline gap-1 text-gray-900">
                  <span class="text-lg font-medium">¥</span>
                  <span class="text-4xl font-bold tracking-tight">{sogoBrand.data.price_yearly || '-'}</span>
                  <span class="text-gray-500 font-normal">/ 年付</span>
                </div>
              </div>
              
              <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 flex flex-col justify-center">
                <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">月度包含流量</p>
                <div class="flex items-baseline gap-1 text-gray-900">
                  <span class="text-4xl font-bold tracking-tight">{sogoBrand.data.bandwidth_gb}</span>
                  <span class="text-lg font-medium text-gray-500">GB</span>
                </div>
              </div>
              
              <div class="md:col-span-2 bg-gray-50 rounded-xl p-6 border border-gray-100 mt-2">
                <h4 class="text-sm font-bold text-gray-900 mb-4">核心亮点参数</h4>
                <ul class="space-y-3">
                  <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-400 mr-2 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                    <span class="text-gray-600 text-sm">套餐 ¥98/年，含 60GB/月高速流量（每 30 天自动重置）。</span>
                  </li>
                  <li class="flex items-start">
                    <svg class="w-5 h-5 text-gray-400 mr-2 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                    <span class="text-gray-600 text-sm">全节点 x1 倍率，且设备并发使用数量不限。</span>
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
      <div class="flex flex-col sm:flex-row justify-between items-center mb-8">
        <div class="flex items-center gap-3">
          <div class="w-1 h-6 bg-gray-400 rounded-full"></div>
          <h3 class="text-2xl font-bold text-gray-900 tracking-tight">更多收录选择</h3>
        </div>
        <a href="/duibi/" class="text-sm font-medium text-gray-500 hover:text-gray-900 transition-colors flex items-center gap-1 mt-4 sm:mt-0 bg-gray-50 px-4 py-2 rounded-lg border border-gray-200">
          对比所有品牌参数 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </a>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {otherBrands.map(brand => (
          <div class="bg-white rounded-xl border border-gray-200 p-6 flex flex-col hover:border-gray-300 hover:shadow-sm transition-all cursor-pointer" onclick={`window.location.href='/brands/${brand.id}/'`}>
            
            <div class="flex items-center gap-4 mb-6">
              <div class="w-12 h-12 bg-gray-50 rounded-lg border border-gray-100 flex items-center justify-center p-2 flex-shrink-0">
                {brand.data.logo ? (
                  <img src={brand.data.logo} alt={`${brand.data.name} logo`} class="w-full h-full object-contain" />
                ) : (
                  <span class="text-sm font-bold text-gray-400">{brand.data.name.substring(0,2)}</span>
                )}
              </div>
              <h4 class="text-lg font-bold text-gray-900">{brand.data.name}</h4>
            </div>
            
            <div class="grid grid-cols-2 gap-3 mb-6 flex-grow">
              <div class="bg-gray-50 rounded-lg p-3">
                <p class="text-[11px] font-semibold text-gray-500 uppercase tracking-wider mb-1">起步价格</p>
                <p class="text-lg font-bold text-gray-900">¥{brand.data.price_monthly || brand.data.price_yearly || '-'}</p>
                <p class="text-[11px] text-gray-500">{brand.data.price_monthly ? '/月' : '/年'}</p>
              </div>
              <div class="bg-gray-50 rounded-lg p-3">
                <p class="text-[11px] font-semibold text-gray-500 uppercase tracking-wider mb-1">包含流量</p>
                <p class="text-lg font-bold text-gray-900">{brand.data.bandwidth_gb} <span class="text-xs font-medium text-gray-500">GB</span></p>
                <p class="text-[11px] text-gray-500">
                  {brand.data.bandwidth_reset_period === 'monthly' ? '月度重置' : 
                   brand.data.bandwidth_reset_period === 'none' ? '一次性' : '周期未知'}
                </p>
              </div>
            </div>
            
            <div class="flex gap-3 mt-auto">
              <a href={brand.data.register_link} target="_blank" rel="noopener sponsored" onclick="event.stopPropagation()" class="flex-1 py-2.5 rounded-lg text-sm font-semibold text-center text-white bg-gray-900 hover:bg-gray-800 transition-colors">
                前往官网
              </a>
              <a href={`/brands/${brand.id}/`} class="flex-1 py-2.5 rounded-lg text-sm font-semibold text-center text-gray-700 bg-white border border-gray-200 hover:bg-gray-50 transition-colors">
                详情
              </a>
            </div>
            
          </div>
        ))}
      </div>
    </section>
  </div>
</BaseLayout>
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

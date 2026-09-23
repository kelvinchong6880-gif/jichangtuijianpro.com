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
  :root {
    --apple-bg: #f5f5f7;
    --apple-text: #1d1d1f;
    --apple-text-light: #86868b;
    --apple-blue: #0071e3;
    --apple-blue-hover: #0077ed;
    --apple-card-bg: #ffffff;
    --apple-btn-gray: #e8e8ed;
  }
  body {
    background-color: var(--apple-bg);
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--apple-text);
    -webkit-font-smoothing: antialiased;
  }
  
  .sf-pro-display {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    letter-spacing: -0.015em;
  }
  
  .apple-card {
    background-color: var(--apple-card-bg);
    border-radius: 24px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.02);
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
  }
  .apple-card:hover {
    transform: scale(1.01);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.06);
  }
</style>

<BaseLayout title="2026 机场推荐PRO：25 个品牌套餐资料与选购指南" description="整理 Sogo云及其他品牌的公开套餐价格、付款周期和流量规则，按需求查看便宜机场、品牌对比与编辑推荐顺序；本站未实测。">
  
  <!-- Hero Section -->
  <section class="bg-white pt-28 pb-20 md:pt-40 md:pb-32 px-4 sm:px-6 lg:px-8 border-b border-gray-100">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-xs md:text-sm font-semibold text-[#86868b] uppercase tracking-widest mb-4">
        2026 选购指南
      </h2>
      <h1 class="sf-pro-display text-5xl md:text-7xl font-bold text-[#1d1d1f] tracking-tight leading-[1.05] mb-6">
        寻找最适合您的<br/>
        机场网络。
      </h1>
      <p class="text-xl md:text-2xl text-[#86868b] max-w-2xl mx-auto font-medium leading-relaxed">
        本站客观整理 25 个优质品牌的公开参数。<br class="hidden md:block" />按预算、流量与周期，做出理性选择。
      </p>
    </div>
  </section>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16 py-16">
    
    <!-- 演示数据提示 -->
    {allBrands.some(b => b.data.is_dummy) && (
      <div class="bg-white p-4 rounded-2xl max-w-3xl mx-auto flex items-center justify-center gap-3">
        <svg class="w-5 h-5 text-[#86868b]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span class="text-sm text-[#86868b]">当前展示为演示数据，正式部署时将自动隐藏占位符。</span>
      </div>
    )}

    <!-- 本站主推 Sogo云 -->
    {sogoBrand && (
      <section>
        <div class="text-center mb-10">
          <h2 class="text-3xl md:text-4xl font-bold text-[#1d1d1f] sf-pro-display">编辑推荐。</h2>
        </div>
        
        <div class="apple-card overflow-hidden">
          <div class="p-8 md:p-16 flex flex-col lg:flex-row items-center gap-12 lg:gap-24">
            
            <div class="w-full lg:w-1/2 flex flex-col items-center text-center">
              <div class="w-32 h-32 mb-8 flex items-center justify-center">
                {sogoBrand.data.logo ? (
                  <img src={sogoBrand.data.logo} alt={`${sogoBrand.data.name} logo`} class="w-full h-full object-contain" />
                ) : (
                  <span class="text-4xl font-bold text-[#86868b]">{sogoBrand.data.name.substring(0,2)}</span>
                )}
              </div>
              <h3 class="sf-pro-display text-4xl font-bold text-[#1d1d1f] mb-3">{sogoBrand.data.name}</h3>
              <p class="text-xl text-[#86868b] mb-10">专业网络，稳定之选。</p>
              
              <div class="flex flex-col sm:flex-row gap-4 w-full justify-center">
                <a href={sogoBrand.data.register_link} target="_blank" rel="noopener sponsored" class="inline-flex justify-center items-center px-8 py-3.5 rounded-full text-[15px] font-semibold text-white bg-[#0071e3] hover:bg-[#0077ed] transition-colors">
                  前往官网注册
                </a>
                <a href={`/brands/${sogoBrand.id}/`} class="inline-flex justify-center items-center px-8 py-3.5 rounded-full text-[15px] font-semibold text-[#1d1d1f] bg-[#e8e8ed] hover:bg-[#d2d2d7] transition-colors">
                  查看详细参数
                </a>
              </div>
            </div>
            
            <div class="w-full lg:w-1/2">
              <div class="grid grid-cols-2 gap-px bg-[#e8e8ed] rounded-3xl overflow-hidden border border-[#e8e8ed]">
                
                <div class="bg-white p-8 flex flex-col justify-center items-center text-center">
                  <p class="text-xs font-semibold text-[#86868b] uppercase tracking-widest mb-2">主推方案</p>
                  <p class="text-3xl font-bold text-[#1d1d1f] sf-pro-display">¥{sogoBrand.data.price_yearly || '-'}</p>
                  <p class="text-sm text-[#86868b] mt-1">按年支付</p>
                </div>
                
                <div class="bg-white p-8 flex flex-col justify-center items-center text-center">
                  <p class="text-xs font-semibold text-[#86868b] uppercase tracking-widest mb-2">包含流量</p>
                  <p class="text-3xl font-bold text-[#1d1d1f] sf-pro-display">{sogoBrand.data.bandwidth_gb}GB</p>
                  <p class="text-sm text-[#86868b] mt-1">每月重置</p>
                </div>
                
                <div class="bg-white p-8 col-span-2">
                  <h4 class="text-xs font-semibold text-[#86868b] uppercase tracking-widest mb-4 text-center">核心优势</h4>
                  <ul class="space-y-4">
                    <li class="flex items-start">
                      <span class="text-[#0071e3] mr-3 font-bold">•</span>
                      <span class="text-[#1d1d1f] text-sm md:text-base">
                        套餐 ¥98/年，含 60GB/月高速流量（每 30 天自动重置）。
                      </span>
                    </li>
                    <li class="flex items-start">
                      <span class="text-[#0071e3] mr-3 font-bold">•</span>
                      <span class="text-[#1d1d1f] text-sm md:text-base">
                        全节点 x1 倍率，且设备并发使用数量不限。
                      </span>
                    </li>
                  </ul>
                </div>
                
              </div>
            </div>
            
          </div>
        </div>
      </section>
    )}

    <!-- 其他选择 -->
    <section>
      <div class="text-center mb-12">
        <h3 class="text-3xl md:text-4xl font-bold text-[#1d1d1f] sf-pro-display mb-4">更多选择。</h3>
        <a href="/duibi/" class="text-[17px] text-[#0071e3] hover:underline flex items-center justify-center gap-1">
          比较所有品牌参数 <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </a>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {otherBrands.map(brand => (
          <div class="apple-card p-8 flex flex-col h-full cursor-pointer hover:shadow-md" onclick={`window.location.href='/brands/${brand.id}/'`}>
            
            <div class="flex flex-col items-center text-center mb-8">
              <div class="h-12 flex items-center justify-center mb-4">
                {brand.data.logo ? (
                  <img src={brand.data.logo} alt={`${brand.data.name} logo`} class="max-h-full max-w-[100px] object-contain" />
                ) : (
                  <span class="text-lg font-bold text-[#86868b]">{brand.data.name}</span>
                )}
              </div>
              <h4 class="text-xl font-bold text-[#1d1d1f] sf-pro-display">{brand.data.name}</h4>
            </div>
            
            <div class="grid grid-cols-2 gap-4 mb-8 flex-grow">
              <div class="text-center">
                <p class="text-[11px] font-semibold text-[#86868b] uppercase tracking-widest mb-1">价格</p>
                <p class="text-lg font-semibold text-[#1d1d1f]">¥{brand.data.price_monthly || brand.data.price_yearly || '-'}</p>
                <p class="text-[11px] text-[#86868b]">{brand.data.price_monthly ? '起/月' : '起/年'}</p>
              </div>
              <div class="text-center">
                <p class="text-[11px] font-semibold text-[#86868b] uppercase tracking-widest mb-1">流量</p>
                <p class="text-lg font-semibold text-[#1d1d1f]">{brand.data.bandwidth_gb}GB</p>
                <p class="text-[11px] text-[#86868b]">
                  {brand.data.bandwidth_reset_period === 'monthly' ? '月度重置' : 
                   brand.data.bandwidth_reset_period === 'none' ? '一次性' : '周期未知'}
                </p>
              </div>
            </div>
            
            <div class="flex flex-col gap-3 mt-auto">
              <a href={brand.data.register_link} target="_blank" rel="noopener sponsored" onclick="event.stopPropagation()" class="w-full py-3 rounded-full text-sm font-semibold text-center text-white bg-[#0071e3] hover:bg-[#0077ed] transition-colors">
                前往官网
              </a>
              <a href={`/brands/${brand.id}/`} class="w-full py-3 rounded-full text-sm font-semibold text-center text-[#1d1d1f] bg-[#e8e8ed] hover:bg-[#d2d2d7] transition-colors">
                查看详情
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

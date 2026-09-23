import os

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
    background-color: #f8fafc;
    /* Subtle plus pattern for a premium tech feel */
    background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%2364748b' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  }
</style>

<BaseLayout title="2026 机场推荐PRO：25 个品牌套餐资料与选购指南" description="整理 Sogo云及其他品牌的公开套餐价格、付款周期和流量规则，按需求查看便宜机场、品牌对比与编辑推荐顺序；本站未实测。">
  
  <div class="space-y-16 pb-20">
    <!-- 英雄区 -->
    <section class="relative bg-slate-950 rounded-[2.5rem] py-16 md:py-24 px-8 md:px-16 shadow-[0_20px_50px_rgba(15,23,42,0.3)] overflow-hidden border border-slate-800">
      <!-- 动态渐变背景 -->
      <div class="absolute inset-0 bg-gradient-to-br from-indigo-900/40 via-slate-900 to-purple-900/40"></div>
      
      <!-- 网格点阵纹理 -->
      <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 24px 24px;"></div>
      
      <!-- 发光装饰球 -->
      <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div class="absolute -top-40 -right-40 w-[40rem] h-[40rem] bg-blue-600/20 rounded-full mix-blend-screen filter blur-[120px]"></div>
        <div class="absolute -bottom-40 -left-20 w-[30rem] h-[30rem] bg-fuchsia-600/20 rounded-full mix-blend-screen filter blur-[100px]"></div>
      </div>
      
      <div class="relative z-10 text-center max-w-4xl mx-auto">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-800/80 border border-slate-700 shadow-xl backdrop-blur-md text-blue-300 text-sm font-semibold mb-8 tracking-wide">
          <span class="flex h-2.5 w-2.5 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-500 shadow-[0_0_8px_rgba(59,130,246,0.8)]"></span>
          </span>
          2026 全新收录与评测数据
        </div>
        <h1 class="text-4xl font-extrabold text-white tracking-tight sm:text-6xl md:text-7xl drop-shadow-2xl">
          寻找最适合您的<br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400">机场网络</span>
        </h1>
        <p class="mt-8 text-lg md:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed font-light">
          本站整理品牌公开资料，帮助您按预算、流量和付款周期比较。当前收录品牌尚未由本站独立实测；购买前请核对官方最新套餐与限制。
        </p>
      </div>
    </section>

    <!-- 演示数据提示 -->
    {allBrands.some(b => b.data.is_dummy) && (
      <div class="bg-gradient-to-r from-amber-50 to-yellow-50 border border-amber-200/50 p-5 rounded-2xl shadow-sm backdrop-blur-sm">
        <div class="flex items-start">
          <div class="flex-shrink-0 mt-0.5">
            <svg class="h-6 w-6 text-amber-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-4">
            <p class="text-sm text-amber-800 leading-relaxed">
              <strong class="font-bold text-amber-900">当前包含演示数据。</strong> 下方展示的部分品牌信息及链接均为占位符，正式线上部署时将自动隐藏此数据，如有占位域名也会阻止发布。
            </p>
          </div>
        </div>
      </div>
    )}

    <!-- 本站主推 Sogo云 -->
    {sogoBrand && (
      <section class="relative">
        <div class="flex items-center gap-4 mb-8">
          <div class="h-10 w-1.5 bg-gradient-to-b from-blue-500 to-purple-600 rounded-full"></div>
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight">本站主推</h2>
        </div>
        
        <!-- 炫彩流光边框包装层 -->
        <div class="relative p-[2px] rounded-[2rem] shadow-xl hover:shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 group overflow-hidden">
          <!-- 静态渐变背景，悬浮时稍微提亮 -->
          <div class="absolute inset-0 bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500 opacity-80 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative bg-white rounded-[calc(2rem-2px)] p-8 md:p-12 overflow-hidden">
            <!-- 卡片内部的高级光影点缀 -->
            <div class="absolute -top-24 -right-24 w-64 h-64 bg-gradient-to-br from-blue-100 to-purple-100 rounded-full opacity-60 filter blur-3xl pointer-events-none group-hover:scale-125 transition-transform duration-700"></div>
            
            <!-- 站长力荐 Badge -->
            <div class="absolute top-0 right-0 bg-gradient-to-l from-orange-500 to-amber-400 text-white text-xs font-bold px-6 py-2 rounded-bl-2xl shadow-lg z-10 flex items-center gap-1.5 tracking-wider">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
              站长力荐
            </div>
            
            <div class="flex flex-col lg:flex-row lg:justify-between items-start gap-10 relative z-10">
              <div class="flex-1 w-full">
                <div class="flex items-center gap-6">
                  {sogoBrand.data.logo && (
                    <div class="bg-white p-3 rounded-2xl shadow-[0_4px_20px_rgb(0,0,0,0.06)] border border-slate-100 flex-shrink-0">
                      <img src={sogoBrand.data.logo} alt={`${sogoBrand.data.name} logo`} class="h-16 w-auto max-w-[140px] object-contain" />
                    </div>
                  )}
                  <a href={`/brands/${sogoBrand.id}/`} class="text-4xl font-black text-slate-900 hover:text-blue-600 transition-colors bg-clip-text">
                    {sogoBrand.data.name}
                  </a>
                </div>
                
                <div class="mt-8 flex flex-col sm:flex-row gap-4">
                  <div class="flex-1 bg-gradient-to-br from-blue-50/80 to-indigo-50/50 rounded-2xl p-5 border border-blue-100/60 shadow-sm">
                    <p class="text-sm text-blue-600 font-semibold mb-1 uppercase tracking-wider">首选套餐方案</p>
                    <p class="text-slate-800 font-bold text-2xl">
                      {sogoBrand.data.price_yearly ? `年付 ¥ ${sogoBrand.data.price_yearly}` : '价格待查'}
                      <span class="text-sm text-slate-500 font-normal ml-2">（约 ¥{(sogoBrand.data.price_yearly / 12).toFixed(2)} / 月）</span>
                    </p>
                  </div>
                  <div class="flex-1 bg-gradient-to-br from-slate-50 to-gray-50/50 rounded-2xl p-5 border border-slate-200/60 shadow-sm">
                    <p class="text-sm text-slate-500 font-semibold mb-1 uppercase tracking-wider">套餐流量</p>
                    <p class="text-slate-800 font-bold text-2xl">
                      {sogoBrand.data.bandwidth_gb} <span class="text-lg">GB</span>
                      <span class="text-sm text-slate-500 font-normal ml-2">/ 月重置</span>
                    </p>
                  </div>
                </div>

                <div class="mt-8">
                  <h4 class="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">核心亮点</h4>
                  <ul class="space-y-4">
                    <li class="flex items-start">
                      <div class="bg-gradient-to-br from-green-400 to-emerald-500 rounded-full p-1.5 mr-4 mt-0.5 shadow-sm shadow-green-500/20 flex-shrink-0">
                        <svg class="h-3.5 w-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                      </div>
                      <span class="text-slate-700 leading-relaxed"><strong class="text-slate-900 font-bold">官方套餐资料：</strong>套餐 ¥98/年，含 60GB/月高速流量（每 30 天自动重置）。</span>
                    </li>
                    <li class="flex items-start">
                      <div class="bg-gradient-to-br from-green-400 to-emerald-500 rounded-full p-1.5 mr-4 mt-0.5 shadow-sm shadow-green-500/20 flex-shrink-0">
                        <svg class="h-3.5 w-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                      </div>
                      <span class="text-slate-700 leading-relaxed"><strong class="text-slate-900 font-bold">官方宣称卖点：</strong>全节点 x1 倍率，且设备并发使用数量不限。</span>
                    </li>
                  </ul>
                </div>
              </div>
              
              <div class="w-full lg:w-72 flex flex-col items-stretch gap-4 mt-4 lg:mt-0 pt-8 lg:pt-0 border-t lg:border-t-0 border-slate-100">
                <a href={sogoBrand.data.register_link} target="_blank" rel="noopener sponsored" class="group relative flex justify-center items-center px-8 py-4 rounded-xl text-white font-bold bg-slate-900 overflow-hidden shadow-[0_8px_20px_rgb(0,0,0,0.12)] hover:shadow-[0_8px_25px_rgba(59,130,246,0.3)] transition-all duration-300">
                  <div class="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <span class="relative z-10 flex items-center gap-2">
                    前往官网注册
                    <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                  </span>
                </a>
                <a href={`/brands/${sogoBrand.id}/`} class="flex justify-center items-center px-8 py-3.5 rounded-xl text-slate-700 font-semibold bg-slate-50 border border-slate-200 hover:bg-slate-100 hover:border-slate-300 transition-colors duration-200">
                  查看品牌详情
                </a>
                <div class="mt-4 p-4 bg-slate-50 rounded-xl border border-slate-100">
                  <p class="text-xs text-slate-500 flex items-center justify-center gap-1.5">
                    <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    核验于: {sogoBrand.data.verification_date}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    )}

    <!-- 其他选择 -->
    <section>
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 mb-10 border-b border-slate-200/80 pb-5">
        <div class="flex items-center gap-4">
          <div class="h-10 w-1.5 bg-slate-400 rounded-full"></div>
          <div>
            <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight">更多收录选择</h2>
            <p class="text-slate-500 mt-2">按需挑选适合您的备用或平替网络</p>
          </div>
        </div>
        <a href="/duibi/" class="inline-flex items-center justify-center px-5 py-2.5 rounded-lg bg-blue-50 text-blue-700 text-sm font-bold hover:bg-blue-100 hover:shadow-sm transition-all group">
          查看完整参数对比 
          <svg class="w-4 h-4 ml-1.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
        </a>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 md:gap-8">
        {otherBrands.map(brand => (
          <div class="group bg-gradient-to-b from-white to-slate-50/50 rounded-2xl shadow-sm border border-slate-200/70 flex flex-col hover:shadow-xl hover:border-blue-300/50 hover:-translate-y-1.5 transition-all duration-300 relative overflow-hidden">
            <!-- 顶部装饰线 -->
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-slate-200 to-slate-200 group-hover:from-cyan-400 group-hover:to-blue-500 transition-colors duration-500"></div>
            
            <div class="p-6 md:p-7 flex-grow flex flex-col">
              <div class="flex items-center gap-4 mb-6">
                {brand.data.logo ? (
                  <div class="bg-white p-2 rounded-xl border border-slate-100 shadow-[0_2px_10px_rgb(0,0,0,0.04)] flex-shrink-0">
                    <img src={brand.data.logo} alt={`${brand.data.name} logo`} class="h-10 w-auto max-w-[80px] object-contain" />
                  </div>
                ) : (
                  <div class="h-14 w-14 bg-gradient-to-br from-slate-100 to-slate-200 rounded-xl border border-slate-200 flex items-center justify-center flex-shrink-0 shadow-sm">
                    <span class="text-slate-500 text-lg font-black">{brand.data.name.substring(0,2)}</span>
                  </div>
                )}
                <h3 class="text-xl font-bold text-slate-900 truncate">
                  <a href={`/brands/${brand.id}/`} class="hover:text-blue-600 transition-colors before:absolute before:inset-0">{brand.data.name}</a>
                </h3>
              </div>
              
              <!-- 核心参数区 -->
              <div class="bg-white rounded-xl p-4 border border-slate-100 shadow-sm mb-5">
                <div class="flex justify-between items-center py-1.5 border-b border-slate-50 last:border-0">
                  <span class="text-xs font-bold text-slate-400 uppercase tracking-wider bg-slate-50 px-2 py-1 rounded">月付</span>
                  <span class="font-bold text-slate-800">{brand.data.price_monthly ? `${brand.data.currency} ${brand.data.price_monthly}` : '-'}</span>
                </div>
                <div class="flex justify-between items-center py-1.5 border-b border-slate-50 last:border-0">
                  <span class="text-xs font-bold text-slate-400 uppercase tracking-wider bg-slate-50 px-2 py-1 rounded">年付</span>
                  <span class="font-bold text-slate-800">{brand.data.price_yearly ? `${brand.data.currency} ${brand.data.price_yearly}` : '-'}</span>
                </div>
                <div class="flex justify-between items-center py-1.5 pt-2">
                  <span class="text-xs font-bold text-blue-500 uppercase tracking-wider bg-blue-50 px-2 py-1 rounded">流量</span>
                  <span class="font-bold text-blue-600 text-lg">{brand.data.bandwidth_gb} <span class="text-sm">GB</span></span>
                </div>
              </div>

              <!-- 卖点列表 -->
              <div class="mt-auto">
                <ul class="space-y-2.5 text-slate-600 text-sm">
                  {brand.data.features && brand.data.features.length > 0 ? (
                    brand.data.features.slice(0, 3).map(f => (
                      <li class="flex items-start">
                        <div class="mt-0.5 mr-2.5 flex-shrink-0 bg-blue-50 rounded text-blue-500 p-0.5">
                          <svg class="h-3 w-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                        </div>
                        <span class="leading-relaxed line-clamp-2">{f}</span>
                      </li>
                    ))
                  ) : (
                    <li class="flex items-start text-slate-400 italic">
                      <div class="mt-0.5 mr-2.5 flex-shrink-0 bg-slate-50 rounded text-slate-400 p-0.5">
                        <svg class="h-3 w-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                      </div>
                      具体套餐特性请参考官方说明
                    </li>
                  )}
                </ul>
              </div>
            </div>
            
            <div class="px-6 pb-6 pt-2 relative z-20">
              <a href={brand.data.register_link} target="_blank" rel="noopener sponsored" class="flex justify-center items-center w-full px-4 py-3 rounded-xl text-sm font-bold text-white bg-slate-800 hover:bg-blue-600 shadow-md hover:shadow-lg hover:shadow-blue-500/20 transform hover:-translate-y-0.5 transition-all duration-300">
                官网注册
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

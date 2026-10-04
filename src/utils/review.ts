import type { PlanItem } from '../data/plans';
import { type BrandView, fmtGB, fmtPrice, monthlyEq, perGB, billingLabel } from './data';

export const USAGE = [
  { label: '轻度', need: 50, desc: '查资料、用 ChatGPT、刷社交软件' },
  { label: '日常', need: 150, desc: '每天 1–2 小时 YouTube、短视频' },
  { label: '追剧', need: 300, desc: '经常看 1080P/4K 剧集' },
  { label: '重度', need: 600, desc: '全家共用、大文件下载' },
] as const;

/** 满足流量需求、折合月价最低的周期套餐 */
export function cheapestFor(b: BrandView, need: number): PlanItem | null {
  const ok = b.plans.filter((p) => p.billing !== 'One-Time' && (p.traffic ?? 0) >= need);
  return ok.sort((x, y) => (monthlyEq(x) ?? 1e9) - (monthlyEq(y) ?? 1e9))[0] ?? null;
}

export function planPriceText(p: PlanItem): string {
  const m = monthlyEq(p);
  if (p.billing === 'Monthly') return `${fmtPrice(p.price)}/月`;
  if (p.billing === 'One-Time') return `${fmtPrice(p.price)} 一次性`;
  return `${fmtPrice(p.price)}/${billingLabel(p.billing).replace('付', '')}（约 ${fmtPrice(m!)}/月）`;
}

export const unlockText = (b: BrandView) =>
  b.streaming && b.ai ? '流媒体 + AI' : b.streaming ? '流媒体' : b.ai ? 'AI' : '官网未写明';

/** 一句话定位（用于卡片和排行榜） */
export function oneLiner(b: BrandView): string {
  const parts: string[] = [];
  if (b.entry) parts.push(`月付 ${fmtPrice(b.entry.price)} 起 ${fmtGB(b.entry.traffic)}`);
  if (b.premium) parts.push(`${b.lineLabel} 专线`);
  else parts.push(`${b.lineLabel} 线路`);
  if (b.minYearly) parts.push(`年付 ${fmtPrice(b.minYearly.price)} 小包`);
  if (b.oneTime.length) parts.push('有不限时包');
  return parts.join('，');
}

export function prosCons(b: BrandView, avgEntry: number) {
  const pros: string[] = [];
  const cons: string[] = [];
  if (b.premium) pros.push(`${b.lineLabel} 专线，晚高峰比普通中转线路稳定`);
  else cons.push(`${b.lineLabel} 线路不是 IPLC/IEPL 专线，晚高峰延迟可能波动`);
  if (b.entry) {
    if (b.entry.price <= avgEntry) pros.push(`月付 ${fmtPrice(b.entry.price)} 起，低于收录机场的平均起步价 ${fmtPrice(avgEntry)}`);
    else cons.push(`月付起步 ${fmtPrice(b.entry.price)}，高于收录机场的平均起步价 ${fmtPrice(avgEntry)}`);
  } else cons.push('没有标准月付套餐');
  if (b.minYearly) pros.push(`年付小包 ${fmtPrice(b.minYearly.price)}，折合每月 ${fmtPrice(b.minYearly.price / 12)}`);
  if (b.oneTime.length) pros.push(`${b.oneTime.length} 款不限时流量包，${fmtPrice(b.oneTime[0].price)} 起，流量不过期`);
  else cons.push('没有不限时流量包，不适合只做备用');
  if (b.streaming && b.ai) pros.push('官网写明支持 Netflix 等流媒体和 ChatGPT 等 AI');
  else cons.push('官网没有完整写明流媒体 / AI 解锁，买前可问客服');
  if (b.maxTraffic && b.maxTraffic < 500) cons.push(`最高只有 ${fmtGB(b.maxTraffic)}/月，重度用户不够用`);
  if (b.bestValue && perGB(b.bestValue)! < 0.1) pros.push(`${b.bestValue.name} 约 ${fmtPrice(perGB(b.bestValue)!)}/GB，单价偏低`);
  return { pros: pros.slice(0, 5), cons: cons.slice(0, 4) };
}

export function brandFaq(b: BrandView): { q: string; a: string }[] {
  const out: { q: string; a: string }[] = [];
  out.push({
    q: `${b.name}怎么样？`,
    a: `${b.name}${oneLiner(b)}。${b.premium ? '专线机场晚高峰表现通常更稳，' : ''}建议第一次先买最低一档月付，确认常用网站和晚高峰速度满意后再续费。`,
  });
  if (b.entry)
    out.push({
      q: `${b.name}多少钱一个月？`,
      a: `${b.name}月付最低 ${fmtPrice(b.entry.price)}（${b.entry.name}，每月 ${fmtGB(b.entry.traffic)}）。${
        b.minYearly ? `只想年付的话，${b.minYearly.name} ${fmtPrice(b.minYearly.price)}/年，每月 ${fmtGB(b.minYearly.traffic)}。` : ''
      }`,
    });
  out.push({
    q: `${b.name}能用 ChatGPT 和 Netflix 吗？`,
    a: b.streaming && b.ai
      ? `可以，${b.name}官网写明支持 Netflix 等流媒体和 ChatGPT 等 AI 工具。个别节点解锁情况会变化，遇到问题换个节点即可。`
      : `${b.name}官网对这部分写得不完整（${unlockText(b)}）。如果这是你的主要用途，购买前先问客服，或者看本站的流媒体解锁机场推荐。`,
  });
  out.push({
    q: `${b.name}有不限时套餐吗？`,
    a: b.oneTime.length
      ? `有，共 ${b.oneTime.length} 款：${b.oneTime.map((p) => `${fmtGB(p.traffic)} ${fmtPrice(p.price)}`).join('、')}，流量用完为止、不会过期。`
      : `没有，${b.name}只有周期订阅，流量按月重置。`,
  });
  if (b.promo) out.push({ q: `${b.name}优惠码是多少？`, a: `${b.name}优惠码：${b.promo}。在官网下单结算页填写，折扣以结算页显示为准。` });
  return out;
}

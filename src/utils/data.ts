import { getCollection, type CollectionEntry } from 'astro:content';
import { PLANS, type PlanItem, type BrandPlans } from '../data/plans';

export const SITE_NAME = '机场推荐PRO';
export const SITE_URL = 'https://jichangtuijianpro.com';
/** 全站“最后更新”日期：更新内容或排名后改这里 */
export const UPDATED = '2026-11-01';
export const UPDATED_LABEL = '2026年11月1日';
export const UPDATED_MONTH = '2026年11月';
export const UPDATED_MONTH_SHORT = '11月';
/** 套餐数据最后一次对照官网核对的日期：重新核对价格后再改这里 */
export const PLANS_VERIFIED_LABEL = '2026年10月4日';

export const getBrands = async () => {
  const allBrands = await getCollection('brands');
  const isDev = import.meta.env.DEV;
  const isPreview = import.meta.env.IS_PREVIEW === 'true';
  const list = isDev || isPreview ? allBrands : allBrands.filter((b) => !b.data.is_dummy);
  if (!list.length) {
    throw new Error('【构建阻止】正式构建必须包含至少一个真实的非占位品牌数据！');
  }
  return list.sort((a, b) => a.data.sort_order - b.data.sort_order || a.data.name.localeCompare(b.data.name));
};

/* ---------------- 格式化 ---------------- */
export function fmtGB(g: number | null | undefined): string {
  if (g === null || g === undefined) return '未说明';
  if (g >= 1000) return `${+(g / 1000).toFixed(2)}TB`;
  return `${+g.toFixed(1)}GB`;
}
export const fmtPrice = (n: number) => `¥${+n.toFixed(2)}`;
/** '2026-10-04' -> '2026年10月4日' */
export const dateLabel = (d: string) => {
  const [y, m, day] = d.split('-').map(Number);
  return `${y}年${m}月${day}日`;
};
export const billingLabel = (b: PlanItem['billing']) =>
  ({ Monthly: '月付', Quarterly: '季付', Yearly: '年付', 'One-Time': '一次性' } as const)[b];

/** 折合每月价格；一次性套餐返回 null */
export function monthlyEq(p: PlanItem): number | null {
  if (p.billing === 'Monthly') return p.price;
  if (p.billing === 'Quarterly') return p.price / 3;
  if (p.billing === 'Yearly') return p.price / 12;
  return null;
}
/** 每 GB 成本：周期套餐 = 每月价格 ÷ 每月流量；一次性 = 总价 ÷ 总流量 */
export function perGB(p: PlanItem): number | null {
  if (!p.traffic) return null;
  return (monthlyEq(p) ?? p.price) / p.traffic;
}

/* ---------------- 品牌视图模型 ---------------- */
export interface BrandView {
  id: string; // 内容文件名（中文）
  slug: string; // 拼音网址
  url: string;
  name: string;
  logo?: string;
  register: string;
  rank: number;
  promo: string | null;
  lines: string[];
  lineLabel: string;
  premium: boolean; // IPLC / IEPL 专线
  streaming: boolean | null;
  ai: boolean | null;
  nodeRegions: string | null;
  plans: PlanItem[];
  monthly: PlanItem[];
  yearly: PlanItem[];
  oneTime: PlanItem[];
  entry: PlanItem | null; // 最低月付套餐
  minYearly: PlanItem | null;
  bestValue: PlanItem | null; // 每 GB 最便宜的周期套餐
  maxTraffic: number;
  minTraffic: number;
  verified: string;
  entry_data: CollectionEntry<'brands'>;
}

const SLUG_BY_FILE: Record<string, string> = Object.fromEntries(
  Object.entries(PLANS).map(([slug, v]) => [v.file, slug]),
);

export const brandSlug = (fileId: string) => SLUG_BY_FILE[fileId] ?? fileId;
export const brandUrl = (fileId: string) => `/brands/${brandSlug(fileId)}/`;

function toView(b: CollectionEntry<'brands'>): BrandView {
  const slug = brandSlug(b.id);
  const bp: BrandPlans | undefined = PLANS[slug];
  const plans = (bp?.plans ?? []).filter((p) => !p.custom);
  const by = (k: PlanItem['billing']) => plans.filter((p) => p.billing === k).sort((a, c) => a.price - c.price);
  const monthly = by('Monthly');
  const yearly = by('Yearly');
  const oneTime = by('One-Time');
  const periodic = plans.filter((p) => p.billing !== 'One-Time' && perGB(p) !== null);
  const bestValue = periodic.sort((a, c) => perGB(a)! - perGB(c)!)[0] ?? null;
  const traffic = plans.map((p) => p.traffic).filter((t): t is number => typeof t === 'number');
  const lines = bp?.lines ?? [];
  return {
    id: b.id,
    slug,
    url: `/brands/${slug}/`,
    name: b.data.name,
    logo: b.data.logo,
    register: b.data.register_link,
    rank: b.data.sort_order,
    promo: bp?.promo ?? null,
    lines,
    lineLabel: lines.length ? lines.join(' / ') : '官网未标注',
    premium: lines.some((l) => l === 'IPLC' || l === 'IEPL'),
    streaming: bp?.streaming ?? null,
    ai: bp?.ai ?? null,
    nodeRegions: bp?.nodeRegions ?? null,
    plans,
    monthly,
    yearly,
    oneTime,
    entry: monthly[0] ?? null,
    minYearly: yearly[0] ?? null,
    bestValue,
    maxTraffic: traffic.length ? Math.max(...traffic) : 0,
    minTraffic: traffic.length ? Math.min(...traffic) : 0,
    verified: b.data.verification_date,
    entry_data: b,
  };
}

export async function getBrandViews(): Promise<BrandView[]> {
  return (await getBrands()).map(toView);
}

/** 编辑推荐 Top N（sort_order < 999 的品牌） */
export const topPicks = (list: BrandView[], n = 10) => list.slice(0, n);

/** 所有周期/一次性套餐展开 */
export function allPlans(list: BrandView[]) {
  return list.flatMap((b) => b.plans.map((p) => ({ b, p })));
}

export function faqSchema(items: { q: string; a: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map((i) => ({ '@type': 'Question', name: i.q, acceptedAnswer: { '@type': 'Answer', text: i.a } })),
  };
}

export function itemListSchema(name: string, list: BrandView[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name,
    numberOfItems: list.length,
    itemListElement: list.map((b, i) => ({ '@type': 'ListItem', position: i + 1, name: b.name, url: `${SITE_URL}${b.url}` })),
  };
}

export function breadcrumbSchema(items: { name: string; path: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [{ name: '首页', path: '/' }, ...items].map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      item: `${SITE_URL}${it.path}`,
    })),
  };
}

/** 机场对比长尾页：/duibi/{a}-vs-{b}/ */
export const PAIRS: [string, string][] = [
  ['sogo', 'feimao'],
  ['sogo', 'weifeng'],
  ['sogo', 'wuyou'],
  ['sogo', 'firefly'],
  ['feimao', 'weifeng'],
  ['wuyou', 'kuajie'],
  ['firefly', 'shanyue'],
  ['kuajie', 'lingmao'],
];
export const pairSlug = (a: string, b: string) => `${a}-vs-${b}`;

/** 编辑推荐 Top 10：按 sort_order 排名，不足 10 家时用专线里每 GB 最便宜的补齐 */
export function top10(list: BrandView[]): BrandView[] {
  const picks = list.filter((b) => b.rank < 999);
  const rest = list
    .filter((b) => b.rank >= 999 && b.premium && b.bestValue)
    .sort((x, y) => perGB(x.bestValue!)! - perGB(y.bestValue!)!);
  return [...picks, ...rest].slice(0, 10);
}

export const avgEntryPrice = (list: BrandView[]) => {
  const e = list.filter((b) => b.entry).map((b) => b.entry!.price);
  return e.reduce((a, c) => a + c, 0) / Math.max(e.length, 1);
};

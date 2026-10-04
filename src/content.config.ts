import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const brandsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/brands" }),
  schema: z.object({
    sort_order: z.number().default(999),
    name: z.string(),
    official_site: z.url(),
    register_link: z.url(),
    logo: z.string().optional(),
    is_sponsored: z.boolean().default(false),
    currency: z.string().default('CNY'),
    price_monthly: z.number().optional(),
    price_yearly: z.number().optional(),
    bandwidth_gb: z.number(),
    bandwidth_reset_period: z.string(), // e.g., 'monthly', 'none'
    multiplier_desc: z.string().optional(),
    device_limit: z.number().optional(),
    refund_policy: z.string().optional(),
    verification_date: z.string(),
    evidence_status: z.string(),
    evidence_images: z.array(z.object({ src: z.string(), alt: z.string(), width: z.number(), height: z.number() })).optional(),
    is_dummy: z.boolean().default(false), // 标记演示数据，正式发布前需清理
    features: z.array(z.string()).optional(),
    seo_title: z.string().optional(),
    seo_description: z.string().optional(),
    seo_h1: z.string().optional(),
  }),
});

// 旧的 posts（测评文章）集合已停用：测评内容已合并进品牌评测页 /brands/{拼音}/。
// src/content/posts/ 文件夹可以直接删除。

export const collections = {
  'brands': brandsCollection,
};

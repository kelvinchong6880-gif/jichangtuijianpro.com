import { defineCollection } from 'astro:content';
import { z } from 'astro:schema';
import { glob } from 'astro/loaders';

const brandsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/brands" }),
  schema: z.object({
    sort_order: z.number().default(999),
    name: z.string(),
    official_site: z.string().url(),
    register_link: z.string().url(),
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
    is_dummy: z.boolean().default(false), // 鏍囪婕旂ず鏁版嵁锛屾寮忓彂甯冨墠闇€娓呯悊
    features: z.array(z.string()).optional(),
    seo_title: z.string().optional(),
    seo_description: z.string().optional(),
    seo_h1: z.string().optional(),
  }),
});

const postsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/posts" }),
  schema: z.object({
    sort_order: z.number().default(999),
    title: z.string(),
    description: z.string(),
    date: z.date(),
    updatedDate: z.date().optional(),
    keywords: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'brands': brandsCollection,
  'posts': postsCollection,
};

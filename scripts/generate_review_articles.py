#!/usr/bin/env python3
"""
为每个品牌在 src/content/posts/ 生成一篇测评文章（editorial review），
与 src/content/brands/ 下的官方套餐资料页分工：
- brands/ 页面：完整套餐价格表、逐项资料核对（已存在，不改动）
- posts/ 文章（本脚本生成）：怎么样/适合谁/编辑点评角度，不重复贴价格表，
  而是链接回 brands/ 页面看完整资料。

所有判断严格基于 frontmatter 中已披露的真实数据，不编造测速或使用体验。
"""
import re
import glob
from datetime import date

TODAY = date.today().isoformat()

files = sorted(glob.glob('src/content/brands/*.md'))
parsed = []
for f in files:
    content = open(f, encoding='utf-8').read()
    fm = re.match(r'^---\n(.*?)\n---\n', content, re.S).group(1)

    def get(key, default=None):
        m = re.search(rf'^{key}:\s*(.+)$', fm, re.M)
        return m.group(1).strip().strip('"') if m else default

    def get_list(key):
        m = re.search(rf'^{key}:\n((?:\s+-.*\n?)+)', fm, re.M)
        if not m:
            return []
        lines = m.group(1).strip('\n').split('\n')
        cleaned = []
        for l in lines:
            l = re.sub(r'^\s*-\s*"?', '', l)
            l = re.sub(r'"?\s*$', '', l)
            cleaned.append(l)
        return cleaned

    slug = f.split('/')[-1].replace('.md', '')
    name = get('name')
    py = float(get('price_yearly')) if get('price_yearly') else None
    pm = float(get('price_monthly')) if get('price_monthly') else None
    bw = float(get('bandwidth_gb'))
    reset = get('bandwidth_reset_period', 'monthly')
    ev = get('evidence_status', '官方宣称，本站未测')
    sponsored = get('is_sponsored', 'false') == 'true'
    refund = get('refund_policy')
    device_limit = get('device_limit')
    features = get_list('features')
    has_evidence_images = 'evidence_images:' in fm
    sort_order = get('sort_order', '999')

    price_for_ranking = pm if pm else (py / 12 if py else None)
    gb_per_month = bw if reset == 'monthly' else bw / 12
    cost_per_gb = (price_for_ranking / gb_per_month) if (price_for_ranking and gb_per_month) else None

    parsed.append({
        'slug': slug, 'name': name, 'py': py, 'pm': pm, 'bw': bw, 'reset': reset,
        'ev': ev, 'sponsored': sponsored, 'refund': refund, 'device_limit': device_limit,
        'features': features, 'has_evidence_images': has_evidence_images,
        'cost_per_gb': cost_per_gb, 'sort_order': sort_order,
    })

ranked = sorted([p for p in parsed if p['cost_per_gb']], key=lambda p: p['cost_per_gb'])
n = len(ranked)
tier_of = {}
rank_of = {}
for i, p in enumerate(ranked):
    rank_of[p['slug']] = i + 1
    if i < n / 3:
        tier_of[p['slug']] = 'cheap'
    elif i < 2 * n / 3:
        tier_of[p['slug']] = 'mid'
    else:
        tier_of[p['slug']] = 'expensive'


def fmt_price(p):
    parts = []
    if p['pm']:
        parts.append(f"¥{p['pm']:g}/月起")
    if p['py']:
        parts.append(f"¥{p['py']:g}/年")
    return '，'.join(parts) if parts else '价格资料未提供'


def explain_feature(line: str) -> str:
    """把官方 features 条目转成带一点解释的句子，而不是原样复述。"""
    if '专线' in line:
        return f"{line}。官方专线宣传通常意味着与普通中转相比，晚高峰更不容易被运营商限速，但本站没有独立测速验证这一点，具体表现建议自己实测。"
    if '解锁' in line:
        return f"{line}。这类解锁能力会随节点 IP 池变化而波动，官方宣传的支持列表不等于任何时间点都 100% 可用。"
    if '设备' in line or '并发' in line:
        return f"{line}，对多设备（手机+电脑+路由器同时挂）用户比较友好。"
    if '倍率' in line:
        return f"{line}，使用被标高倍率的节点会更快消耗套餐流量，选节点时留意一下。"
    if '计费' in line or '不过期' in line:
        return f"{line}，适合用量不稳定、不想被按月清零卡节奏的用户。"
    return f"{line}（官方资料原文）。"


for p in parsed:
    name = p['name']
    slug = p['slug']
    tier = tier_of.get(slug, 'mid')
    rank = rank_of.get(slug)

    # ---- 适合谁 / 谨慎考虑 ----
    audience = []
    caution = []
    if p['bw'] >= 500:
        audience.append("流量额度大，适合重度流媒体、多设备长期在线的用户")
    elif p['bw'] >= 100:
        audience.append("流量额度中等，适合每天有稳定使用时长但不算重度的用户")
    else:
        audience.append("流量额度偏小，适合偶尔查资料的轻量用户")
        caution.append("重度用户大概率不够用，注意加油包或升级成本")

    if tier == 'cheap' and rank:
        audience.append(f"官方标价折算后，单位流量成本在本站收录的 {n} 家品牌中排第 {rank} 便宜，预算有限时值得放进候选")
    elif tier == 'expensive' and rank:
        caution.append(f"官方标价折算后，单位流量成本在本站收录的 {n} 家品牌中排第 {n - rank + 1} 贵，如果只是要便宜大流量，建议先对比本站「性价比」分类")

    if p['reset'] == 'none':
        audience.append("流量为一次性额度、用完即止，适合想自己灵活规划用量节奏的用户")
        caution.append("旺季容易提前用完，没有按月重置兜底")

    if p['device_limit']:
        audience.append(f"官方标注设备限制为 {p['device_limit']}，多设备用户购买前确认一下够不够用")

    caution.append(f"资料来源标注为「{p['ev']}」，本站尚未对晚高峰速率、真实解锁效果、长期稳定性做独立验证")

    audience_html = "\n".join(f"- {a}" for a in audience)
    caution_html = "\n".join(f"- {c}" for c in caution)

    # ---- 官方主打卖点 ----
    if p['features']:
        feature_html = "\n".join(f"- {explain_feature(f)}" for f in p['features'])
    else:
        feature_html = "- 官方公开资料中未提供进一步的卖点说明，具体以购买时页面展示为准。"

    # ---- 证据部分 ----
    if p['has_evidence_images']:
        evidence_para = f"{name}是本站目前唯一有真实用户截图佐证的品牌：有用户提供了节点延迟测试截图，显示部分节点连通、部分节点（如新加坡、台湾某些编号节点）出现过 Timeout。这些截图只反映延迟（ms），不代表下载速度或长期稳定性，具体请看完整套餐资料页里的截图和说明。"
    else:
        evidence_para = f"{name}目前资料来源标注为「{p['ev']}」，本站没有该品牌的实测截图或测速记录，以下内容全部来自官网公开资料，购买前建议自己用短周期套餐验证。"

    # ---- FAQ ----
    faqs = []
    if p['refund']:
        faqs.append((f"{name}支持退款吗？", f"官方资料标注的退款政策是：{p['refund']}。具体条款和执行细节以官网结算页当时展示为准，建议下单前截图保存。"))
    else:
        faqs.append((f"{name}支持退款吗？", "官方公开资料未明确说明退款政策，购买前建议直接联系客服确认，或在官网结算页查看条款。"))
    faqs.append((f"{name}年付划算还是月付划算？", "年付通常单价更低，但也意味着一次性投入更多、体验不满意难以退出。如果是第一次尝试这家，建议先用最短付费周期实测晚高峰速率和解锁效果，确认符合预期后再考虑年付。"))
    if tier == 'expensive':
        faqs.append((f"{name}价格是不是偏高？", f"按官方标价折算，{name}的单位流量成本在本站收录的 {n} 家品牌里确实偏贵。如果预算优先，可以看本站「性价比机场推荐」里的其它选项；如果更看重官方宣传的专线/服务，可以再权衡。"))

    faq_html = "\n\n".join(f"**Q：{q}**\n\nA：{a}" for q, a in faqs)

    body = f"""> 本文是编辑点评角度的测评文章，完整套餐价格表和逐项资料核对请看 [{name} 官方套餐资料页](/brands/{slug}/)。以下判断均基于该品牌官网公开资料，本站{'已有部分用户截图佐证，但仍未' if p['has_evidence_images'] else '尚未'}独立实测晚高峰速率和长期稳定性。

## 一句话结论

{name}目前主推套餐{fmt_price(p)}，流量额度约 {int(p['bw'])}GB（{'按月重置' if p['reset'] == 'monthly' else '一次性额度，用完即止'}）。{'官方资料显示走专线线路，' if any('专线' in f for f in p['features']) else ''}资料来源标注为「{p['ev']}」。

## 适合谁

{audience_html}

## 谨慎考虑的情况

{caution_html}

## 官方主打卖点解读

{feature_html}

## 证据与局限

{evidence_para}

## 常见问题

{faq_html}

## 编辑点评

综合官方披露的价格、流量和功能资料看，{name}{'走的是官方宣称的专线+功能路线，' if any('专线' in f for f in p['features']) else ''}{'单位流量成本在同类品牌中较有优势，适合预算有限、想先试试看的用户。' if tier == 'cheap' else ('单位流量成本在同类品牌中偏高，更适合看重官方宣传功能、愿意为此多付一些的用户。' if tier == 'expensive' else '单位流量成本处于同类品牌中间水平，选择时更应关注节点覆盖和自己的实际使用场景是否匹配。')}建议先用最短付费周期验证晚高峰速率和解锁效果，确认符合预期后再考虑长期订阅。{'本文包含与该品牌的推广合作链接，上述判断仍基于同一套客观数据标准给出，请知悉这一利益关系。' if p['sponsored'] else ''}
"""

    title = f"{name}测评：2026年套餐、价格与适用人群解析"
    description = f"{name}怎么样？本文从适合谁、官方卖点、证据与局限几个角度点评{name}的套餐，并附完整套餐资料链接。资料来源：{p['ev']}。"

    frontmatter = f"""---
title: "{title}"
description: "{description}"
date: {TODAY}
sort_order: {p['sort_order']}
keywords: ["{name}测评", "{name}怎么样", "{name}评测", "机场推荐"]
---

"""

    with open(f'src/content/posts/{slug}.md', 'w', encoding='utf-8') as fh:
        fh.write(frontmatter + body)

print(f"已生成 {len(parsed)} 篇测评文章")

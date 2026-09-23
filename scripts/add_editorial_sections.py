#!/usr/bin/env python3
"""
为 src/content/brands/*.md 批量补充 ## 适用人群 / ## 核心限制与缺点 / ## 编辑点评
三个板块。所有判断均严格基于 frontmatter 中已披露的真实数据（价格、流量、
重置周期、evidence_status），不编造测速结果或使用体验。
"""
import re
import glob

files = sorted(glob.glob('src/content/brands/*.md'))

parsed = []
for f in files:
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    fm = re.match(r'^---\n(.*?)\n---\n', content, re.S).group(1)

    def get(key, default=None):
        m = re.search(rf'^{key}:\s*(.+)$', fm, re.M)
        return m.group(1).strip().strip('"') if m else default

    name = get('name')
    py = float(get('price_yearly'))
    pm_field = get('price_monthly')
    bw = float(get('bandwidth_gb'))
    reset = get('bandwidth_reset_period', 'monthly')
    ev = get('evidence_status', '官方宣称，本站未测')
    sponsored = get('is_sponsored', 'false') == 'true'

    monthly_equiv = py / 12
    if reset == 'monthly':
        gb_per_month = bw
    else:
        gb_per_month = bw / 12
    cost_per_gb = monthly_equiv / gb_per_month if gb_per_month else None

    parsed.append({
        'file': f, 'content': content, 'name': name, 'py': py,
        'pm_field': pm_field, 'bw': bw, 'reset': reset, 'ev': ev,
        'sponsored': sponsored, 'monthly_equiv': monthly_equiv,
        'cost_per_gb': cost_per_gb,
    })

# 按每 GB 月成本排序，用于给出"在本站收录品牌中处于什么水位"这种可验证的相对判断
ranked = sorted([p for p in parsed if p['cost_per_gb']], key=lambda p: p['cost_per_gb'])
n = len(ranked)
tier_of = {}
for i, p in enumerate(ranked):
    if i < n / 3:
        tier_of[p['file']] = '低'  # 每GB成本最低 = 相对便宜
    elif i < 2 * n / 3:
        tier_of[p['file']] = '中'
    else:
        tier_of[p['file']] = '高'  # 每GB成本最高 = 相对偏贵

for p in parsed:
    name = p['name']
    bw = p['bw']
    reset = p['reset']
    monthly_equiv = p['monthly_equiv']
    cost_per_gb = p['cost_per_gb']
    tier = tier_of.get(p['file'], '中')

    # ---- 适用人群：基于流量规模与重置规则的客观推断 ----
    audience_lines = []
    if bw >= 500:
        audience_lines.append(f"流量额度（约 {int(bw)}GB/月）较大，适合日常重度使用流媒体、频繁使用 AI 工具或多设备长期在线的用户。")
    elif bw >= 100:
        audience_lines.append(f"流量额度（约 {int(bw)}GB/月）属于中等水平，适合每天有一定使用时长、但不算重度的用户。")
    else:
        audience_lines.append(f"流量额度（约 {int(bw)}GB/月）偏小，更适合只是偶尔查资料、轻量使用的用户，重度用户大概率不够用，需要留意加油包或升级成本。")
    if reset == 'none':
        audience_lines.append("流量为一次性额度、用完即止（不按月重置），适合用量不稳定、想自己灵活规划节奏的用户，但也意味着旺季容易提前用完。")
    audience = "\n".join(f"- {line}" for line in audience_lines)

    # ---- 核心限制与缺点：如实反映"未实测"这件事本身，以及基于数字的合理提醒 ----
    limit_lines = [f"资料来源标注为「{p['ev']}」，本站尚未对晚高峰速率、真实解锁情况、长期稳定性进行独立测速验证，以上判断均基于官方公开信息推导。"]
    if tier == '高':
        limit_lines.append(f"按官方标价折算，约合 {cost_per_gb:.3f} 元/GB/月，在本站收录的 {n} 家品牌中处于价格偏高的区间，建议先确认自己的实际流量需求，避免为用不完的流量多付费。")
    elif tier == '低':
        limit_lines.append(f"按官方标价折算，约合 {cost_per_gb:.3f} 元/GB/月，在本站收录的 {n} 家品牌中单价较低；单价低通常意味着线路成本压得更紧，建议优先用短周期套餐验证晚高峰体验后再考虑长期付费。")
    else:
        limit_lines.append(f"按官方标价折算，约合 {cost_per_gb:.3f} 元/GB/月，在本站收录的 {n} 家品牌中处于中间水位。")
    limit_lines.append("退款政策、限速细则、节点倍率等条款以官方页面实际展示为准，购买前建议截图保存当时的条款。")
    limits = "\n".join(f"- {line}" for line in limit_lines)

    # ---- 编辑点评 ----
    verdict_parts = [f"综合官方披露的价格与流量数据看，{name}目前"]
    if tier == '高':
        verdict_parts.append("定价在同类收录品牌中偏高，如果预算有限，建议先看看本站「性价比」分类里的其它选项做对比。")
    elif tier == '低':
        verdict_parts.append("单价在同类收录品牌中较有优势，但本站未做实测，建议先用最短付费周期试用，确认晚高峰速率和真实解锁效果符合预期后，再考虑年付。")
    else:
        verdict_parts.append("定价处于同类收录品牌的中间水平，没有明显的价格优势或劣势，选择时更应关注节点覆盖和自己的实际使用场景是否匹配。")
    if p['sponsored']:
        verdict_parts.append("\n\n**推广声明**：本文包含与该品牌的推广合作链接，上述判断仍基于同一套客观数据标准给出，但请知悉这一利益关系。")
    verdict = "".join(verdict_parts)

    new_sections = f"""
## 适用人群
{audience}

## 核心限制与缺点
{limits}

## 编辑点评
{verdict}
"""

    content = p['content']
    marker = "## 未明确资料"
    if marker in content:
        content = content.replace(marker, new_sections.strip() + "\n\n" + marker, 1)
    else:
        content = content.rstrip() + "\n" + new_sections

    with open(p['file'], 'w', encoding='utf-8') as fh:
        fh.write(content)

print(f"已处理 {len(parsed)} 个品牌文件")

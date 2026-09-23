import os, glob, re

brands_dir = 'src/content/brands'
md_files = glob.glob(os.path.join(brands_dir, '*.md'))

for file_path in md_files:
    if 'sogo.md' in file_path:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already have features in frontmatter
    if '\nfeatures:\n' in content:
        print(f"Skipping {file_path}, features already exist.")
        continue
        
    # Extract the text block
    text_match = re.search(r'```text\n(.*?)\n```', content, re.DOTALL)
    features = []
    if text_match:
        text_block = text_match.group(1)
        
        # Look for specific keywords
        if '不限时' in text_block or '按量' in text_block:
            features.append("包含不限时/按量计费套餐，流量不过期")
        if 'IPLC' in text_block.upper() or 'IEPL' in text_block.upper():
            if 'IPLC' in text_block.upper():
                features.append("官方宣称接入 IPLC 专线网络")
            else:
                features.append("官方宣称接入 IEPL 专线网络")
        if 'x1 倍率' in text_block or '1倍率' in text_block:
            features.append("全节点 x1 倍率，无高倍率节点陷阱")
        if '不限制设备' in text_block or '不限设备' in text_block or '无设备限制' in text_block:
            features.append("官方声明不限制设备同时在线数量")
        if '原生 IP' in text_block:
            features.append("主打原生 IP 线路，便于流媒体与 AI 服务访问")
        if '不限速' in text_block:
            features.append("官方承诺晚高峰时段不降速")
            
    # If we didn't find enough, add some generic fallback based on frontmatter
    if len(features) < 1:
        if 'price_monthly: ' in content:
            features.append("提供常规月付周期套餐")
        if 'bandwidth_reset_period: "monthly"' in content:
            features.append("标准按月重置流量模式")
            
    # Take up to 2 features
    features = features[:2]
    
    # If still empty, add a default
    if not features:
        features = ["具体套餐特性请参考官方说明"]
        
    # Build yaml array
    features_yaml = "features:\n"
    for f_str in features:
        features_yaml += f"  - \"{f_str}\"\n"
        
    # Insert into frontmatter
    content = content.replace('\nsort_order:', f'\n{features_yaml}sort_order:')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file_path} with {len(features)} features")


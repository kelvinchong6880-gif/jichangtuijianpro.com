import os, glob, re

brands_dir = 'src/content/brands'
md_files = glob.glob(os.path.join(brands_dir, '*.md'))

for file_path in md_files:
    if 'sogo.md' in file_path:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the text block
    text_match = re.search(r'```text\n(.*?)\n```', content, re.DOTALL)
    features = []
    if text_match:
        text_block = text_match.group(1)
        
        # Look for specific keywords
        if 'IPLC' in text_block.upper() or 'IEPL' in text_block.upper():
            line_type = "IPLC 专线" if 'IPLC' in text_block.upper() else "IEPL 专线"
            features.append(f"网络类型：官方宣称全节点接入 {line_type}")
            
        unlocks = []
        if 'Netflix' in text_block or '奈飞' in text_block: unlocks.append('Netflix')
        if 'Disney+' in text_block or '迪士尼' in text_block: unlocks.append('Disney+')
        if 'ChatGPT' in text_block: unlocks.append('ChatGPT')
        if 'TikTok' in text_block: unlocks.append('TikTok')
        
        if unlocks:
            features.append(f"流媒体解锁：官方标称支持解锁 {', '.join(unlocks)} 等")
        elif '原生 IP' in text_block:
            features.append("流媒体解锁：原生 IP，宣称支持主流流媒体与 AI")
            
        if '不限时' in text_block or '按量' in text_block:
            features.append("计费方式：提供不限时/按量计费套餐，流量不过期")
            
        if 'x1 倍率' in text_block or '1倍率' in text_block:
            features.append("流量政策：所有节点 x1 倍率")
            
        if '不限制设备' in text_block or '不限设备' in text_block or '无设备限制' in text_block:
            features.append("设备限制：不限制同时连接的设备数量")
            
    # Take up to 2 features
    features = features[:2]
    if not features:
        features = ["具体套餐特性请参考官方说明"]
        
    # Replace existing features block
    features_yaml = "features:\n"
    for f_str in features:
        features_yaml += f"  - \"{f_str}\"\n"
        
    content = re.sub(r'features:\n(?:  - ".*?"\n)*', features_yaml, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file_path} with: {features}")


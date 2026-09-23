import os, glob

brands_dir = 'src/content/brands'
md_files = glob.glob(os.path.join(brands_dir, '*.md'))

logo_map = {
    'edgenova': 'edgenova-logo.png',
    'firefly': 'firefly-logo.png',
    'sogo': 'sogoyun-logo.webp',
    'u1s1': 'logo (16).png', # guess, we'll see
    '一翻': 'yifanyun-logo.png',
    '二猫': 'ermaoyun-logo.png',
    '光年梯': 'logo (20).png', # guess
    '光速': 'guangsuyun-logo.png',
    '可信云': 'kexinyun-logo.png',
    '唯图': 'weituyun-logo.png',
    '微风': 'weifeng-logo.png',
    '快狸': 'kuaili-logo.png',
    '无忧': 'wuyou-logo.png',
    '星岛梦': 'xingdaomeng-logo.png',
    '暮光': 'muguang-logo.png',
    '极连': 'jilianyun-logo.png',
    '浪网': 'shanshuiyun-logo.png', # maybe?
    '灵动': 'lingdong-logo.png',
    '灵猫': 'lingmao-logo.png',
    '跨界': 'kaujieyun-logo.png',
    '速界': 'xsus-logo.png', # maybe xsus
    '闪跃': 'shanyue-logo.png',
    '隐形人': 'yingxingren-logo.png',
    '飞v': 'feiv-logo.png',
    '飞猫': 'feimaoyun-logo.png'
}

for file_path in md_files:
    basename = os.path.basename(file_path).replace('.md', '')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    logo_file = logo_map.get(basename)
    
    if logo_file and f'logo: "/images/logos/{logo_file}"' not in content:
        if 'logo: ' in content:
            # Replace existing logo
            import re
            content = re.sub(r'logo: ".*?"', f'logo: "/images/logos/{logo_file}"', content)
        else:
            # Insert before sort_order
            content = content.replace('\nsort_order:', f'\nlogo: "/images/logos/{logo_file}"\nsort_order:')
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Set logo for {basename} to {logo_file}")


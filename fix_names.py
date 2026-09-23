import os
import re

files_to_fix = ['firefly.md', '无忧.md', '灵猫.md', '飞v.md', '光年梯.md']
brands_dir = 'src/content/brands'

for fname in files_to_fix:
    fpath = os.path.join(brands_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace name: "xxx云" with name: "xxx"
    content = re.sub(r'name: "(.*?)云"', r'name: "\1"', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {fname}')

import os
import re

files_to_fix = ['快狸.md', '浪网.md', '灵动.md', '暮光.md', '速界.md']
brands_dir = 'src/content/brands'

for fname in files_to_fix:
    fpath = os.path.join(brands_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace name: "xxx云" with name: "xxx"
        content = re.sub(r'name: "(.*?)云"', r'name: "\1"', content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {fname}')
    else:
        print(f'File {fname} not found!')

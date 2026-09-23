import os
import re

files_to_fix = ['星岛梦.md', '隐形人.md', 'edgenova.md', 'u1s1.md', '可信云.md']
brands_dir = 'src/content/brands'

for fname in files_to_fix:
    fpath = os.path.join(brands_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace name: "xxx云" with name: "xxx"
        # For 可信云云 -> 可信云, it will strip one 云 if we use greedy, wait, let's be careful.
        # It's better to just manually set them or use a specific regex.
        if fname == '星岛梦.md':
            content = re.sub(r'name: ".*?"', 'name: "星岛梦"', content)
        elif fname == '隐形人.md':
            content = re.sub(r'name: ".*?"', 'name: "隐形人"', content)
        elif fname == 'edgenova.md':
            content = re.sub(r'name: ".*?"', 'name: "edgenova"', content)
        elif fname == 'u1s1.md':
            content = re.sub(r'name: ".*?"', 'name: "u1s1"', content)
        elif fname == '可信云.md':
            content = re.sub(r'name: ".*?"', 'name: "可信云"', content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {fname}')
    else:
        print(f'File {fname} not found!')

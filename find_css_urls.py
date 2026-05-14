import re

with open(r'css\eaf_login.css', encoding='utf-8', errors='ignore') as f:
    content = f.read()

urls = re.findall(r'url\(["\']?([^)"\']+)["\']?\)', content)
for u in urls:
    print(u)

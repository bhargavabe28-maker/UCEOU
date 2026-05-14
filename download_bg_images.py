import os
import requests
import urllib3

urllib3.disable_warnings()

base = "https://uceou.in/eaf/student/"
local_root = r"c:\Users\saibh\OneDrive\Desktop\UCEOU"

assets = [
    "images/login/bg5.jpg",
    "images/login/arrow_icon.png",
]

for asset in assets:
    url = base + asset
    local_path = os.path.join(local_root, asset.replace("/", os.sep))
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        print(f"Downloading {url}...")
        r = requests.get(url, verify=False, timeout=10)
        if r.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(r.content)
            print(f"  OK -> {local_path}")
        else:
            print(f"  FAIL {r.status_code}")
    except Exception as e:
        print(f"  ERROR: {e}")

# Also check mask-login.css for images
import re
for css_file in [r'css\main.css', r'loginmask\mask-login.css']:
    try:
        with open(os.path.join(local_root, css_file), encoding='utf-8', errors='ignore') as f:
            content = f.read()
        urls = re.findall(r'url\(["\']?([^)"\']+)["\']?\)', content)
        for u in urls:
            if u.startswith('http') or u.startswith('data:'):
                continue
            print(f"Found in {css_file}: {u}")
    except Exception as e:
        print(f"Error reading {css_file}: {e}")

print("\nDone!")

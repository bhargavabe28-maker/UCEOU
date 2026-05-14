import os
import requests
import urllib3

urllib3.disable_warnings()

base = "https://uceou.in/eaf/student/"
local_root = r"c:\Users\saibh\OneDrive\Desktop\UCEOU"

assets = [
    "loginmask/images/arow_icons.png",
    "images/login-button-bg-orange.png",
    "images/login-button-bg-orangeHover.png",
    "images/bg-image/kk.png",
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

print("\nAll done!")

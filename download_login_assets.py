import os
import requests
import urllib3

urllib3.disable_warnings()

# Login page CSS assets
base_login = "https://uceou.in/eaf/student/"
login_assets = [
    "css/bootstrap.min.css",
    "css/main.css",
    "css/eaf_login.css",
    "css/css.css",
    "loginmask/mask-login.css",
    "Scripts/jquery-1.5.1.min.js",
    "images/logo.jpg",
    "loginmask/images/bg.jpg",
    "loginmask/images/bg-login.jpg",
    "loginmask/images/login-bg.jpg",
]

local_root = r"c:\Users\saibh\OneDrive\Desktop\UCEOU"

for asset in login_assets:
    url = base_login + asset
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

# Also try the login bg images referenced in CSS
print("\nDone!")

import os
import requests
import urllib3

urllib3.disable_warnings()

base_url = "https://uceou.in/EAF/Student/"

assets = [
    "css/NewEafTemplate/bootstrap.min.css",
    "css/NewEafTemplate/custom.css",
    "css/NewEafTemplate/home.css",
    "Scripts/NewEafTemplateScript/jquery.min.js",
    "Scripts/NewEafTemplateScript/bootstrap.min.js",
    "Scripts/NewEafTemplateScript/custom.js",
    "images/logo.jpg",
    "loginmask/images/placementuser.png",
    "images/greenanim.gif"
]

for asset in assets:
    url = base_url + asset
    local_path = os.path.join(r"c:\Users\saibh\OneDrive\Desktop\UCEOU", asset.replace("/", os.sep))
    
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        print(f"Downloading {url}...")
        r = requests.get(url, verify=False, timeout=10)
        if r.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(r.content)
            print(f"Saved to {local_path}")
        else:
            print(f"Failed: {r.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

import requests

url = "https://uceou.in/eaf/student/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
try:
    response = requests.get(url, headers=headers, timeout=10, verify=False)
    print("Status:", response.status_code)
    print("Content len:", len(response.text))
except Exception as e:
    print("Error:", str(e))

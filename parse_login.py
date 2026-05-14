import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

url = "https://uceou.in/EAF/Student/index.php"
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
res = session.get(url, headers=headers, verify=False)
soup = BeautifulSoup(res.text, 'html.parser')

form = soup.find('form')
if form:
    print("Form action:", form.get('action'))
    inputs = form.find_all('input')
    for inp in inputs:
        print(inp.get('name'), inp.get('type'), inp.get('value'))
else:
    print("No form found")

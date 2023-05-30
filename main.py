import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")
    for script in soup.find_all("style", "script"):
        script.extract()
    rezult = ' '.join(soup.stripped_strings)
    req = len(rezult.split())
    print(req)
else:
    print(f"немає підклчення {response.status_code}")
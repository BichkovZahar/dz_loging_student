import requests
from bs4 import BeautifulSoup
response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    req = BeautifulSoup(response.content, "html.parser")
    classs = req.find_all("exampel_class")
    for i in classs:
        print(i)
else:
    print(f"Немає підключення {response.status_code}")
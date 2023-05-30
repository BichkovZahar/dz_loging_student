import requests
from bs4 import BeautifulSoup
response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    req = BeautifulSoup(response.content, "html.parser")
    table = req.find_all("table")
    for i in table:
        trs = i.find_all('tr')
        for tr in trs:
            finish = tr.find_all(['td', 'th'])
            for text_in_row in finish:
                print(text_in_row.get.text().strip)
else:
    print(f"Немає підкючення {response.status_code}")
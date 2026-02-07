from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import random


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
]

headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "www.google.com"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table")
table_head = table.find("tr")
head = [th.text.strip() for th in table_head.find_all("th")]

rows = table.find_all("tr")

data = []
for row in rows:
    cells = row.find_all("td")
    if not cells:
        continue
    
    body = [cell.text.strip() for cell in cells]

    while len(body) < len(head):
        body.append('')

    data.append(body)

df = pd.DataFrame(data, columns=head)
print(df.head())
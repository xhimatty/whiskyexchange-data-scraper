# import requests
# from bs4 import BeautifulSoup
# import random
# import lxml

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# # url = 'https://www.thomann.co.uk/guitar_sets.html'

# url = 'https://webscraper.io/test-sites/e-commerce/allinone/tablets'
# r = requests.get(url, headers=headers)

# attribute-style tag navigation/ chained tag navigation
# article = BeautifulSoup(r.text, 'lxml')
# tag = article.header.div.a.button.span
# print(tag.get_text())


# find() and find_all() Function 

# from bs4 import BeautifulSoup
# import requests
# import random

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
# r = requests.get(url, headers=headers)
# article = BeautifulSoup(r.text, 'lxml')
# prices = article.find_all('h4', class_='price float-end card-title pull-right')
# desc = article.find_all('p', class_='description card-text')
# print(prices[3])
# print(desc[3])


# BeatifulSoup find, find_all() with pandas

# from bs4 import BeautifulSoup
# import requests
# import random
# import lxml
# import pandas as pd

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
# r = requests.get(url, headers=headers)
# article = BeautifulSoup(r.text, 'lxml')

# product_wrapper = article.find_all('div', class_='product-wrapper card-body')

# products = []
# for product in product_wrapper:
#     name = product.find('a', class_="title").get_text(strip=True)
#     price = product.find('h4', class_="price float-end card-title pull-right").get_text(strip=True)
#     desc = product.find('p', class_="description card-text").get_text(strip=True)
#     star = product.find('p', attrs={"data-rating": True})
#     rating = int(star["data-rating"])
#     review = product.find('p', class_="review-count float-end").get_text(strip=True)
    
#     products.append([name, price, desc, rating, review])

# df = pd.DataFrame(products)
# print(df)


# Extract data from nested html tags

# from bs4 import BeautifulSoup
# import requests
# import random
# import lxml
# import pandas as pd

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
# r = requests.get(url, headers=headers)
# article = BeautifulSoup(r.text, 'lxml')

# boxes = article.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')

# article = article.find_all('div', class_="col-md-4 col-xl-4 col-lg-4")[3]
# data = []
# name = article.find('a').get_text(strip=True)
# desc = article.find('p').get_text(strip=True)
# print(desc)


# Extract data from Table

# from bs4 import BeautifulSoup
# import requests
# import random
# import lxml
# import pandas as pd

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# # url = 'https://www.premierleague.com/en/tables?competition=8&season=2025&round=L_1&matchweek=-1&ha=-1'

# url = 'https://ticker.finology.in/'
# r = requests.get(url, headers=headers)
# article = BeautifulSoup(r.text, 'lxml')
# table = article.find('table', class_="table table-sm table-hover screenertable")
# heads = table.find_all('th')
# titles = []
# for head in heads:
#     title = head.get_text(strip=True)
#     titles.append(title)

# df = pd.DataFrame(columns=titles)

# rows = table.find_all('tr')

# for row in rows[1:]:
#     cells = row.find_all('td')
#     data_rows = [cell.get_text(strip=True) for cell in cells]

#     length = len(df)
#     df.loc[length] = data_rows

# print(df)

# Extract data from Table

# from bs4 import BeautifulSoup
# import requests
# import random
# import lxml
# import pandas as pd

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# url = 'https://www.iplt20.com/auction/2022'

# r = requests.get(url, headers=headers)
# article = BeautifulSoup(r.text, 'lxml')
# table = article.find('table', class_="ih-td-tab w-100 auction-tbl")
# heads = table.find_all('th')
# titles = []
# for i in heads:
#     top = i.get_text(strip=True)
#     titles.append(top)

# df = pd.DataFrame(columns=titles)

# rows = table.find_all('tr')
# for i in rows[1:]:
#     tds = i.find_all('td')
#     row_data = [td.get_text(strip=True) for td in tds]
    
#     length = len(df)
#     df.loc[length] = row_data

# print(df)


#  How to scrape Multiiple pages on website

# from bs4 import BeautifulSoup
# import requests
# import random
# import lxml
# import pandas as pd

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Android 15; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
# ]

# headers = {
#     "User-Agent": random.choice(user_agents),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive"
# }

# # for page in range(1,5):
# url = f'https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text,'lxml')
# article = soup.find("div",class_="QSCKDh dLgFEE")

# product_names = []
# product_prices = []
# product_descs = []
# product_reviews = []

# product_name = article.find_all("div",class_="RG5Slk")
# for n in product_name:
#     name = n.get_text(strip=True)
#     product_names.append(name)

# product_price = article.find_all("div",class_="hZ3P6w DeU9vF")
# for p in product_price:
#     price = p.get_text(strip=True)
#     product_prices.append(price)

# product_desc = article.find_all("ul",class_="HwRTzP")
# for d in product_desc:
#     desc = d.get_text(strip=True)
#     product_descs.append(desc)

# product_review = article.find_all("div",class_="MKiFS6")
# for r in product_review:
#     review = r.get_text(strip=True)
#     product_reviews.append(review)

# print(len(product_names))
# print(len(product_prices))
# print(len(product_descs))
# print(len(product_reviews))


# df = pd.DataFrame({'Product Name':product_names, 'Product Price':product_prices, 'Product Description':product_descs, 'Product Review':product_reviews})
# print(df)

# div = soup.find("div", class_="LwDgZ8 eq0K9s tBcEQe")

# articles = div.find_all("div", class_="ZFwe0M row")

# products = []
# for article in articles:
#     product_name = article.find("div",class_="RG5Slk")
#     name = product_name.get_text(strip=True)

#     product_price = article.find_all("div",class_="hZ3P6w DeU9vF")
#     price = product_price.get_text(strip=True)

#     product_desc = article.find_all("ul",class_="HwRTzP")
#     desc = product_desc.get_text(strip=True)

#     product_review = article.find_all("div",class_="MKiFS6")
#     review = product_review.get_text(strip=True)

#     products.append({
#     "name": name,
#     "price": price,
#     "desc": desc,
#     "review": review
#     })

# print(products)

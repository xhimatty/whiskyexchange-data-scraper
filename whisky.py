import requests
import json
import pandas as pd

session = requests.Session()

cookies = {}

headers = {}

def get_pages(page_num):
    json_data = {
        'model': {
            'FilteringCriterias': {
                'SearchTextToFilterBy': 'whisky',
                'IsOnOffer': False,
                'IncludeOutOfStock': False,
                'Price': None,
            },
            'DisplaySettings': {
                'PageNumber': page_num,
                'PageSize': 24,
                'SortingOrder': 'rdesc'
            },
            'CurrentCustomerSettings': 'eyJDb29raWVzIjoie30ifQ==',
            'CurrentQueryString': 'q=whisky',
            'ApiToken': '1d00c600e800ea00f9009b00d30048008d007700aa005a001a00c000ec00470010006c00',
            'DataReturnedSettings': {
                'RemoveSelectedFiltersFromFiltersData': False,
                'ReturnArrayOfProductDataForGA4': True,
            },
            'OriginUrl': '/search?q=whisky',
        },
    }

    response = session.post(
        'https://www.thewhiskyexchange.com/api/product/productlistdata',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()
    return response.json()

def product_detail():
    all_products = []
    for i in range(1, 15):
        data = get_pages(i)

        products = data.get("ProductsForGA4", [])
        for p in products:
            name = p.get("item_name", "N/A")
            price = p.get("price", "N/A")
            brand = p.get("item_brand", "N/A")
            all_products.append({
                'Name': name,
                'Price': price,
                'Brand': brand
            })

    return all_products

df = pd.DataFrame(product_detail())
print(df)
df.to_csv('thewhiskyexchange_whisky_prices', index=False)

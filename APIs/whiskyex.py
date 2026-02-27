import requests
import json
import pandas as pd

session = requests.Session()

cookies = {
    'ASP.NET_SessionId_Live': 'hw4g02uj4ntb31bjlqnwtywn',
    '__tweuid': '6c2793304cf843c0bc668bcb811693f9',
    'startedat': '27/02/2026 08:42:37',
    'csrf_token': 'fad18e6d-cd95-44bf-8adb-799eaa2bccf6',
    'AwinChannelCookie': 'direct',
    '_gcl_au': '1.1.1195615330.1772181767',
    '_ga': 'GA1.1.2035299883.1772181769',
    'FPID': 'FPID2.2.8vvMyLtbQdI3Xuvq7a9mKWzoKjbHF1oZPhax9HhWU14%3D.1772181769',
    'FPLC': 'h8mHM%2FFq4RJRpCYem7EN78t3WAkFEx5x6uvSHV%2Bw4IRBsNyZmtxs3%2FOqLJNRl6h469eQQONEcChCkGNKXpjCHYsnIiWtS80u7wsiB5R1Gd1WGRXtkMqF7TjgjMqFVw%3D%3D',
    '_fbp': 'fb.1.1772181772189.975515483837405261',
    'lantern': 'c2934b3b-b1ea-4d99-800e-6f41dec860e0',
    'ServerAwinChannelCookie': 'direct',
    '_gtmeec': 'e30%3D',
    '_pin_unauth': 'dWlkPU1EVmpOREUyWVdVdE1qRXpNUzAwWlRjM0xUZ3dOall0WldFd1lUaGpNbUZpTm1ZeQ',
    '_cs_c': '0',
    '_cs_s_ctx': '%7B%22firstViewTime%22%3A1772181776974%2C%22firstViewUrl%22%3A%22https%3A%2F%2Fwww.thewhiskyexchange.com%2F%22%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D',
    'rbuid': 'rbos-94f390f3-e347-430b-b4fc-4f6e7eb9b226',
    '__zlcmid': '1WJoK1a2HLIS5mF',
    'cf_clearance': '0lmwCr5hbkTzOIvODV9raTOFIcc9_lVvoPQl0cCOe2o-1772181877-1.2.1.1-eocBlqfDAj6.Gzj1ukBDXUmcVFu6Gx.Ko8bn7.aVv8t.dlYEgkWyJ1rlbl1Jdub7uei5lLBWW27ifqYghHBpAvCGPKetQtWRu6xUJF2Oo5o2u.0bXdm9dw3nYlUB.ykfe28X8pJl.QxH_4szzZI3LIfQ9dsF3l_TM._3ilC0Aqro3hzT3fK7.ZwMYPHRgb_dGOPgveTTKXaLF.n4ce0x7IkB092Ej0Kcs9s9rMTZCU8',
    '__cf_bm': 'XW1Kj9t8nnChuk63c3m7CtEQcnylPxR848A.KuXaoPQ-1772181877.439153-1.0.1.1-n6pYjyn44Qv.vh_Rj.YRt0lqSxCx4fF6o17m4E4_foWpM_HJ4vbUaaLlyX9CQDh7sy5X.at_ZHRGvgFdedpGEjEhWvdjsQ7HDG2ZSvWLWuwR4mNSSsjMJ7xsMQryXBH0',
    'ometria': '2_cid%3D3P2gscZ2wI04MVsv%26nses%3D1%26osts%3D1772181772%26sid%3Df15e3b148AeHbz9DAcQMJ%26npv%3D2%26tids%3D%26ecamp%3D%26src%3Dgoogle.com%257CNOT_SUPPLIED%257Csearch%257C%257CGoogle%257C%257C20511%26osrc%3Dgoogle.com%257CNOT_SUPPLIED%257Csearch%257C%257CGoogle%257C%257C20511%26slt%3D1772182039%26shopify_bskt_url%3Dhttps%253A%252F%252Fwww.thewhiskyexchange.com%252F',
    '_uetsid': '4e86f5e013b811f1840f45b0a0f3976f',
    '_uetvid': '4e87531013b811f183a6bf66ba18f099',
    '_cs_id': 'a9858cf5-9400-a17b-ef86-29baec394011.1772181776.1.1772182040.1772181776.1750258502.1806345776972.1.x',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.thewhiskyexchange.com%252F',
    'ABTasty': 'uid=pdd8p0kw4wv1rxz7&fst=1772181772689&pst=-1&cst=1772181772689&ns=1&pvt=7&pvis=7&th=',
    '_ga_53RV91M60Z': 'GS2.1.s1772181768$o1$g1$t1772182040$j53$l0$h1447372467',
    '_cs_s': '7.5.U.9.1772184026454',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apitoken': '"1d00c600e800ea00f9009b00d30048008d007700aa005a001a00c000ec00470010006c00"',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.thewhiskyexchange.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.thewhiskyexchange.com/search?q=whisky',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'ASP.NET_SessionId_Live=hw4g02uj4ntb31bjlqnwtywn; __tweuid=6c2793304cf843c0bc668bcb811693f9; startedat=27/02/2026 08:42:37; csrf_token=fad18e6d-cd95-44bf-8adb-799eaa2bccf6; AwinChannelCookie=direct; _gcl_au=1.1.1195615330.1772181767; _ga=GA1.1.2035299883.1772181769; FPID=FPID2.2.8vvMyLtbQdI3Xuvq7a9mKWzoKjbHF1oZPhax9HhWU14%3D.1772181769; FPLC=h8mHM%2FFq4RJRpCYem7EN78t3WAkFEx5x6uvSHV%2Bw4IRBsNyZmtxs3%2FOqLJNRl6h469eQQONEcChCkGNKXpjCHYsnIiWtS80u7wsiB5R1Gd1WGRXtkMqF7TjgjMqFVw%3D%3D; _fbp=fb.1.1772181772189.975515483837405261; lantern=c2934b3b-b1ea-4d99-800e-6f41dec860e0; ServerAwinChannelCookie=direct; _gtmeec=e30%3D; _pin_unauth=dWlkPU1EVmpOREUyWVdVdE1qRXpNUzAwWlRjM0xUZ3dOall0WldFd1lUaGpNbUZpTm1ZeQ; _cs_c=0; _cs_s_ctx=%7B%22firstViewTime%22%3A1772181776974%2C%22firstViewUrl%22%3A%22https%3A%2F%2Fwww.thewhiskyexchange.com%2F%22%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; rbuid=rbos-94f390f3-e347-430b-b4fc-4f6e7eb9b226; __zlcmid=1WJoK1a2HLIS5mF; cf_clearance=0lmwCr5hbkTzOIvODV9raTOFIcc9_lVvoPQl0cCOe2o-1772181877-1.2.1.1-eocBlqfDAj6.Gzj1ukBDXUmcVFu6Gx.Ko8bn7.aVv8t.dlYEgkWyJ1rlbl1Jdub7uei5lLBWW27ifqYghHBpAvCGPKetQtWRu6xUJF2Oo5o2u.0bXdm9dw3nYlUB.ykfe28X8pJl.QxH_4szzZI3LIfQ9dsF3l_TM._3ilC0Aqro3hzT3fK7.ZwMYPHRgb_dGOPgveTTKXaLF.n4ce0x7IkB092Ej0Kcs9s9rMTZCU8; __cf_bm=XW1Kj9t8nnChuk63c3m7CtEQcnylPxR848A.KuXaoPQ-1772181877.439153-1.0.1.1-n6pYjyn44Qv.vh_Rj.YRt0lqSxCx4fF6o17m4E4_foWpM_HJ4vbUaaLlyX9CQDh7sy5X.at_ZHRGvgFdedpGEjEhWvdjsQ7HDG2ZSvWLWuwR4mNSSsjMJ7xsMQryXBH0; ometria=2_cid%3D3P2gscZ2wI04MVsv%26nses%3D1%26osts%3D1772181772%26sid%3Df15e3b148AeHbz9DAcQMJ%26npv%3D2%26tids%3D%26ecamp%3D%26src%3Dgoogle.com%257CNOT_SUPPLIED%257Csearch%257C%257CGoogle%257C%257C20511%26osrc%3Dgoogle.com%257CNOT_SUPPLIED%257Csearch%257C%257CGoogle%257C%257C20511%26slt%3D1772182039%26shopify_bskt_url%3Dhttps%253A%252F%252Fwww.thewhiskyexchange.com%252F; _uetsid=4e86f5e013b811f1840f45b0a0f3976f; _uetvid=4e87531013b811f183a6bf66ba18f099; _cs_id=a9858cf5-9400-a17b-ef86-29baec394011.1772181776.1.1772182040.1772181776.1750258502.1806345776972.1.x; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.thewhiskyexchange.com%252F; ABTasty=uid=pdd8p0kw4wv1rxz7&fst=1772181772689&pst=-1&cst=1772181772689&ns=1&pvt=7&pvis=7&th=; _ga_53RV91M60Z=GS2.1.s1772181768$o1$g1$t1772182040$j53$l0$h1447372467; _cs_s=7.5.U.9.1772184026454',
}

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
# df.to_csv('thewhiskyexchange_whisky_prices', index=False)
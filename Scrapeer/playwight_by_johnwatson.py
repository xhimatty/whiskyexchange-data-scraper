# from playwright.sync_api import sync_playwright

# def run(p):
#     with sync_playwright() as p:
#         url = "https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F"
#         browser = p.chromium.launch(headless=False, slow_mo=500)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto(url,wait_until="domcontentloaded")

#         context.close()
#         browser.close()

# run()


# Did this fucntion shit below myself!

# def main(url, headless, slow_mo):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto(url,wait_until="domcontentloaded")
#         page.get_by_label("Email:").click()
#         page.get_by_label("Password:").click()
#         page.get_by_role("button",name="Log in").click()


#         context.close()
#         browser.close()

# main(
#     url ="https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F",
#     headless=False,
#     slow_mo=500
#     )




# Open cart demo

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    url = "https://demo3x.opencartreports.com/admin/"
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")
    page.fill("input#input-username", "demo")
    page.fill("input#input-password", "demo")
    page.click("button[type=submit]")

    page.wait_for_selector("div.tile-body")    
    total_orders = page.locator("h2.pull-right").first.text_content()
    total_sales = page.locator("h2.pull-right").nth(1).text_content()
    total_customers = page.locator("h2.pull-right").nth(2).text_content()
    people_online = page.locator("h2.pull-right").nth(3).text_content()

    data = []
    data.append({
        "Total Orders":total_orders,
        "Total Sales":total_sales,
        "Total Customers":total_customers,
        "People Online":people_online
    })

    print(data)

    browser.close()

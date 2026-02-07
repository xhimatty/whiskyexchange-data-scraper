from playwright.sync_api import sync_playwright

def main(url, headless, slow_mo):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        page = browser.new_page()
        page.goto(url,wait_until="domcontentloaded")
        
        browser.close() 

main(
    url ="https://www.google.com",
    headless=False,
    slow_mo=500
    )
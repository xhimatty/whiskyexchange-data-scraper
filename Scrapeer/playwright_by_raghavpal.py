from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        url = "https://www.google.com/"
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(url,wait_until="domcontentloaded")
        print(f"Page title: {page.title()}")

        browser.close()

if __name__ == "__main__":
    main()
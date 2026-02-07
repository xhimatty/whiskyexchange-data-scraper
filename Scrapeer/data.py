from playwright.sync_api import sync_playwright
url = "https://arxiv.org/search/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                                            "Chrome/118.0.0.0 Safari/537.36")
    page = context.new_page()
    page.goto(url, timeout=50000)

    page.get_by_placeholder("Search term...").fill("neural network")
    page.get_by_role("button", name="Search").nth(1).click()
    page.wait_for_selector("a[href*='pdf']")
    links = page.locator("a[href*='pdf']").all()

    all_pdf = []

    for link in links:
        pdfs = link.get_attribute("href")
        if pdfs:
            print(pdfs)
            all_pdf.append(pdfs)
    
    print(all_pdf)

    browser.close()



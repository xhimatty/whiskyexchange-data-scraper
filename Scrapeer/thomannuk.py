from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    base_url = "https://www.thomann.co.uk/st_models.html"
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto(base_url, wait_until="domcontentloaded")

    all_products = []

    try:
        consent_button = page.locator('.spicy-consent-wrapper button.fx-button--primary, .js-accept-all').first
        consent_button.click(timeout=5000)
        print("Consent banner dismissed.")
    except Exception:
        print("Consent button not found. Nuking overlay with CSS...")
        page.add_style_tag(content="""
            .spicy-consent-wrapper, .js-spicy-ask, .theme-fx.spicy-consent-wrapper { 
                display: none !important; 
            }
            body { overflow: auto !important; }
        """)

    pagination = page.locator('button.fx-pagination__pages-button')
    pagination.first.wait_for(state='attached')
    total_pages = min(pagination.count(), 2)

    for i in range(total_pages):
        page.evaluate("""() => {
            const selectors = ['.spicy-consent-wrapper', '.js-spicy-ask', '.theme-fx.spicy-consent-wrapper'];
            selectors.forEach(s => document.querySelectorAll(s).forEach(el => el.remove()));
            document.body.style.overflow = 'auto';
        }""")

        page.locator('button.fx-pagination__pages-button').nth(i).click(force=True,timeout=30000, no_wait_after=True)

        page.wait_for_selector("div.product", timeout=12000)
        time.sleep(1)
        products = page.locator("div.product").all()

        for product in products:
            title_ = product.locator('div.product__title').first
            title = title_.inner_text() if title_.count() > 0 else 'N/A'
            price_ = product.locator('[data-track-id="priceContainer"]').first
            price = price_.inner_text() if price_.count() > 0 else None
            desc_ = product.locator('div.product__description').first
            desc = desc_.inner_text() if desc_.count() > 0 else 'N/A'
            availability_ = product.locator('div.product__availability').first
            availability = availability_.inner_text() if availability_.count() > 0 else 'N/A'
            review_ = product.locator('div.product__rating-stars').first
            review = review_.inner_text() if review_.count() > 0 else 'N/A'

            all_products.append({
                'Title':title,
                'Price':price,
                'Description':desc,
                'Availability':availability,
                'Review':review
            })
        
        print(f"Page {i+1} scraped. Total products: {len(all_products)}")

    browser.close()

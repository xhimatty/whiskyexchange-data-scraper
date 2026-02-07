from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://books.toscrape.com/", wait_until='domcontentloaded')

    while True:

        page.wait_for_selector('article')

        articles = page.locator('article').all()

        for article in articles:
            image = article.locator('img')
            title = image.get_attribute('alt')
            price = article.locator('div.product_price p.price_color').first.inner_text()
            availability = article.locator('div.product_price p.availability').first.inner_text()
            rating_classes = article.locator("p.star-rating").first.get_attribute("class")
            rating_word = rating_classes.split()[-1].lower()
            mapping = {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5
            }
            rating = mapping[rating_word]

            print(f"Title: {title} Price: {price} Availability: {availability} Rating: {rating}")

        next_page = page.get_by_role('link', name='next').first
        if not next_page.is_visible():
            break

        next_page.click()
        page.wait_for_selector('article')

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    the_username = page.wait_for_selector('//input[@name="username"]')
    the_username.type('Admin')
    the_password = page.wait_for_selector('//input[@placeholder="Password"]')
    the_password.type('admin123')
    the_login = page.wait_for_selector('//button[@type="submit"]')
    the_login.click()
    page.wait_for_timeout(3000)

    print("Login successful...")

    browser.close()
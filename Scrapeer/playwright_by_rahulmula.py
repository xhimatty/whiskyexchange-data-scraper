# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     # launch browser
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     # create a new page
#     page = browser.new_page()
#     # visit website
#     page.goto("https://playwright.dev/python")


#     browser.close()


#  How to use get_by_role() to select link element (How to click a link)

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     # launch browser
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     # create a new page
#     page = browser.new_page()
#     # visit website
#     page.goto("https://playwright.dev/python")

#     # locate a link element with "Docs" text
#     docs_button = page.get_by_role('link', name="Docs")
#     docs_button.click()

#     browser.close()


# How to get the url after clicking the link

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     # launch browser
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     # create a new page
#     page = browser.new_page()
#     # visit website
#     page.goto("https://playwright.dev/python")

#     # locate a link element with "Docs" text
#     docs_button = page.get_by_role('link', name="Docs")
#     docs_button.click()

#     # Get the url 
#     print(f"Docs: {page.url}")

#     browser.close()


# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     btn = page.get_by_role('button',name='Default button')
#     btn.highlight()
#     btn.click()
    
#     browser.close()


# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     heading = page.get_by_role("heading",name="Heading 2")
#     heading.highlight()
    
#     browser.close()

# get_by_role() for Clicking radio buton
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     radio = page.get_by_role("radio",name="Option one is this and that—be sure to include why it's great")
#     radio.highlight()
    
#     browser.close()

# get_by_role() for checking box
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     check = page.get_by_role("checkbox",name="Default checkbox")
#     check.highlight()
#     check.check()
    
#     browser.close()

# Using get_by_label() for Email and password highlighting
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     email_input = page.get_by_label("Email address")
#     email_input.highlight()
#     password_input =  page.get_by_label("Password")
#     password_input.highlight()
    
#     browser.close()


# Using get_by_placeholder() for Email and password highlighting if the are no labels
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     enter_email = page.get_by_placeholder("Enter email")
#     enter_email.highlight()

#     page.get_by_placeholder("Password").highlight()
    
#     browser.close()


# Locator text helps locate text element based on their text
# get_by_text()
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     texts = page.get_by_text("with faded secondary text")
#     texts.highlight()
#     another_text = page.get_by_text("fine print")
#     another_text.highlight()
    
#     browser.close()


# Alt text locator for images

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://unsplash.com"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     alt_text = page.get_by_alt_text("Woman in black dress standing on fence under blue sky")
#     alt_text.highlight()
#     alt_text.click()
    
#     browser.close()


# get_by_title()
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url)

#     titles = page.get_by_title("Source Title")
#     titles.highlight()
    
#     browser.close()

# CSS Selectors
# However, you must note that playwright does not recommend as the DOM can often change
# Playwright recommends locator instead, such as role locators

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     selectors = page.locator("css=h1")
#     selectors.highlight()
#     page.locator("footer").highlight()
#     button_highlight = page.locator("button.btn-outline-success")
#     button_highlight.highlight()
#     button_click = page.locator("button.btn-outline-success")
#     button_click.click()
#     dropdown = page.locator("button#btnGroupDrop1")
#     dropdown.click()

#     print(dropdown)
#     if dropdown:
#         print("Drop down clicked successfully!")
    
#     browser.close()

# Back to using locator. Selecting input fields
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("input[readonly]").highlight()
#     page.locator("input[value='correct value']").highlight()
    
#     browser.close()


# locator
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("nav.bg-dark a.nav-link.active").highlight()
    
#     browser.close()


# xpaths: This is tougher but provides more functionality than selectors
# xpath is used to select elements explicitly
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("xpath=//h1").highlight()
#     page.locator("xpath=//h1[@id='navbars']").highlight() #id
    
#     browser.close()


# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("//h1[@id='navbars']").highlight() #id
#     page.locator("//input[@readonly]").highlight() # we can use the xpath with including xpath=
#     page.locator("//input[@value='wrong value']").highlight()

#     browser.close()


# xpath functions

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("//h1[text()='Heading 1']").highlight() #texts
#     page.locator("//h1[contains(text(),'Head')]").highlight() # specific texts
#     page.locator("//button[contains(@class, 'btn-outline-primary')]").highlight() # class
#     page.locator("//input[contains(@value, 'correct')]").highlight()

#     browser.close()


# Other locators
# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.get_by_role("button", name="Primary").locator("nth=1").highlight()
#     # We can also do this
#     page.locator("button").locator("nth=18").highlight()
#     page.locator("button").locator("nth=22").highlight()
#     page.locator("button").locator("nth=30").highlight()
#     page.locator("button").locator("nth=25").highlight()

#     page.locator("id=btnGroupDrop1").highlight()

#     browser.close()


# Using locators without using css selectors or xpath

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     page.locator("id=btnGroupDrop1").highlight() # using locator directly

#     browser.close()


# Mouse action

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     button = page.locator("button", name="Block button").first
#     button.click()
#     button.dblclick() # double clicking
#     button.dblclick(delay=500) # applying delay

#     browser.close()


# Input Field Action

# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     email_input = page.get_by_placeholder("Enter email")
#     email_input.fill("matty@gmail.com") # to fill in
#     email_input.clear() # to clear the input
#     email_input.type("matty@gmail.com",delay=200) # the type method with delay fills more like human 

#     browser.close()


# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     url = "https://bootswatch.com/default"
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto(url, wait_until="domcontentloaded")

#     radio_two = page.get_by_label("Option two can be something else and selecting it will deselect option one")
#     radio_two.check()
#     radio_one = page.get_by_label("Option one is this and that—be sure to include why it's great")
#     radio_one.check()


#     browser.close()


# Select element

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    url = "https://bootswatch.com/default"
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")

    select = page.get_by_label("Example select")
    select.select_option("4")
    select.select_option("2")
    select.select_option("3")

    # To select multiple options we do this
    mult_select = page.get_by_label("Example multiple select")
    mult_select.select_option(["2","4"])
    
    browser.close()
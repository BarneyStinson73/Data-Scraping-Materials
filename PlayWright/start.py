from playwright.sync_api import sync_playwright, Playwright, TimeoutError

def run(playwright: Playwright):
    st_url = "https://www.bhphotovideo.com/deals-promotions-coupons/"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(st_url)
    for link in page.locator('a[data-selenium="miniProductPageDetailsGridViewNameLink" ]').all():
        # opening each link in a new tab
        p=browser.new_page(base_url="https://www.bhphotovideo.com/")
        url= link.get_attribute('href')
        if url is not None:
            p.goto(url)
            try:
                # Wait for the script tag to be available before extracting its content
                p.wait_for_selector("script[type='application/ld+json']", timeout=5000)
                product_info = p.locator("script[type='application/ld+json']").text_content()
                print(product_info)  # this will print the product info in json format
            except TimeoutError:
                print(f"Could not find the product info script tag for {url}")
            finally:
                p.close()
         
        
with sync_playwright() as p:
    run(p)

from playwright.sync_api import sync_playwright, Playwright, TimeoutError

def run(playwright: Playwright):
    st_url = "https://www.bhphotovideo.com/deals-promotions-coupons/"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(st_url)
    for link in page.locator('a[data-selenium="miniProductPageDetailsGridViewNameLink" ]').all():
        # print(link.text_content())
        p=browser.new_page(base_url="https://www.bhphotovideo.com")
        url= link.get_attribute('href')
        if url is not None:
            p.goto(url)
            p.close()
with sync_playwright() as p:
    run(p)

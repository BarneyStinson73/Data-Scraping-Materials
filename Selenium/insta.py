# because of instagram's strict security measures, it's very hard to scrape data from it. I worked with selenium and tried to scrape data from instagram. But it's not working. I tried to use selenium-stealth to bypass the security measures but it's not working. I tried to use edge driver and chrome driver but it's not working. 
# keeping this file for future reference.


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint
import json
from selenium_stealth import stealth

usernames=["jlo","therock","kyliejenner","kimkardashian","selenagomez","arianagrande","beyonce","justinbieber","taylorswift","kendalljenner"]

proxy = "server:port"
output= {}

def main():
    for username in usernames:
        scrape(username)
   
def prepare_browser():
    # first tried with edge,but stealth doesn't work in it
    # edge_options = webdriver.EdgeOptions()
    # edge_options.add_argument('--proxy-server=%s' % proxy)
    # edge_options.add_argument("start-maximized")
    # edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # edge_options.add_experimental_option('useAutomationExtension', False)
    # edge_options.add_argument("--disable-blink-features=AutomationControlled")
    # PATH = "/home/asif/Downloads/edgedriver_linux64/msedgedriver"
    # service = Service(executable_path=PATH)
    # driver = webdriver.Edge(service=service)
    
    # now trying using chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options)
    stealth(driver,
            user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="linux",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=False,
            run_on_insecure_origins= False,
            )
    return driver

def scrape(username):
    url= f"https://www.instagram.com/{username}/?__a=1&_d=dis"  # Instagram's __a=1 endpoint has been deprecated for public use. 
    driver=prepare_browser()
    driver.get(url)
    print("Scraping: {driver.current_url}")
    try:
        # Wait until the body of the page is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Retrieve page source or any required data from page content
        page_source = driver.page_source

        # Now, parse the HTML content to extract information
        if "Sorry, this page isn't available" in page_source:
            print(f"{username} not found")
            driver.quit()
            return
        else:
            # You can use BeautifulSoup or regex to extract data from page_source
            output[username] = page_source  # Save raw page source for now

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()       
# def parse_data(username,data):
        

if __name__=='__main__':
        main()
        pprint(output)
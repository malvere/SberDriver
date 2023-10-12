#%%
from selenium import webdriver
from selenium.webdriver.common.by import By

from .firefox import Options, Service, WebDriver
from .plat import whoami

# Define the URL and user agent
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)"

class PrigozhinSelenium:
    def __init__(self) -> None:
        self.url = "https://megamarket.ru/catalog/?q=моторное%20масло%205л"
        self.options = Options()
        self.options.add_argument(f"user-agent={user_agent}")
        self.options.add_argument(f"-headless")
        # self.options.binary_location = whoami()
        self.service = Service(executable_path=whoami())
        self.driver: WebDriver

    def go_sber(self):
        with webdriver.Firefox(options=self.options, service=self.service) as driver:
            self.parse(driver)

    def raw_go(self):
        self.driver = webdriver.Firefox(options=self.options, service=self.service)
        self.driver.get(self.url)

    def parse(self):
        driver = self.driver
        driver.get(self.url)
        print(driver.title)
        mobs = driver.find_elements(By.CSS_SELECTOR, '.item-block')
        if len(mobs) == 0:
            print("Found 0 items, refreshing")
            driver.implicitly_wait(10)
            driver.refresh()
            driver.implicitly_wait(20)
            mobs = driver.find_elements(By.CSS_SELECTOR, '.item-block')
        print(f"Found {len(mobs)} items.")
        self.save_html(driver.page_source)

    def captcha(self):
        cpt = Captcha(self.driver)
        return cpt
    
    def save_html(self, page):
        with open('page.html', 'w') as f:
            f.write(page)
            print("Page saved!")

    def grace_shutdown(self):
        self.driver.close()
        self.driver.quit()

class Captcha():
    def __init__(self, driver: WebDriver) -> None:
        self.captcha = driver.find_element(By.ID, "captcha_image")
        self.field = driver.find_element(By.NAME, "captcha")
        self.submit_btn = driver.find_element(By.NAME, "submit")
        print("Captcha found!")
    
    def screenshot(self, name = "test.png"):
        self.captcha.screenshot(name)
        print(f"Captcha saved as {name}")
    
    def send_keys_to_captcha(self, keys: str):
        self.field.send_keys(keys)
    
    def submit(self):
        self.submit_btn.click()
        print("Captcha submitted")



# %%

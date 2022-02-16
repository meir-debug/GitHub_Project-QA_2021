from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Helpers as Hp
import unittest
import time


class LogInWinChrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '95.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        Key = Hp.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=Key,
            desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        self.driver.maximize_window()
        # workflow over "elem" and "wait" variable to better code length
        elem = driver.find_element
        wait = WebDriverWait(driver, 10)

        driver.get(Hp.url_Test)

        # API testing from Selenium
        print("AliceBlue Florist Url has", requests.get(Hp.url_Test).status_code,
              "as status Code")
        code = requests.get(Hp.url_Test).status_code

        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if Hp.Title not in driver.title:
            raise Exception("AliceBlue Florist - page has wrong Title!")
        Hp.delay()
        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ALICEBLUE FLORIST")))
            print("First Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)

        # Checking page title
        self.assertIn(Hp.Title, driver.title)
        print("Page has", driver.title + " as Page title")
        elem(By.XPATH, "//*[@class='_1UDJF']").click()
        Hp.delay()
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@data-testid='signUp.headline']")))
            print("Second Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        Hp.delay()
        elem(By.XPATH, "//span[@class='_1Qjd7'][contains(.,'Sign up with email')]").click()
        Hp.delay()
        elem(By.XPATH, Hp.input_em).clear()
        elem(By.XPATH, Hp.input_em).send_keys(Hp.fake.email())  #
        elem(By.XPATH, Hp.input_pas).clear()
        elem(By.XPATH, Hp.input_pas).send_keys(Hp.fake.ean(length=8) + Keys.ENTER)
        time.sleep(10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Hp.input_em)))
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        except TE:
            print("Everything is fine!!!")

    def tearDown(self):
        self.driver.quit()


class LogInWinFf(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '74.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Frefox Test',
            'acceptSslCerts': True
        }
        Key = Hp.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=Key,
            desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        self.driver.maximize_window()
        # workflow over "elem" and "wait" variable to better code length
        elem = driver.find_element
        wait = WebDriverWait(driver, 10)

        driver.get(Hp.url_Test)

        # API testing from Selenium
        print("AliceBlue Florist Url has", requests.get(Hp.url_Test).status_code,
              "as status Code")
        code = requests.get(Hp.url_Test).status_code

        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if Hp.Title not in driver.title:
            raise Exception("AliceBlue Florist - page has wrong Title!")
        Hp.delay()
        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ALICEBLUE FLORIST")))
            print("First Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)

        # Checking page title
        self.assertIn(Hp.Title, driver.title)
        print("Page has", driver.title + " as Page title")
        elem(By.XPATH, "//*[@class='_1UDJF']").click()
        Hp.delay()
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@data-testid='signUp.headline']")))
            print("Second Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        Hp.delay()
        elem(By.XPATH, "//span[@class='_1Qjd7'][contains(.,'Sign up with email')]").click()
        Hp.delay()
        elem(By.XPATH, Hp.input_em).clear()
        elem(By.XPATH, Hp.input_em).send_keys(Hp.fake.email())  #
        elem(By.XPATH, Hp.input_pas).clear()
        elem(By.XPATH, Hp.input_pas).send_keys(Hp.fake.ean(length=8) + Keys.ENTER)
        time.sleep(10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Hp.input_em)))
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        except TE:
            print("Everything is fine!!!")

    def tearDown(self):
        self.driver.quit()


class LogInWinEdge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Edge',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        Key = Hp.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=Key,
            desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        self.driver.maximize_window()
        # workflow over "elem" and "wait" variable to better code length
        elem = driver.find_element
        wait = WebDriverWait(driver, 10)

        driver.get(Hp.url_Test)

        # API testing from Selenium
        print("AliceBlue Florist Url has", requests.get(Hp.url_Test).status_code,
              "as status Code")
        code = requests.get(Hp.url_Test).status_code

        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if Hp.Title not in driver.title:
            raise Exception("AliceBlue Florist - page has wrong Title!")
        Hp.delay()
        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ALICEBLUE FLORIST")))
            print("First Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)

        # Checking page title
        self.assertIn(Hp.Title, driver.title)
        print("Page has", driver.title + " as Page title")
        elem(By.XPATH, "//*[@class='_1UDJF']").click()
        Hp.delay()
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@data-testid='signUp.headline']")))
            print("Second Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        Hp.delay()
        elem(By.XPATH, "//span[@class='_1Qjd7'][contains(.,'Sign up with email')]").click()
        Hp.delay()
        elem(By.XPATH, Hp.input_em).clear()
        elem(By.XPATH, Hp.input_em).send_keys(Hp.fake.email())  #
        elem(By.XPATH, Hp.input_pas).clear()
        elem(By.XPATH, Hp.input_pas).send_keys(Hp.fake.ean(length=8) + Keys.ENTER)
        time.sleep(10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Hp.input_em)))
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        except TE:
            print("Everything is fine!!!")

    def tearDown(self):
        self.driver.quit()


class LogInBigSurChrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        Key = Hp.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=Key,
            desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        self.driver.maximize_window()
        # workflow over "elem" and "wait" variable to better code length
        elem = driver.find_element
        wait = WebDriverWait(driver, 10)

        driver.get(Hp.url_Test)

        # API testing from Selenium
        print("AliceBlue Florist Url has", requests.get(Hp.url_Test).status_code,
              "as status Code")
        code = requests.get(Hp.url_Test).status_code

        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if Hp.Title not in driver.title:
            raise Exception("AliceBlue Florist - page has wrong Title!")
        Hp.delay()
        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ALICEBLUE FLORIST")))
            print("First Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)

        # Checking page title
        self.assertIn(Hp.Title, driver.title)
        print("Page has", driver.title + " as Page title")
        elem(By.XPATH, "//*[@class='_1UDJF']").click()
        Hp.delay()
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@data-testid='signUp.headline']")))
            print("Second Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        Hp.delay()
        elem(By.XPATH, "//span[@class='_1Qjd7'][contains(.,'Sign up with email')]").click()
        Hp.delay()
        elem(By.XPATH, Hp.input_em).clear()
        elem(By.XPATH, Hp.input_em).send_keys(Hp.fake.email())  #
        elem(By.XPATH, Hp.input_pas).clear()
        elem(By.XPATH, Hp.input_pas).send_keys(Hp.fake.ean(length=8) + Keys.ENTER)
        time.sleep(10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Hp.input_em)))
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        except TE:
            print("Everything is fine!!!")

    def tearDown(self):
        self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# if __name__ == '__main__':
#     unittest.main(AllureReports)

# py.test --alluredir=./AllureReports ./unittest4.py

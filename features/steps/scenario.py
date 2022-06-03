import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scenario:

    def __init__(self, context):
        self.context = context

    def open_browser(self, browser):
        match browser:
            case 'Chrome':
                self.context.driver = webdriver.Chrome()
                self.context.driver.maximize_window()

            case 'Edge':
                self.context.driver = webdriver.ChromiumEdge()
                self.context.driver.maximize_window()

            case 'Firefox':
                self.context.driver = webdriver.Firefox()
                self.context.driver.maximize_window()

    def got_to_url(self, url):
        self.context.driver.get(url)

    def input_using_name(self, name, text):
        self.context.driver.find_element_by_name(name).send_keys(text)
        time.sleep(1)

    def input_using_id(self, id, text):
        self.context.driver.find_element_by_id(id).send_keys(text)
        time.sleep(1)

    def click_using_css(self, css):
        self.context.driver.find_element_by_css_selector(css).click()

    def click_using_name(self, name):
        self.context.driver.find_element_by_name(name).click()

    def click_using_id(self, id):
        self.context.driver.find_element_by_id(id).click()

    def wait_for_id_to_be_present(self, element):
        WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.ID, element)))

    def wait_for_name_to_be_present(self, element):
        WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.NAME, element)))

    def wait_for_css_to_be_present(self, element):
        WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    def take_screenshot(self, ssName):
        time.sleep(1)
        self.context.driver.get_screenshot_as_file('Screenshots\\'+ssName + '.png')
        #myScreenshot = pyautogui.screenshot()
        #myScreenshot.save(r'frezzing_test_selenium\Screenshots\Use Case 1\\'+ssName+'.png')


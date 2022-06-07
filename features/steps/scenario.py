import time
from selenium import webdriver
from selenium.common import TimeoutException, NoAlertPresentException, NoSuchElementException
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

    def close_browser(self):
        self.context.driver.close()

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
        try:
            WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.ID, element)))
        except TimeoutException as te:
            print('id = ' + element + ' cannot be found')
            raise te

    def id_is_present(self, element):
        if self.context.driver.find_element(By.ID, element).is_displayed():
            return True
        else:
            return False

    def wait_for_name_to_be_present(self, element):
        try:
            WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.NAME, element)))
        except TimeoutException as te:
            print('name = ' + element + ' cannot be found')
            raise te

    def name_is_present(self, element):
        if self.context.driver.find_element(By.NAME, element).is_displayed():
            return True
        else:
            return False

    def wait_for_css_to_be_present(self, element):
        try:
            WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        except TimeoutException as te:
            print('css selector = ' + element + ' cannot be found')
            raise te

    # #def css_is_present(self, element):
    #     #try:
    #      #   WebDriverWait(self.context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
    #    # except Exception:
    #      #   pass
    #
    #     if self.context.driver.find_element(By.CSS_SELECTOR, element).is_displayed():
    #         return True
    #     else:
    #         return False

    def wait_for_xpath_to_be_present(self, element):
        try:
            WebDriverWait(self.context.driver, 20).until(EC.presence_of_element_located((By.XPATH, element)))
        except TimeoutException as te:
            print('xpath = ' + element + ' cannot be found')
            raise te

    def xpath_is_present(self, element):
        try:
            WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
            if (self.context.driver.find_element(By.XPATH, element).is_displayed()):
                return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    def css_is_present(self, element):
        try:
            WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            if(self.context.driver.find_element(By.CSS_SELECTOR, element).is_displayed()):
                return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    def take_screenshot(self, directory, ss_name):
        time.sleep(1)
        self.context.driver.get_screenshot_as_file(directory + ss_name + '.png')

    def get_text_from_class(self, element):
        text = self.context.driver.find_element(By.CLASS_NAME, element).text
        return text

    def get_text_from_xpath(self, element):
        text = self.context.driver.find_element(By.XPATH, element).text
        return text

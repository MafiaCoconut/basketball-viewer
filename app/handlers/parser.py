import logging
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchDriverException, NoSuchElementException
import urllib

# from config import config

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
# from config.log_def import set_func
from PIL import Image
import easyocr

from app.handlers import config
from app.utils.logs import set_func
from app.utils.selenium_setup import get_selenium_driver

tag = 'parser'

class Parser:
    def __init__(self):
        self.url = "https://ticket-resale.paris2024.org/tickets/all/1/1/18172109"

        self.driver = None
        self.service = None
        self.options = None
        self.waiting_time = 2
        self.ddos_flag = False
        self.captcha_count = 0

    def start_parser(self):
        function_name = 'start_parser'
        set_func(function_name, tag)
        print(0)
        self.driver = get_selenium_driver()
        print(1)
        self.driver.get("https://ticket-resale.paris2024.org/tickets/all/1/1/18172109")

        print(self.driver.current_url)

        self.ddos_flag = False
        self.captcha_count = 0

        time.sleep(self.waiting_time)
        # self.open_page()
        try:
            button = self.driver.find_element(By.XPATH, '//*[@id="EventDetailsAndListingCard"]/div[4]/div[3]/div[3]')
            button.click()
            self.save_screenshot("termins")
            return "Есть свободные записи"
        except:
            self.save_screenshot("termins")
            return "Нет свободных записей"





        # button.click()
        # time.sleep(self.waiting_time)

        self.driver.close()

        # self.driver.click()


        # while True:
        #     try:
        #         if self.set_captcha():
        #             break
        #         if self.ddos_flag:
        #             break
        #     except:
        #         pass

        # if self.ddos_flag:
        #     self.save_screenshot("ddos_screenshot")
        #     return "Сайт заподозрил DDOS"
        # else:
        #     next_button = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_ButtonB"]')
        #     next_button.click()
        #     time.sleep(self.waiting_time)
        #
        #     data = self.driver.find_element(By.XPATH, '//*[@id="center-panel"]')
        #     if "нет свободного времени" in data.text:
        #         self.save_screenshot("termins")
        #         data = "Нет свободных записей"
        #     else:
        #         self.save_screenshot("termins")
        #         data = "Есть свободные записи"
        #
        #     self.driver.close()
        #     return data

    def set_captcha(self):
        function_name = 'set_captcha'
        set_func(function_name, tag)

        self.captcha_count += 1
        if self.captcha_count >= 5:
            self.captcha_count = 0
            self.ddos_flag = True
            return False

        captcha = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_imgSecNum"]')
        captcha.screenshot("data/captcha.png")

        reader = easyocr.Reader(['en'])
        image_path = "data/captcha.png"
        result = reader.readtext(image_path)[0][-2]
        logging.info(f" ---------------- '{result}' ----------------")
        if not self.check_result:
            logging.info('Обновление страницы')
            self.open_page()
            return False

        captcha_code = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_txtCode"]')
        captcha_code.send_keys(result)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_ButtonA"]')
        next_button.click()

        time.sleep(self.waiting_time)

        if self.is_captcha_correct():
            logging.info('Капча правильная')
            return True

        logging.info("Капча неправильная")
        self.clear_captcha_code()
        return False

    def is_captcha_correct(self):
        function_name = 'is_captcha_correct'
        set_func(function_name, tag)

        try:
            item = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_lblCodeErr"]')
            return False
        except:
            return True

    def clear_captcha_code(self):
        function_name = 'clear_captcha_code'
        set_func(function_name, tag)

        captcha_code = self.driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_txtCode"]')
        captcha_code.clear()

    def open_page(self):
        function_name = 'open_page'
        set_func(function_name, tag)

        self.driver.get(self.url)
        time.sleep(self.waiting_time)

    def save_screenshot(self, name):
        function_name = f'save_screenshot: {name}'
        set_func(function_name, tag)

        self.driver.save_screenshot(f"data/{name}.png")

    @staticmethod
    def test_func():
        function_name = 'test_func'
        set_func(function_name, tag)

        data1 = "Есть свободные записи"
        data2 = "Нет свободных записей"
        data3 = "Сайт заподозрил DDOS"
        return data2

    def check_result(self, result: str):
        function_name = 'check_result'
        set_func(function_name, tag)

        if len(result) >= 8:
            logging.info(f"Сайт думает что это DDOS. Так как result='{result}'")
            self.ddos_flag = True
            return False
        else:
            numbers = [i for i in range(10)]
            for item in result:
                if item not in numbers:
                    logging.info(f"В капче '{result}' ошибка в символе '{item}'")
                    return False
                # if not item.isdigit():
                #     return False

        return True

    def set_raspberry_geckodriver(self):
        function_name = 'set_raspberry_geckodriver'
        set_func(function_name, tag)

        FF_OPTIONS = [
            '--headless',
            '--no-sandbox',
            '--disable-xss-auditor',
            '--disable-web-security',
            '--ignore-certificate-errors',
            '--log-level=3',
            '--disable-notifications',
        ]

        SET_PREF = {
            'general.useragent.override': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'permissions.default.desktop-notification': 1,
            'dom.webnotifications.enabled': 1,
            'dom.push.enabled': 1,
            'intl.accept_languages': 'en-US'
        }

        options = FirefoxOptions()
        [options.add_argument(opt) for opt in FF_OPTIONS]
        [options.set_preference(key, value) for key, value in SET_PREF.items()]

        path_to_geko = "/home/pi/Downloads/geckodriver"
        self.driver = webdriver.Firefox(service=Service(path_to_geko), options=options)

    def set_laptop_geckodriver(self):
        function_name = 'set_laptop_geckodriver'
        set_func(function_name, tag)

        # proxy = '198.27.115.215:80'
        # # ip = '85.26.146.169'
        # # port = '80'
        # options = FirefoxOptions()
        # options.proxy = Proxy({
        #     'proxyType': ProxyType.HTTP,
        #     'httpProxy': proxy,
        #     'sslProxy': proxy,
        #     'noProxy': ''})
        self.driver = webdriver.Firefox()


    def open_2ip(self):
        function_name = 'open_2ip'
        set_func(function_name, tag)

        self.driver.get("https://2ip.ru")
        time.sleep(5)







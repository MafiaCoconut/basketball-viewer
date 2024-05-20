# import os
#
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
#
# def get_selenium_driver():
#     profile_path = '/home/mafiacoconut/.mozilla/firefox/mshugs1l.default-release'
#     FF_OPTIONS = [
#         '--headless',
#         '--no-sandbox',
#         '--accept-cookies',
#         '--disable-xss-auditor',
#         '--disable-web-security',
#         '--ignore-certificate-errors',
#         '--log-level=1',
#         '--disable-notifications',
#         f'-profile {profile_path}'
#     ]
#
#     SET_PREF = {
#         'general.useragent.override': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         'permissions.default.desktop-notification': 1,
#         'dom.webnotifications.enabled': 1,
#         'dom.push.enabled': 1,
#         'intl.accept_languages': 'en-US'
#     }
#
#     options = FirefoxOptions()
#
#     if os.getenv("DEVICE") == "Ubuntu" or os.getenv("DEVICE") == "Laptop":
#         options.binary_location = "/usr/bin/firefox"
#         print('ноут')
#         current_directory = os.path.dirname(os.path.realpath(__file__))
#         current_directory = current_directory[:current_directory.rfind('/')]
#         # print(f"current_directory: {current_directory}")
#         geckodriver_path = os.path.join(current_directory, "geckodriver")
#         # ic(f"geckodriver path: {geckodriver_path}")
#     # elif os.getenv("DEVICE") == "RaspberryTest":
#     elif os.getenv("DEVICE") == "Raspberry" or os.getenv("DEVICE") == "RaspberryTest":
#         print('сервер')
#         geckodriver_path = "/app/geckodriver"
#     else:
#         raise Exception("Неправильный ENV DEVICE")
#
#     [options.add_argument(opt) for opt in FF_OPTIONS]
#     [options.set_preference(key, value) for key, value in SET_PREF.items()]
#
#     driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)
#
#     return driver

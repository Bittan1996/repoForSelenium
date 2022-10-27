from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=1).install(), options=options,)
    context.browser = driver
    context.browser.maximize_window()
    print('before_all')


def after_all(context):
    context.browser.quit()
    print('after_all')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=1).install())
    driver.find_element_by_xpath()
    context.browser = driver
    context.browser.maximize_window()
    print('before_all')


def after_all(context):
    context.browser.quit()
    print('after_all')


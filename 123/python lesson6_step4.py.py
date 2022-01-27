import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("form > :nth-child(1) > .form-control")
    name.send_keys("123")
    last_name = browser.find_element_by_css_selector("form > :nth-child(2) > .form-control")
    last_name.send_keys("321")
    citi = browser.find_element_by_css_selector(".city")
    country = browser.find_element_by_id("country")
    citi.send_keys("voronehz")
    country.send_keys('russha')
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

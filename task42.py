from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = r'/Users/vladkishchak/chromedriver_mac64/chromedriver '

driver = webdriver.Chrome(service = Service (driver_path))

driver.get('https://www.lez.com.ua')


def capture_screenshot_with_highlights(filename, locator_type, locator):
    element = None
    if locator_type == 'xpath':
        element = driver.find_element_by_xpath(locator)
    elif locator_type == 'css':
        element = driver.find_element_by_css_selector(locator)

    driver.execute_script("arguments[0].style.border='2px solid red'", element)

    driver.save_screenshot(filename)

    driver.execute_script("arguments[0].style.border=''", element)

css_locators = ['div',
                '.header',
                '#menu' ,
                '[href="/about"]',
                'ul.nav li.active']

xpath_locators = ['//div',
                  '//*[@class="header"]',
                  '//*[@id="menu"]',
                  '//*[@href="/about"]',
                  '//*[text()="Some text"']

for i, xpath_locator in enumerate(xpath_locators):
    filename = f'legtah_xpath_element_{i+1}.png'
    capture_screenshot_with_highlights(filename, 'xpath', xpath_locators)

for i, css_locator in enumerate(css_locators):
    filename = f'legtah_css_element_{i+1}.png'
    capture_screenshot_with_highlights(filename, 'css', css_locators)


driver.quit()


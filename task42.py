from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#
# Устанавливаем путь к драйверу Selenium (например, для Chrome)
driver_path = r''

# Создаем экземпляр драйвера
driver = webdriver.Chrome(service=Service(driver_path))

# Загружаем веб-ресурс
driver.get('https://legtah.com/')

# Функция для создания скриншота с выделенными элементами
def capture_screenshot_with_highlights(filename, locator_type, locator):
    # Находим элемент на странице
    element = None
    if locator_type == 'xpath':
        element = driver.find_element_by_xpath(locator)
    elif locator_type == 'css':
        element = driver.find_element_by_css_selector(locator)

    # Выделяем элемент на скриншоте
    driver.execute_script("arguments[0].style.border='2px solid red'", element)

    # Создаем скриншот страницы
    driver.save_screenshot(filename)

    # Удаляем выделение элемента
    driver.execute_script("arguments[0].style.border=''", element)

# Примеры XPath локаторов
xpath_locators = [
    "//a[contains(@href, 'about')]",  # Ссылка с текстом 'About'
    "//h1[contains(text(), 'LEGTAH')]",  # Заголовок с текстом 'LEGTAH'
    "//input[@placeholder='Search']",  # Поле поиска
    "//div[@class='hero-slider']",  # Элемент с классом 'hero-slider'
    "(//div[@class='product-card'])[1]"  # Первая карточка товара
]

# Примеры CSS локаторов
css_locators = [
    "a[href*='about']",  # Ссылка с текстом 'About'
    "h1:contains('LEGTAH')",  # Заголовок с текстом 'LEGTAH'
    "input[placeholder='Search']",  # Поле поиска
    "div.hero-slider",  # Элемент с классом 'hero-slider'
    "div.product-card:first-of-type"  # Первая карточка товара
]

# Создаем скриншоты с выделенными элементами для XPath локаторов
for i, xpath_locator in enumerate(xpath_locators):
    filename = f'legtah_xpath_element_{i+1}.png'
    capture_screenshot_with_highlights(filename, 'xpath', xpath_locator)

# Создаем скриншоты с выделенными элементами для CSS локаторов
for i, css_locator in enumerate(css_locators):
    filename = f'legtah_css_element_{i+1}.png'
    capture_screenshot_with_highlights(filename, 'css', css_locator)

# Закрываем браузер
driver.quit()


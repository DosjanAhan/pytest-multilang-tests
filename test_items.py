import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):
    # Открываем тестовую страницу
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки языка

    # Ищем кнопку добавления в корзину
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, "Кнопка добавления в корзину отсутствует!"

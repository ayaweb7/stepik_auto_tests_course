from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
url = 'https://google.com'
try:
    # open google.com
    browser.get(url)
    search = browser.find_element_by_tag_name('input')

    # search request for OZON.ru
    search.send_keys('ozon.ru')
    search.send_keys(Keys.RETURN)

    # locate by partial link and open ozon.ru
    browser.find_element_by_partial_link_text('OZON — интернет-магазин').click()
    # sleep(5)
    wait = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "div[type='addToCartButton']"))

    prod_1 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(3) div[type='addToCartButton']").click()

    prod_2 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(4) div[type='addToCartButton']").click()

    prod_3 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(5) div[type='addToCartButton']").click()

    cart = browser.find_element_by_css_selector("a[href='/cart/']").click()
    wait1 = WebDriverWait(browser, 20).until(EC.element_to_be_selected(By.CSS_SELECTOR, '.container:nth-child(3) .a7m4'))
    goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')

    print(goods)
    print(len(goods))

    assert len(goods) == 3, 'в корзине не 3 вещи'
finally:
    sleep(2)
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python ozon.py
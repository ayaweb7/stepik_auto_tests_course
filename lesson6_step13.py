from selenium import webdriver
import time

browser = webdriver.Chrome()

email = input("Введите email\t>> ")
password = input("Введите пароль\t>> ")

browser.get("https://stepik.org/course/575/promo?auth=login")
time.sleep(3)
def click(s):
    browser.find_element_by_css_selector(s).click()
def clickxpath(s):
    browser.find_element_by_xpath(s).click()
def send(s,keys):
    browser.find_element_by_css_selector(s).send_keys(keys)

send('[name = "login"]', email)
send('[name = "password"]', password)
click(".sign-form__btn")
time.sleep(1)
s = ['//*[contains(text(), "Тестовые фреймворки в Python")]',
'//*[contains(text(), "Использование паттерна PageObject для упрощения поддержки авто-тестов")]',
'//*[contains(text(), "Настройка окружения Selenium WebDriver")]',
'//*[contains(text(), "Поиск элементов на HTML-странице")]',
'//*[contains(text(), "Запуск браузера с помощью Selenium WebDriver")]',
'//*[contains(text(), "Методы работы с всплывающими окнами браузера в Selenium WebDriver")]',
'//*[contains(text(), "Методы для поиска элементов в Selenium WebDriver")]',
'//*[contains(text(), "Параллельный запуск тестов")]',]
def nl(n):
    return (10 - len(bin(n))) * "0" + bin(n)[2:]

def c(n = 0):
    while True:
        n += 1
        print(n)
        es = []
        c = nl(n)
        for i in range(8):
            if c[i] == "1":
                es.append(s[i])
        for i in es:
            clickxpath(i)
            time.sleep(0.05)
        click(".submit-submission")
        time.sleep(1.5)
        click(".again-btn")
        time.sleep(1.5)
        if n > 255:
            return "!"

def ss():
    browser.get("https://stepik.org/lesson/138920/step/12?unit=196194")
    time.sleep(4)
    browser.execute_script("window.scrollBy(0, 300);")
    c()
    
ss()

# не забываем оставить пустую строку в конце файла
# python lesson6_step13.py
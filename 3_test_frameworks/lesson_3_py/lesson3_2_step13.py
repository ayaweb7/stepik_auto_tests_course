from selenium import webdriver
import time
import unittest


class test_class_name(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector("div.first_block .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("div.first_block .second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector("div.first_block .third")
        email.send_keys("test@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"ожидали: {'Congratulations! You have successfully registered!'}, на самом деле: '{welcome_text}'")
        #self.assertEqual('что должно быть', 'что есть', 'что произошло');
        
    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector("div.first_block .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("div.first_block .second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector("div.first_block .third")
        email.send_keys("test@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"ожидали: {'Congratulations! You have successfully registered!'}, на самом деле: '{welcome_text}'")
        
if __name__ == "__main__":
    unittest.main()

"""

try: 
#    link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("div.first_block .first")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("div.first_block .second")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("div.first_block .third")
    email.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""

# не забываем оставить пустую строку в конце файла
# python lesson3_2_step13.py
# pytest lesson3_2_step13.py
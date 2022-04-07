import pytest
from selenium import webdriver
import time
import math

sum_message = ""
print('sum_message: ', sum_message)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print('sum_message: ', sum_message)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(sum_message)  # напечатать ответ про Сов в конце всей сессии

# 2. Класс который начинается на Test. Как в предыдущих примерах.
# 3. Внутри класса 2 переменные: 1. пустая для сообщения = "".  2. массив со списком адресов
# 4.Внутри класса также есть функция с parametrize
#     ('название переменной для исползования внутри этой функции= неважно какое
#      но желательно подходящее по смыслу я назову links', "название переменой масива со списком адресов")
#      похожее на предыдущий урок
@pytest.mark.parametrize('steps', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLinks:
    sum_message = ""
    print('\nsum_message: ', sum_message)
    # steps = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
    # 5. Эта функция тест поэтому название функции должно начинаться на test_
    # 6. Эта функция получает self, browser, и название переменной для исползования внутри этой функции
    #      ( с 4 пункта ' ' я назову links например)
    # этот тест запустится 8 раз
    def test_stepik_links(browser, steps):
        global sum_message
        # Внутри функции:
        # 7.  Первые 2 строчки как в предыдущем примере 2 предпоследние с небольшим изменением в link
        link = f"https://stepik.org/lesson/{steps}/step/1/"
        browser.implicitly_wait(10)
        # 8. browser.implicitly_wait(10)
        browser.implicitly_wait(5)
        browser.get(link)
        # 9. Ищем textarea
        text_area = browser.find_element_by_css_selector('textarea')
        # text_area = browser.find_element_by_tag_name('textarea')
        # 10. Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера
        answer = math.log(int(time.time() - 3.1))
        text_area.send_keys(str(answer))
        # 11. Через WebDriverWait EC.element_to_be_clickable находим класс кнопку
        # 12. нажимаем на кнопку
        button = browser.find_element_by_css_selector('.submit-submission ')
        button.click()
        browser.implicitly_wait(10)
        time.sleep(5)
        # 13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем переменной
        message = browser.find_element_by_css_selector('.smart-hints__hint').text
        # 14. Проверяем не равен ли он !="Correct!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        try:
            assert 'Correct!' == message
        except AssertionError:
            sum_message += message  # собираем ответ про Сов с каждой ошибкой

# Запустите тест:
# pytest -s -v test_alien_363.py
# наконец-то получилось выводить тесты в удобочитаемом виде без всяких warnings и тд:
# pytest -s -v -m smoke test_alien_363.py -q --tb=no -p no:warnings
from selenium import webdriver
import pytest
import time
import math

final = ''

@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    # Добавьте в функцию которая открывает браузер эти строки:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield br
    br.quit()
    print('\n', final)  # напечатать ответ про Сов в конце всей сессии

@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time() - 3.1))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    print(check_text)
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        print(link, ": expected 'Correct!', got", check_text)
        final += check_text  # собираем ответ про Сов с каждой ошибкой

# Запустите тест:
# pytest -s -v test_alien_363_1.py
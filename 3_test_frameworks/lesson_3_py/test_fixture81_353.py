import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_fixture81_353.py
# А что означает -s -v -m ?
# флаги для запуска: -s выводить в консоль принты, -v выводить полный отчёт,  -m запускать маркированные тесты.

# наконец-то получилось выводить тесты в удобочитаемом виде без всяких warnings и тд:
# pytest -s -v -m smoke test_fixture81_353.py -q --tb=no -p no:warnings

# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
# pytest -s -v -m "smoke and win10" test_fixture81_353.py
# Должен выполнится тест test_guest_should_see_basket_link_on_the_main_page.
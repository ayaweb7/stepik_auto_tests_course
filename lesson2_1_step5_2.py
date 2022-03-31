import os
import time
import math
from selenium import webdriver as driver


class ChromeDriver:
    """Объект Chrome driver."""
    def __init__(self):
        # Если были открыты - принудительно закрываю все Chrome и драйвер
        os.system("TASKKILL /F /IM chrome.exe /IM chromedriver.exe")
        # Объект браузера
        self.browser = driver.Chrome(chrome_options=self.chrome_options())
        # Статус выполнения задачи
        self.status = False

    def chrome_options(self):
        """Настройка Chrome browser"""
        print("Устанавливаю настройки для Chrome browser...")
        options = driver.ChromeOptions()
        # При запуске разворачивать на весь экран
        options.add_argument("--start-maximized")
        # Отключить уведомления об автоматическом режиме
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        print("Настройки для Chrome browser установлены.")
        return options

    def wait_element_by_xpath(self, element, time_wait: int=30, reraise=False) -> bool:
        """Проверяет доступен ли элемент по xpath.\n
        * time_wait - сколько ждем (30сек.)\n
        * reraise - бросать ли исключение (False)"""
        while not self.browser.find_elements_by_xpath(element) and time_wait > 0:
            time.sleep(1)
            time_wait -= 1
        # Если время ожидания не истекло до обнаружения элемента - это успех. Иначе - либо False, либо Exception.
        if time_wait:
            return True
        else:
            if not reraise:
                return False
            else:
                # Генерирую ошибку
                self.browser.find_element_by_xpath(element)

    def wait_alert(self, time_wait: int=30, reraise=False):
        """Проверяет доступно ли окно alert.\n
        * time_wait - сколько ждем (30сек.)\n
        * reraise - бросать ли исключение (False)"""
        check_flag = False
        while not check_flag and time_wait > 0:
            try:
                temp = self.browser.switch_to.alert.text
                check_flag = True
            except Exception:
                time.sleep(1)
                time_wait -= 1
        # Если время ожидания не истекло до обнаружения элемента - это успех. Иначе - либо False, либо Exception.
        if time_wait:
            return True
        else:
            if not reraise:
                return False
            else:
                # Генерирую ошибку
                raise Exception("Не удалось обнаружить окно Alert!")

    def calc(self, x):
        """Рассчитывает математическую функцию от x."""
        return str(math.log(abs(12 * math.sin(int(x)))))

    def __del__(self):
        # Закрываю браузер и драйвер
        print("Закрываю браузер и chrome драйвер...")
        try:
            time.sleep(1)
            self.browser.close()
            time.sleep(1)
            self.browser.quit()
            time.sleep(1)
        except Exception:
            pass
        finally:
            # Если остались открыты - принудительно закрываю все Chrome и драйвер
            os.system("TASKKILL /F /IM chrome.exe /IM chromedriver.exe")
        print("Браузер и chrome драйвер закрыты.")


if __name__ == "__main__":
    print("===== СТАРТ =====")

    try:
        print("Инициализирую Chrome object...")
        worker = ChromeDriver()
        print("Инициализация Chrome object завершена.")
        # 1) Открыть страницу http://suninjuly.github.io/math.html.
        print("Открываю страницу в браузере...")
        worker.browser.get("http://suninjuly.github.io/math.html")
        print("Страница в браузере открыта.")
        # 2) Считать значение для переменной x.
        print("Считываю значение для переменной x...")
        worker.wait_element_by_xpath('//span[@class="nowrap"][@id="input_value"]')
        x = worker.browser.find_element_by_xpath('//span[@class="nowrap"][@id="input_value"]').text
        print(f"Значение для переменной x считано как [{x}].")
        # 3) Посчитать математическую функцию от x.
        print("Высчитываю математическую функцию от x...")
        calc = worker.calc(x)
        print(f"Математическая функция от x высчитана как: [{calc}].")
        # 4) Ввести ответ в текстовое поле.
        print("Ввожу ответ в текстовое поле...")
        worker.browser.find_element_by_xpath('//input[@id="answer"]').send_keys(calc)
        print("Ответ в текстовое поле введен.")
        # 5) Отметить checkbox "I'm the robot".
        print("Отмечаю checkbox 'I\'m the robot'...")
        worker.browser.find_element_by_xpath('//input[@id="robotCheckbox"]').click()
        print("Checkbox 'I\'m the robot' отмечен...")
        # 6) Выбрать radiobutton "Robots rule!".
        print("Выбраю radiobutton 'Robots rule!'...")
        worker.browser.find_element_by_xpath('//input[@id="robotsRule"]').click()
        print("Radiobutton 'Robots rule!' выбран.")
        # 7) Нажать на кнопку Submit.
        print("Нажимаю на кнопку 'Submit'...")
        worker.browser.find_element_by_xpath('//button[@type="submit"]').click()
        print("На кнопку 'Submit' нажал.")
        # Считываю текст с окна с результатом
        print("Считываю текст с окна содержащего результат...")
        worker.wait_alert()
        result = worker.browser.switch_to.alert.text.split()[-1]
        print(f"Текст с окна содержащего результат считан как: [\033[1m\033[91m{result}\033[0m].")

    except Exception as ex:
        print(f"Системная ошибка: [{ex}].")

    print("===== КОНЕЦ =====")

# не забываем оставить пустую строку в конце файла
# python lesson2_1_step5_2.py
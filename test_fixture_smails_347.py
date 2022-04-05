import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
 #область покрытия class означает, что фикстура будет вызываться один раз для класса
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n") # эта часть выполниться только после прогона всех тестов

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

@pytest.fixture(autouse=True)  
# параметр autouse=True указывает на то, что данная фикстура будет 
# запускаться для каждого теста , даже без явного вызова

def print_smiling_faces():
    print(":-Р", "\n")

class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):  
# вызываем фикстуру prepare_faces в тесте, передав ее как параметр (выполнится сначала "^_^", а потом после окончания второго теста ":3")
# вызываем фикстуру very_important_fixtureв тесте, передав ее как параметр
# не передаём как параметр фикстуру print_smiling_faces, но она все равно выполняется
        pass

    def test_second_smiling_faces(self, prepare_faces): 
# фикстура prepare_faces вызывается в данном тесте, но так как она задана для класса, то тут выполняться не будет
# не передаём как параметр фикстуру print_smiling_faces, но она все равно выполняется
        pass

# pytest -s -v test_fixture_smails_347.py
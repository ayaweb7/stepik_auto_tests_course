import pytest
from selenium import webdriver

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False

# pytest -s -v test_xfail_356.py
# pytest -v test_xfail_356.py
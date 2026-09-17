from time import sleep
import pytest
from selene import browser
import time

def test_tmp():
    browser.open('https://www.google.com')
    sleep(5)

    print('\n Тест прошел успешно \n*************************************')
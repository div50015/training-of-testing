from selene import browser
import pytest


def test_text_box_fill():
    browser.open('/text-box')

    browser.element('#userName').type('IGOR')
    browser.element('#userEmail').type('div50015@mail.ru')
    browser.element('#currentAddress').type('MOSKOVSKATA 100')
    browser.element('#permanentAddress').type('MOSKOVSKATA 200')
    browser.element('#submit').click()
    pass
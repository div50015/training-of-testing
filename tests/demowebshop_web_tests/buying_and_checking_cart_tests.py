import pytest
from selene import browser, have


def test_buying_and_checking_card():
    # GIVEN

    browser.open('')
    browser.element('[href=\/login]').click()
    browser.element('#Email').type('example1200@example.com')
    browser.element('#Password').type('123456')

    # WHEN

    browser.element('.button-1.login-button').click()
    browser.element('[href=\/computers]').click()
    browser.all('[href=\/notebooks]')[2].click()
    browser.element('input.button-2').click()
    browser.all('[href=\/cart]')[1].click()

    # THEN

    browser.element('.product-name').should(have.text('14.1-inch Laptop'))

    # Clear cart
    browser.element('.remove-from-cart>input[type=checkbox]').click()
    browser.element('input[name=updatecart]').click()

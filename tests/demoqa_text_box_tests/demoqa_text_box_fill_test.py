from selene import browser
import pytest
from selene.support.conditions import have


def test_text_box_fill():
    # GIVEN
    browser.open('/text-box')

    # WHEN
    browser.element('#userName').type('IGOR')
    browser.element('#userEmail').type('div50015@mail.ru')
    browser.element('#currentAddress').type('MOSKOVSKATA 100')
    browser.element('#permanentAddress').type('MOSKOVSKATA 200')
    browser.element('#submit').click()

    # THEN
    browser.element('#output #name').should(have.text('Name:IGOR'))
    browser.element('#output #email').should(have.text('Email:div50015@mail.ru'))
    browser.element('#output #currentAddress').should(have.text('Current Address :MOSKOVSKATA 100'))
    browser.element('#output #permanentAddress').should(have.text('Permananet Address :MOSKOVSKATA 200'))


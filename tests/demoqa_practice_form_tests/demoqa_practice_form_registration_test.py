import pytest
from selene import browser, have, command
from time import sleep
import os.path
from selenium.webdriver import Keys


def test_demoqa_practice_form_registration():
    # GIVEN
    browser.open('https://demoqa.com/automation-practice-form')


    pass
    browser.element('#firstName').type('ИГОРЬ')
    browser.element('#lastName').type('ПЕТРОВ')
    browser.element('#userEmail').type('div50015@mail.ru')
    browser.element('[value=Male][name=gender]').click()
    browser.element('#userNumber').type('9999999991')
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('4 Aug 1967').press_enter()
    pass
    browser.element('#subjectsInput').type('His').press_enter()
    browser.all('[id^=hobbies-checkbox]')[0].click()
    browser.element('#currentAddress').type('Roctov city Moskovskaya strit bilding 10')

    browser.element("#state").click()
    browser.all("[id^=react-select]").element_by(have.text("Rajasthan")).click()

#    browser.element('#state').click()
#    browser.all('[id^=react-select]').element_by(have.text('NCR')).click()
    pass
    # WHEN

    # THEN

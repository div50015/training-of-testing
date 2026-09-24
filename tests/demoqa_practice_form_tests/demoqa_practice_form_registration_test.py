from pathlib import Path
import os.path
import pytest
from selene import browser, have, command
from time import sleep
import os.path
from selenium.webdriver import Keys


def test_demoqa_practice_form_registration():
    # GIVEN
    browser.config.window_width = 1000
    browser.config.window_height = 1100

    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")

    # WHEN

    browser.element('#firstName').type('ИГОРЬ')
    browser.element('#lastName').type('ПЕТРОВ')
    browser.element('#userEmail').type('div50015@mail.ru')
    browser.element('[value=Male][name=gender]').click()
    browser.element('#userNumber').type('9999999991')
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('4 Aug 1967').press_enter()
    pass
    browser.element('#subjectsInput').type('His').press_enter()
    browser.all('[id^=hobbies-checkbox]')[0].click()

    # browser.element('#uploadPicture').set_value(
    #     str(Path(tests.__file__).parent.joinpath('demoqa_pactice_form_tests/resources/foto.jpg').absolute())
    import tests

    browser.element("#uploadPicture").send_keys(
        os.path.dirname(tests.__file__), "/demoqa_practice_form_tests/resources/foto.jpg"
    )


    browser.element('#currentAddress').type('Moskovskaya strit 10')


    browser.element("#state").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("NCR")).click()
    browser.element("#city").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Delhi")).click()

    browser.element("#submit").click()
    pass


    # THEN

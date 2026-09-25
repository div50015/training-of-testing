from pathlib import Path
import os.path
import pytest
from selene import browser, have, command
from time import sleep
import os.path
from selenium.webdriver import Keys
import tests


def test_demoqa_practice_form_registration():
    # GIVEN

    browser.open('/automation-practice-form')
    browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")

    # WHEN

    browser.element('#firstName').type('ИГОРЬ')
    browser.element('#lastName').type('Д')
    browser.element('#userEmail').type('div@mail.ru')
    browser.element('[value=Male][name=gender]').click()
    browser.element('#userNumber').type('9999999991')
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('10 Aug 1999').press_enter()
    browser.element('#subjectsInput').type('His').press_enter()
    browser.all('[id^=hobbies-checkbox]')[0].click()
    # browser.element('#uploadPicture').set_value(
    #     str(Path(tests.__file__).parent.joinpath('demoqa_pactice_form_tests/resources/foto.jpg').absolute())
    browser.element("#uploadPicture").send_keys(
        os.path.dirname(tests.__file__), "/demoqa_practice_form_tests/photo.jpg"
    )
    browser.element('#currentAddress').type('Moskovskaya Street 10')
    browser.element("#state").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("NCR")).click()
    browser.element("#city").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Delhi")).click()
    browser.element("#submit").click()

    # THEN

    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'ИГОРЬ Д',
        'Student Email', 'div@mail.ru',
        'Gender', 'Male',
        'Mobile', '9999999991',
        'Date of Birth', '10 August,1999',
        'Subjects', 'History',
        'Hobbies', 'Sports',
        'Picture', 'photo.jpg',
        'Address', 'Moskovskaya Street 10',
        'State and City', 'NCR Delhi'
    ))

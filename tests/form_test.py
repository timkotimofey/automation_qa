import time

import allure

from pages.form_page import FormPage


@allure.suite('Forms')
class TestForm:
    @allure.feature('FormPage')
    class TestFormPage:

        @allure.title('Check form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()
            result = form_page.form_result()
            print(person_info)
            print(result)
            # print(person_info.firstname, person_info.lastname, person_info.email)
            # print(result[0], result[1])
            assert str(person_info.firstname) + " " + str(person_info.lastname) + str(person_info.email) == str(
                result[0]) + str(result[1]), "the form has not been filled"

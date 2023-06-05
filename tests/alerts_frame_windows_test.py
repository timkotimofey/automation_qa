import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new tab has not opened or an incorrect tab has opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new window has not opened or an incorrect tab has opened"

    @allure.feature('Alerts Page')
    class TestAlertPage:

        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok' or alert_text == 'You selected Cancel', 'Alert did not show up'

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            # print(text)
            # print(alert_text)
            assert alert_text == f'You entered {text}', 'Alert did not show up'

    @allure.feature('Frame Page')
    class TestFramesPage:

        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Page')
    class TestNestedFramesPage:

        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialog Page')
    class TestModalDialogPage:
        @allure.title('Check the page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            # print(small)
            # print(large)
            assert small == ['Small Modal', 47], 'The header is not "Small modal"'
            assert large == ['Large Modal', 574], 'The header is not "Large modal"'

        @allure.title('Check the page with close_by_cross')
        def test_close_by_cross(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            modal_dialogs_page.check_modal_close_by_cross()

import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'The added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_after != count_value_before, 'Value was not deleted'

        def test_remove_all_values_cross(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            time.sleep(3)
            before_list, after_list = autocomplete_page.remove_all_values()
            time.sleep(3)
            assert after_list == '', 'All values were not deleted'

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            # print(color)
            # print(color_result)
            assert color == color_result, 'The added colors are missing in the input'


class TestDatePickerPage:
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after, 'The date has not been changed'

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        # print(value_date_before)
        # print(value_date_after)
        assert value_date_before != value_date_after, 'The date and time have not been changed'


class TestSliderPage:
    def test_slider(self, driver):
        slider = SliderPage(driver, "https://demoqa.com/slider")
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, 'the slider value has not been changed'


class TestProgressBarPage:
    def test_progress_bar(self, driver):
        progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after, 'the progress bar value has not been changed'

    def test_progress_bar_reset(self, driver):
        progress_bar_reset = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_reset.open()
        before, after, reset = progress_bar_reset.reset_progress_bar_value()
        assert (after != reset) and reset == '0%', 'the progress bar value has not been reset'


class TestTabsPage:

    def test_tabs(self, driver):
        tabs = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs.open()
        what_button, what_content = tabs.check_tabs('what')
        origin_button, origin_content = tabs.check_tabs('origin')
        use_button, use_content = tabs.check_tabs('use')
        more_button, more_content = tabs.check_tabs('more')
        assert what_button == 'What' and what_content != 0, 'the tab "What" was not pressed or text is missing'
        assert origin_button == 'Origin' and origin_content != 0, 'the tab "Origin" was not pressed or text is missing'
        assert use_button == 'Use' and what_content != 0, 'the tab "Use" was not pressed or text is missing'
        assert more_button == 'More' and more_content != 0, 'the tab "More" was not pressed or text is missing'


class TestToolTips:

    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        print(button_text)
        print(field_text)
        print(contrary_text)
        print(section_text)
        assert button_text == 'You hovered over the Button', 'hover missing or incorrect'
        assert field_text == 'You hovered over the text field', 'hover missing or incorrect'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect'
        assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect'






import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        # print(section_title.text)
        # print(section_content)
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        # print(colors)
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        # print(count_value_before)
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        # print(remove_button_list)
        for value in remove_button_list:
            value.click()
            break  # for remove only one element
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        # print(count_value_after)
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        print(color_list)
        print(color_list[0].text)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def remove_all_values(self):
        color_list_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        # print(color_list_before)
        remove_all_cross = self.element_is_visible(self.locators.REMOVE_ALL_CROSS).click()
        color_list_after = self.elements_are_present(self.locators.MULTI_INPUT)
        # print(color_list_before)
        # print(color_list_after[0].text)
        return color_list_before, color_list_after[0].text

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text






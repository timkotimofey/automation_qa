import random

from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self, name_select):
        tabs = {'list':
                    {'tab': self.locators.TAB_LIST,
                     'list': self.locators.LIST_ITEM},
                'grid':
                    {'tab': self.locators.TAB_GRID,
                     'list': self.locators.GRID_ITEM}
                }

        self.element_is_visible(tabs[name_select]['tab']).click()
        order_before = self.get_sortable_items(tabs[name_select]['list'])
        item_list = random.sample(self.elements_are_visible(tabs[name_select]['list']),
                                  k=2)  # here i am choose two random elements
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(tabs[name_select]['list'])
        # print(order_before)
        # print(order_after)
        return order_before, order_after

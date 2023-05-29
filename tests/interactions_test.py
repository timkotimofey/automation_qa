from pages.interactions_page import SortablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable_for_list(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order('list')
            # print(order_before)
            # print(order_after)
            assert order_before != order_after, 'the order of the list has not been changed'

        def test_sortable_for_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order('grid')
            # print(order_before)
            # print(order_after)
            assert order_before != order_after, 'the order of the grid has not been changed'




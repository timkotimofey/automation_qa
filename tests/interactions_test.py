from pages.interactions_page import SortablePage, SelectablePage


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

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            # print(item_list)
            # print(item_grid)
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, 'no elements were selected'

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            print(max_box, min_box)
            print(max_resize, min_resize)
            assert ('500px', '300px') == max_box, 'maximum size not equal to 500px, 300px'
            assert ('150px', '150px') == min_box, 'maximum size not equal to 150px, 150px'
            assert min_resize != max_resize, 'resizable has not been changed'

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            # print(text)
            assert text == 'Dropped!', "the elements has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', "the dropped element has been accepted"
            assert accept == 'Dropped!', "the dropped element has not been accepted"
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', "the elements texts has not been changed"
            assert not_greedy_inner == 'Dropped!', "the elements texts has not been changed"
            assert greedy == 'Outer droppable', "the elements texts has been changed"
            assert greedy_inner == 'Dropped!', "the elements texts has not been changed"

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'the elements has not reverted'
            assert not_will_after_move == not_will_after_revert, 'the elements has  reverted'






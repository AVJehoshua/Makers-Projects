from lib.take_away_order import *
from unittest.mock import *

"""
Mock Test 1: When a dish and it's price have been created
it's added to a list
"""

def test_mock_dish_added_to_list():
    order = Order()
    mock_meal = Mock()
    order.add(mock_meal)
    assert order.list_all() == [mock_meal]


"""
Mock Test 2: When multiple dishes and their price have been created
it's added to a list
"""

def test_multiple_mock_dishes_added_to_list():
    order = Order()
    mock_meal1 = Mock()
    mock_meal2 = Mock()
    order.add(mock_meal1)
    order.add(mock_meal2)
    assert order.list_all() == [mock_meal1, mock_meal2]


# """
# Mock Test 3: Test returned list of available dishes
# """

# def test_whether_available_dishes_can_be_returned():
#     order = Order()
#     mock_meal_1 = Mock()
#     order.add(mock_meal_1)
#     mock_meal_1.mark_available.return_value = True
#     mock_meal_1.is_available.return_value = True
#     assert order.available_dishes() == [mock_meal_1]
from lib.take_away_meal import *
from unittest.mock import *
import pytest

"""
Test: Testing the construction of a dish and it's price
"""

def test_dish_and_price_construction():
    meal = Meal("Sushi", "3")
    assert meal.dish == "Sushi"
    assert meal.price == "3"


"""
Test: If dish input is an empty string, raise exception:
"""

def test_if_dish_input_is_empty_raise_exception():
    with pytest.raises(Exception) as e:
        meal = Meal(" ", "3")
    assert str(e.value) == "Dish cannot be an empty string!"

"""
Test: If price input is an empty string, raise exception:
"""

def test_if_price_input_is_empty_raise_exception():
    with pytest.raises(Exception) as e:
        meal = Meal("Sushi", " ")
    assert str(e.value) == "Price cannot be an empty string!"


"""
Test: Testing unavailable dishes can be marked as available
"""

def test_marking_available_dishes():
    meal = Meal("Sushi", "3")
    meal.mark_available()


"""
Mock Test:
Test dishes which are initially unavailable,
can be marked as available
"""

def test_whether_available_dishes_can_be_returned():
    mock_order = Mock()
    meal_1 = Meal("Sushi", "3")
    meal_1.mark_available()
    mock_order.available_dishes.return_value = True
    assert mock_order.available_dishes() == True

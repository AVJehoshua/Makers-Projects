"""
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

"""

"""
TWILIO: 
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

"""

"""
Purpose of this project:

To create a program which allows the user,
to ORDER something, after seeing a *list* 
of *dishes and prices*.

For them to make the order, they must be able to see
an option of *available* dishes.

In order to verify the order, the user should be able to 
view an itemised *receipt* with a *grand total*
of the items they have purchased.

So that they have reassurance of delivery time, they would
need a confirmation text stating the estimated,
delivery time, after they have completed the order.

"""


"""
Possible classes:

Order Class: 
-* Purpose is to list an instance of meals class, 
and to show corresponding prices for those meals

-* Also, to show itemised receipt with total of all meal purchase,
for the order

Functions:
__init__(): To store a dict of meal/prices
-* Parameters: 1, a dict representing meal and prices
-* None

all_meals(): To add meals/prices to empty dict in __init__
-* returns, a list of all meals and prices on the menu

customer_receipt(): 
Parameters: None
Returns: A itemised list of all purchased meals/prices,
and total of prices of those meals

"""

"""
Meal Class: 
-* Purpose is to create Meals and prices for those meals
if a meal is out of stock, it should be marked as unavailble

-* all meals start off as available

Functions:
__init__() function:
Parameters: meal name and price
Returns: None

unavailable function: Marks meal as unavailble


"""


"""
Receipt class: Purpsose is to create a receipt-like-format
that can be called from Order class,
and show items user has brought with grand total

Functions: 
__init__(): To store meal and price
Returns: None

meals purchased(): To create list of meals purchased

Meal_totals(): to total up all prices of meals,
that have been purchased

"""

from lib.take_away_order import *
from lib.take_away_meal import *
import pytest

"""
Test 1: When a dish and it's price has been created,
it is added to a list so that the user can view all dishes
"""

def test_construction_of_1_dish_added_to_list():
    order = Order()
    meal_1 = Meal("Sushi", "3")
    order.add(meal_1)
    assert order.list_all() == [meal_1]

"""
Test 2: When multiple dishes and it's prices have been created,
they are added to a list so that the user can view all dishes
"""

def test_construction_of_multiple_dishes_added_to_list():
    order = Order()
    meal_1 = Meal("Sushi", "3")
    meal_2 = Meal("Temaki", "5")
    order.add(meal_1)
    order.add(meal_2)
    assert order.list_all() == [meal_1, meal_2]


"""
Test 3: When available_dishes() is called, user can see
a list of 1 available dishe
"""

def test_available_dishes_return_list():
    order = Order()
    meal_1 = Meal("Sushi", "3")
    meal_2 = Meal("Temaki", "5")
    order.add(meal_1)
    order.add(meal_2)
    meal_1.mark_available()
    assert order.available_dishes() == [meal_1]


"""
Test 4: When available_dishes() is called, user can see
a list of multiple available dishes
"""

def test_multiple_available_dishes_return_list():
    order = Order()
    meal_1 = Meal("Sushi", "3")
    meal_2 = Meal("Temaki", "5")
    meal_3 = Meal("Dragon roll", "8")
    drink_1 = Meal("Grape Soju", "6")
    order.add(meal_1)
    order.add(meal_2)
    order.add(meal_3)
    order.add(drink_1)
    meal_1.mark_available()
    meal_2.mark_available()
    drink_1.mark_available()
    assert order.available_dishes() == [meal_1, meal_2, drink_1]

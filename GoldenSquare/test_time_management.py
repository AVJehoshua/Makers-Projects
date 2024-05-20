"""
1 - describe the problem :

As a user,
So that I can manage my time,
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

60 / 200 = 0.3 words a second

2 - Design the function signature:

Purpose: create a function, called 'time_manager()'
which tracks the time it takes for a reader,
to read a text - reader reads at 200 words a minute


E.g: 1 word = 0.3 seconds
    4 words = 1.2 seconds
    10 words = 3 seconds
    100 words = 30 seconds
    400 words = 2 minutes
    1000 words = 5 minutes

Parameters: 1 num, representing the num of words 
(refer to example above)

Side effects: No side effects.

3 - Create examples as tests:

-* Test if input is an integer, 0, if so, return
0 minutes.

-* Test if input is a string, if so return a nice error message

-* Test if input is an integer, 4, if so return 1.2 seconds

-* Test if input is an integer, 100, if so return 30 seconds

-* Test if input is an integer, 1000, if so return 5 minutes

-* Test if input is an integer, 6900, if so return 34.5 minutes rounded to an int


"""

from lib.time_management import *

# Testing if input is a string, if so return a nice error message

def test_if_input_is_string_not_integer():
    assert time_manager("") == "This is a string, not an integer!"

# Testing if Test if input is an integer, 0, if so, return 0 minutes:

def test_if_input_is_integer_0_return_0():
    assert time_manager(0) == "0 minutes"

# Testing if input is an integer, 4, if so return 1 second:

def test_if_input_is_4_returns_1_second():
    assert time_manager(4) == "4 second"

# Testing if input is an integer, 100, if so return 30 seconds:

def test_if_input_is_200_return_1_minute():
    assert time_manager(200) == "1 minute"


# Testing if input is an integer, 6900, if so return 34.5 minutes rounded to an int:

def test_if_input_is_600_return_3_min():
    assert time_manager(600) == "3 minutes"





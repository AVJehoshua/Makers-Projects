from unittest.mock import *
from lib.mock_track import *

"""
Test to see if keyword matches title
"""

def test_keyword_in_title():
    track_1 = Track("Nostalgia", "Odunsi")
    assert track_1.matches("Nostalgia") == True

"""
Test to see if keyword matches the artist, 
if so return True
"""

def test_keyword_matches_artist():
    track_1 = Track("Nostalgia", "Odunsi")
    assert track_1.matches("Odunsi") == True

"""
Test to see if keyword matches the artist, 
if so return True
"""

def test_keyword_matches_title_or_artist():
    track_1 = Track("Nostalgia", "Odunsi")
    assert track_1.matches("Odunsi") == True

"""
Given a keyword that does not match either title or artist
return False
"""

def test_keyword_does_not_match_title_or_artist():
    track_1 = Track("Nostalgia", "Odunsi")
    assert track_1.matches("pizza") == False



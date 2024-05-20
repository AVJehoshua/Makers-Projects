from unittest.mock import *
from lib.mock_music_library import *


"""
Given i add a track, it is stored in the library
and can be be returned as a list
"""

def test_add_one_track_to_library():
    music_library = MusicLibrary()
    mock_track_1 = Mock()
    music_library.add(mock_track_1)
    assert music_library.track_list == [mock_track_1]


"""
Given i add multiple tracks, it is stored in the library
and can be be returned as a list
"""

def test_add_multiple_track_to_library():
    music_library = MusicLibrary()
    mock_track_1 = Mock()
    mock_track_2 = Mock()
    music_library.add(mock_track_1)
    music_library.add(mock_track_2)
    assert music_library.track_list == [mock_track_1, mock_track_2]

"""
Given i add tracks to a library, i can return a specific
track depending on the keyword inputted
"""

def test_inputted_keyword_return_related_track():
    music_library = MusicLibrary()
    mock_matching = Mock()
    mock_matching.matches.return_value = True
    music_library.add(mock_matching)
    mock_no_match = Mock()
    mock_no_match.matches.return_value = False
    music_library.add(mock_no_match)
    assert music_library.search("Nostalgia") == [mock_matching]



    
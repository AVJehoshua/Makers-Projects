from lib.mock_music_library import *
from lib.mock_track import *

"""
Given i add a track, it is added to the music library
and can be viewed in a list
"""

def test_add_one_track_to_music_library():
    music_library = MusicLibrary()
    track_1 = Track("Nostalgia", "Odunsi")
    music_library.add(track_1)
    assert music_library.track_list == [track_1]



"""
Given i add multiple tracks, it is added to the music library
and can be viewed in a list
"""

def test_add_multiple_track_to_music_library():
    music_library = MusicLibrary()
    track_1 = Track("Nostalgia", "Odunsi")
    track_2 = Track("Heaven or Hell", "Don Tolliver")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.track_list == [track_1, track_2]


"""
Given i add multiple tracks, 
and i search for track title
it returns that track in a list
"""

def test_search_track_by_title():
    music_library = MusicLibrary()
    track_1 = Track("Nostalgia", "Odunsi")
    track_2 = Track("Heaven or Hell", "Don Tolliver")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Nostalgia") == [track_1]

"""
Given i search for a song by partial artist name,
the song is returned in a list
"""

def test_search_track_by_partial_artist():
    music_library = MusicLibrary()
    track_1 = Track("Nostalgia", "Odunsi")
    track_2 = Track("Heaven or Hell", "Don Tolliver")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Don") == [track_2]

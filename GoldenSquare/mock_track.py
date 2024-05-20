# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        self.title = title
        self.artist = artist
        

    def matches(self, keyword):
        return keyword in self.artist or keyword in self.title
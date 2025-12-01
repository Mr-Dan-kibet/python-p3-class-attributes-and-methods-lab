# song.py

class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the total song count
        self.add_song_to_count()
        
        # Add to genres and artists lists
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        
        # Update genre count and artist count
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by 1."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre count dictionary."""
        # If the genre already exists in the dictionary, increment its count
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist count dictionary."""
        # If the artist already exists in the dictionary, increment their count
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        # Otherwise, add them to the dictionary with a count of 1
        else:
            cls.artist_count[artist] = 1
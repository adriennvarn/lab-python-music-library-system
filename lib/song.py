class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    def add_song_to_count(self):
        Song.count += 1
    
    def add_to_genres(self, genre):
        Song.genres.add(genre)
    
    def add_to_artists(self, artist):
        Song.artists.add(artist)
    
    def add_to_genre_count(self, genre):
        count = Song.genre_count.get(genre)
        if count == None:
            Song.genre_count.setdefault(genre, 1)
        else:
            Song.genre_count.update({genre: count + 1})
    
    def add_to_artist_count(self, artist):
        count = Song.artist_count.get(artist)
        if count == None:
            Song.artist_count.setdefault(artist, 1)
        else:
            Song.artist_count.update({artist: count + 1})
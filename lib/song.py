class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.add_song_to_count()

        # Add the genre and artist 
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Add to the genre and artist count histograms
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add the genre to the genres list only if it's unique
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add the artist to the artists list only if it's unique
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # If the genre exists in dictionary, increment the count
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # If artist exists in the dictionary, increment the count
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



# Creating song instances
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
hotel_california = Song("Hotel California", "Eagles", "Rock")
another_song = Song("Another Song", "Jay-Z", "Rap")

# Checking the values 
print(Song.count)            # Output: 3
print(Song.genres)           # Output: ['Rap', 'Rock']
print(Song.artists)          # Output: ['Jay-Z', 'Eagles']
print(Song.genre_count)      # Output: {'Rap': 2, 'Rock': 1}
print(Song.artist_count)     # Output: {'Jay-Z': 2, 'Eagles': 1}



class Music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    def __str__(self):
        headers = ["Performer:", "Song:", "Album", "Year:"]
        return f"{headers[0]: <11}{self.artist}\n{headers[1]: <11}{self.track_title}\n{headers[2]: <11}{self.album}\n{headers[3]: <11}{self.year}"
music1 = Music("Kendrick Lamar", "GOD.", "DAMN", "2017")
music2 = Music("Kanye West", "Runway", "MBDTF", "2010")
print(music1)
print(music2)
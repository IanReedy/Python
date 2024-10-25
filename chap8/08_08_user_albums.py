"""
This code extends the previous album program by adding a while loop 
that allows users to enter an album's artist and title. The program 
creates and prints the album dictionary based on user input, with a 
quit option to exit the loop.
"""

def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    artist = input("Enter the artist's name (or 'quit' to exit): ")
    if artist.lower() == 'quit':
        break
    title = input("Enter the album title: ")
    album = make_album(artist, title)
    print(album)

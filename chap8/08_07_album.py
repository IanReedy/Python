"""
This code defines a function that creates a dictionary for a music album, 
including an optional parameter for the number of songs, and demonstrates 
its use with three albums: Michael Jackson's "Thriller," Travis Scott's "Astroworld," 
and Playboi Carti's "Die Lit."
"""

def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

album1 = make_album("Michael Jackson", "Thriller", 9)
album2 = make_album("Travis Scott", "Astroworld", 17)
album3 = make_album("Playboi Carti", "Die Lit", 19)

print(album1)
print(album2)
print(album3)

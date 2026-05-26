import numpy as np
from ytmusicapi import YTMusic
import webbrowser

yt = YTMusic()

# SONG DATA
songs = np.array([
    [0.6,0.7,0.6,0.5,0.9],
    [0.5,0.6,0.7,0.4,0.9],
    [0.3,0.4,0.9,0.3,0.8],
    [0.4,0.5,0.8,0.4,0.9],
    [0.8,0.9,0.2,0.8,0.9],
    [0.9,0.9,0.1,0.9,0.9],
    [0.9,0.8,0.2,0.9,0.8],
    [0.8,0.7,0.3,0.8,0.8],
    [0.8,0.7,0.3,0.6,0.9],
    [0.9,0.8,0.2,0.7,0.9]
])

song_details = [
    ("Love Story","Taylor Swift"),
    ("Blank Space","Taylor Swift"),
    ("Someone Like You","Adele"),
    ("Hello","Adele"),
    ("Halo","Beyoncé"),
    ("Crazy in Love","Beyoncé"),
    ("Super Bass","Nicki Minaj"),
    ("Starships","Nicki Minaj"),
    ("Blinding Lights","The Weeknd"),
    ("Levitating","Dua Lipa")
]

features = ["Energy","Danceability","Acousticness","Tempo","Popularity"]

# YOUTUBE PLAY
def play_song(name, artist):
    results = yt.search(f"{name} {artist}", filter="songs")
    if results:
        url = "https://www.youtube.com/watch?v=" + results[0]['videoId']
        webbrowser.open(url)

# COSINE SIMILARITY
def cosine(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

# USER INPUT
print("\nEnter values between 0 and 1:\n")
user = np.array([float(input(f"{f}: ")) for f in features])

# SIMILARITY
scores = [cosine(user, s) for s in songs]

# TOP 3
top = np.argsort(scores)[::-1][:3]

print("\nTop 3 Recommendations:\n")
for i, idx in enumerate(top):
    name, artist = song_details[idx]
    print(f"{i+1}. {name} - {artist} ({scores[idx]:.3f})")

# CHOICE
choice = int(input("\nChoose (1-3): "))
name, artist = song_details[top[choice-1]]

print(f"\nPlaying: {name} - {artist}")
play_song(name, artist)
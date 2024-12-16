import tkinter as tk
from tkinter import messagebox, filedialog
import json

class Song:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} min) - {self.genre}"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        self.songs = [song for song in self.songs if song.title != title]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump({"name": self.name, "songs": [song.__dict__ for song in self.songs]}, f)

   
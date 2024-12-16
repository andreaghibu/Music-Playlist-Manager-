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
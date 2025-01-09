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

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            playlist = Playlist(data['name'])
            playlist.songs = [Song(**song) for song in data['songs']]
            return playlist

class MusicPlaylistApp:
    def __init__(self, root):
        self.playlist = Playlist("My Playlist")
        self.setup_ui(root)

    def setup_ui(self, root):
        root.title("Music Playlist Manager")

        # Input fields
        for i, text in enumerate(["Song Title:", "Artist:", "Duration:", "Genre:"]):
            tk.Label(root, text=text).grid(row=i, column=0)
        self.entries = [tk.Entry(root, width=30) for _ in range(4)]
        for i, entry in enumerate(self.entries):
            entry.grid(row=i, column=1)

        # Buttons
        tk.Button(root, text="Add Song", command=self.add_song).grid(row=4, column=0, pady=5)
        tk.Button(root, text="Remove Song", command=self.remove_song).grid(row=4, column=1, pady=5)
        tk.Button(root, text="Save Playlist", command=self.save_playlist).grid(row=5, column=0, pady=5)
        tk.Button(root, text="Load Playlist", command=self.load_playlist).grid(row=5, column=1, pady=5)

        # Playlist display
        self.playlist_display = tk.Listbox(root, width=50, height=15)
        self.playlist_display.grid(row=6, column=0, columnspan=2, pady=10)

    def add_song(self):
        values = [entry.get() for entry in self.entries]
        if all(values):
            try:
                self.playlist.add_song(Song(values[0], values[1], float(values[2]), values[3]))
                self.update_playlist_display()
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Invalid Input", "Duration must be a number.")
        else:
            messagebox.showerror("Missing Information", "Please fill in all fields.")

    def remove_song(self):
        selected = self.playlist_display.curselection()
        if selected:
            self.playlist.remove_song(self.playlist_display.get(selected).split(" by ")[0])
            self.update_playlist_display()
        else:
            messagebox.showerror("Selection Error", "Please select a song to remove.")

    def save_playlist(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            self.playlist.save_to_file(filename)
            messagebox.showinfo("Success", "Playlist saved successfully.")

    def load_playlist(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            self.playlist = Playlist.load_from_file(filename)
            self.update_playlist_display()

    def update_playlist_display(self):
        self.playlist_display.delete(0, tk.END)
        for song in self.playlist.songs:
            self.playlist_display.insert(tk.END, str(song))

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlaylistApp(root)
    root.mainloop()

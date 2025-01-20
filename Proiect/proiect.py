import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
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

    def find_song(self, title):
        for song in self.songs:
            if song.title == title:
                return song
        return None

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
        self.selected_song = None
        self.setup_ui(root)

    def setup_ui(self, root):
        root.title("Music Playlist Manager")
        root.configure(bg="lightblue")

        for i, text in enumerate(["Song Title:", "Artist:", "Duration:", "Genre:"]):
            tk.Label(root, text=text, bg="beige", fg="black").grid(row=i, column=0, padx=10, pady=5)
        self.entries = [tk.Entry(root, width=30) for _ in range(4)]
        for i, entry in enumerate(self.entries):
            entry.grid(row=i, column=1, padx=10, pady=5)

        button_styles = {
            "bg": "lightpink",
            "fg": "black",
            "activebackground": "green",
            "activeforeground": "black"
        }
        tk.Button(root, text="Add Song", command=self.add_song, **button_styles).grid(row=4, column=0, pady=5, padx=10)
        tk.Button(root, text="Remove Song", command=self.remove_song, **button_styles).grid(row=4, column=1, pady=5, padx=10)
        tk.Button(root, text="Save Playlist", command=self.save_playlist, **button_styles).grid(row=5, column=0, pady=5, padx=10)
        tk.Button(root, text="Load Playlist", command=self.load_playlist, **button_styles).grid(row=5, column=1, pady=5, padx=10)
        tk.Button(root, text="Edit Song", command=self.edit_song, **button_styles).grid(row=6, column=0, pady=5, padx=10)

        self.canvas = tk.Canvas(root, width=600, height=300, bg="black", highlightthickness=0)
        self.canvas.grid(row=7, column=0, columnspan=3, pady=10, padx=10)


        self.bg_image = Image.open("Imagine muzica.jpg")
        self.bg_image = self.bg_image.resize((600, 300), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)

        self.text_items = []

        self.canvas.bind("<Button-1>", self.on_song_click)

    def add_song(self):
        values = [entry.get() for entry in self.entries]
        if all(values):
            try:
                song = Song(values[0], values[1], float(values[2]), values[3])
                self.playlist.add_song(song)
                self.update_playlist_display()
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Invalid Input", "Duration must be a number.")
        else:
            messagebox.showerror("Missing Information", "Please fill in all fields.")

    def remove_song(self):
        if self.selected_song:
            self.playlist.remove_song(self.selected_song)
            self.selected_song = None
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

    def edit_song(self):
        if self.selected_song:
            song = self.playlist.find_song(self.selected_song)
            if song:
                self.entries[0].delete(0, tk.END)
                self.entries[0].insert(0, song.title)
                self.entries[1].delete(0, tk.END)
                self.entries[1].insert(0, song.artist)
                self.entries[2].delete(0, tk.END)
                self.entries[2].insert(0, song.duration)
                self.entries[3].delete(0, tk.END)
                self.entries[3].insert(0, song.genre)

                self.playlist.remove_song(song.title)
            else:
                messagebox.showerror("Error", "Selected song not found.")
        else:
            messagebox.showerror("Selection Error", "Please select a song to edit.")

    def on_song_click(self, event):
        for text_item in self.text_items:
            bbox = self.canvas.bbox(text_item)
            if bbox and bbox[0] <= event.x <= bbox[2] and bbox[1] <= event.y <= bbox[3]:
                self.selected_song = self.canvas.itemcget(text_item, "text").split(" by ")[0]
                break

    def update_playlist_display(self):
        for item in self.text_items:
            self.canvas.delete(item)
        self.text_items = []

        for i, song in enumerate(self.playlist.songs):
            text_item = self.canvas.create_text(
                10, 20 + i * 30,
                anchor="nw",
                text=str(song),
                fill="white",
                font=("Arial", 12)
            )
            self.text_items.append(text_item)

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlaylistApp(root)
    root.mainloop()

# Manager de Playlist-uri Muzicale 🎵

Aceasta este o aplicație bazată pe Python pentru gestionarea unui playlist muzical. Poți adăuga, elimina, edita melodii și salva/încărca playlist-uri în/din fișiere JSON. Aplicația include o interfață grafică interactivă construită cu **Tkinter** și suportă afișarea unei imagini de fundal utilizând **Pillow**.

---
## O scurta descriere a proiectului 
- Este o aplicație Python cu o interfață grafică (GUI) pentru gestionarea playlist-urilor muzicale 
- Permite utilizatorilor să adauge, editeze, elimine, salveze și să încarce melodii într-un playlist.
- Aplicația utilizează biblioteca tkinter pentru interfața sa și integrează manipularea fișierelor JSON pentru stocarea datelor despre playlist.

## Funcționalități
- **Adăugare melodii:** Introduceți titlul, artistul, durata și genul pentru a adăuga o melodie nouă.
- **Eliminare melodii:** Selectați o melodie din playlist pentru a o elimina.
- **Editare melodii:** Modificați detaliile unei melodii existente.
- **Salvare playlist:** Salvați playlist-ul într-un fișier `.json`.
- **Încărcare playlist:** Încărcați un playlist existent dintr-un fișier `.json`.
- **Interfață interactivă:** Faceți clic pe melodiile afișate peste imaginea de fundal pentru a le selecta.

---

## Biblioteci Utilizate
Următoarele biblioteci sunt utilizate în acest proiect:
1. **tkinter** (inclus în Python): Folosit pentru crearea interfeței grafice.
   - `messagebox`: Pentru afișarea alertelor și mesajelor de eroare.
   - `filedialog`: Pentru selectarea fișierelor (salvare/încărcare).
2. **Pillow (PIL):** Folosit pentru încărcarea și manipularea imaginii de fundal.
3. **json** (inclus în Python): Pentru salvarea și încărcarea datelor din playlist în format JSON.


---
## Prezentare Generală a Claselor

1. Clasa Song
Reprezintă o melodie cu următoarele atribute:
title: Titlul melodiei.
artist: Numele artistului.
duration: Durata în minute (float).
genre: Genul melodiei.

2. Playlist
Gestionează o listă de melodii cu metode pentru:
Adăugare și ștergere melodii.
Găsirea unei melodii specifice după titlu.
Salvarea și încărcarea playlist-urilor din fișiere JSON.

3. MusicPlaylistApp
Definește interfața grafică și integrează funcționalitatea playlist-ului. 
Metode cheie includ: add_song: Adaugă o melodie în playlist.
remove_song: Elimină melodia selectată.
save_playlist: Salvează playlist-ul curent într-un fișier.
load_playlist: Încarcă un playlist dintr-un fișier.
edit_song: Editează detaliile melodiei selectate.
update_playlist_display: Actualizează canvas-ul pentru a reflecta playlist-ul curent.



## Cum să rulezi programul 
1. Clonează sau descarcă proiectul.
2. Plasează imaginea de fundal (Imagine muzica.jpg) în același director cu scriptul.
3. Rulează scriptul Python:
   python script_name.py

4. Interacționează cu interfața grafică pentru a gestiona playlist-ul.



## Cum functioneaza programul 
1.Interfață Grafică:
Interfața principală include câmpuri de text pentru detaliile melodiilor, butoane pentru acțiuni (adăugare, editare, ștergere, salvare, încărcare) și un canvas pentru afișarea playlist-ului.
Melodiile sunt listate pe canvas, unde utilizatorii pot face clic pe ele pentru a le selecta.

2.Stocarea Datelor:
Playlist-urile sunt stocate în format JSON, ceea ce le face ușor de salvat și încărcat.
Fiecare melodie este reprezentată ca un dicționar, iar playlist-ul conține metadate despre numele său și lista de melodii.

3.Gestionarea Evenimentelor:
Butoanele și clicurile pe canvas sunt legate de funcții care procesează acțiunile utilizatorilor, cum ar fi adăugarea sau eliminarea melodiilor.

4.Validare:
Câmpurile de intrare sunt validate pentru a asigura integritatea datelor (de exemplu, durata trebuie să fie un număr).

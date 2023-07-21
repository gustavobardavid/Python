 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

temp_song = ()


def addsongs():
    global temp_song
    
    temp_song = filedialog.askopenfilenames(initialdir="C:/Users/Gustavo/python-mp3-music-player/Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))

    for s in temp_song:
        s = s.replace("C:/Users/Gustavo/python-mp3-music-player/", "")
        songs_list.insert(END, s)

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/Gustavo/python-mp3-music-player/{song}'
    mixer.music.load(song)
    mixer.music.play()

root = Tk()
root.title('Bardavid Python MP3 Music player App ')
mixer.init()

songs_list = Listbox(root, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15), height=12, width=47, selectbackground="red", selectforeground="white")
songs_list.grid(columnspan=9)

defined_font = font.Font(family='Helvetica')

play_button = Button(root, text="Tocar", width=7, command=Play)
play_button['font'] = defined_font
play_button.grid(row=1, column=0)

my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Adicionar msc", command=addsongs)
add_song_menu.add_command(label="Apagar msc", command=deletesong)

mainloop()
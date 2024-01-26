import tkinter
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "true"
import pygame
import re

pygame.mixer.init()
window = tkinter.Tk()
window.title("ZDMusic")
window.geometry("300x300")
tkinter.Label(text="ZDMusic",font=("Arial", "35")).pack()
songs = []
def playsong(song):
   for songfile in os.listdir("music"):
       if re.match(song + "*", songfile):
           pygame.mixer.music.load(os.path.join("music", songfile))
           pygame.mixer.music.play()
           break
for song in os.listdir("music"):
    if not song.startswith("."):
        songs.append(os.path.splitext(song)[0])
selection = tkinter.OptionMenu(window, tkinter.StringVar(window, "Select a Song"), *songs, command=playsong)
selection.pack()
tkinter.Button(text="Stop Music", command=pygame.mixer.music.stop, bg="red", fg="white").pack()
tkinter.mainloop()
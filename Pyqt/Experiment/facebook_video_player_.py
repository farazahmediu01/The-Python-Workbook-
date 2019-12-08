import tkinter as tk
from Pil import ImageTk,Image
import imageio
from os import path,remove
import subprocess
from pygame import mixer
mixer.init()

class Player(tk.Label):
    def __init__(self,master,label,vidname):
        tk.Label.__init__(self, master=None)
        self.root = master
        self.label = label
        self.videoname = vidname
        self.video = imageio.get_reader(self.videoname)


        self.delay = int(1000/self.video.get_meta_data()['fps'])
        self.videosize = self.video.get_meta_data()['source_size']
        self.image_data = 0
        self.audio()
        self.play()


    def play(self):
        try:
            self.image_data = self.video.get_next_data()
        except Exception:
            self.video.close()
            self.label.destroy()
            remove('extract.mp3')
        else:
            self.label.after(self.delay,lambda :self.play())
            framme_img = ImageTk.PhotoImage(Image.fromarray(self.image_data))
            self.label.config(image=framme_img)
            self.label.image = framme_img
            self.root.geometry(f"{self.videosize[0]}x{self.videosize[1]}")
            self.label.place(x=0,y=0)
            self.root.resizable(width=False,height=False)


    def audio(self):
        if path.isfile('extract.mp3'): remove('extract.mp3')
        command = f"ffmpeg -i {self.videoname} -ab 160k -ac 2 -ar 44100 -vn extract.mp3"
        subprocess.call(command,shell=True)
        mixer.music.load('extract.mp3')
        mixer.music.play()

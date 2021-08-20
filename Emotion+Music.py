import tkinter as tk
from tkinter import *
from EmotionRecognition import Emotion

track = Emotion()

class Application(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Emotion=Music")

        self.start = Button(self)
        self.start["text"] = "Start video capture"
        self.start["command"] = track.startCapture
        self.start.pack({"side": "left"})

        self.stop = Button(self)
        self.stop["text"] = "Stop video capture"
        self.start["command"] = track.capture.release()
        self.stop.pack({"side": "right"})

Application().mainloop()

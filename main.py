# main.py
import core.config

from gui.window import ReelAutoApp
from moviepy.config import change_settings
import tkinter as tk



change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"})
print("Launching the app...")

root = tk.Tk()
app = ReelAutoApp(root)

print("App launched.")
root.mainloop()

print("Exited main loop.")

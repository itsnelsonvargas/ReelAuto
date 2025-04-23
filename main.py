import os
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from dotenv import load_dotenv

# Ensure ImageMagick path is correctly set
os.environ['IMAGEMAGICK_BINARY'] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

import core.config  # safe to import here
import tkinter as tk  # safe

print("✅ ImageMagick path set to:", r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe")

from gui.window import ReelAutoApp  # must come AFTER setting the env var

print("Launching the app...")

root = tk.Tk()
app = ReelAutoApp(root)

print("App launched.")
root.mainloop()

print("Exited main loop.")

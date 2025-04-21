# main.py
from moviepy.config import change_settings

# ✅ Set ImageMagick path BEFORE any MoviePy usage
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"
})

import core.config  # safe
import tkinter as tk  # safe

print("✅ ImageMagick path set to:", r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe")

from gui.window import ReelAutoApp  # must come AFTER change_settings

print("Launching the app...")

root = tk.Tk()
app = ReelAutoApp(root)

print("App launched.")
root.mainloop()

print("Exited main loop.")

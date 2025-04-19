# main.py
from gui.window import ReelAutoApp
import tkinter as tk

print("Launching the app...")

root = tk.Tk()
app = ReelAutoApp(root)

print("App launched.")
root.mainloop()

print("Exited main loop.")

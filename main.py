import tkinter as tk
import ctypes
import sys


def display_on():
    global root
    print("Always On")
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    root.iconify()


def display_reset():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    sys.exit(0)


root = tk.Tk()
root.geometry("150x20")
root.title("Display App")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Quit",
                   fg="red",
                   command=display_reset)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Always ON",
                   command=display_on)
slogan.pack(side=tk.LEFT)

root.mainloop()
import tkinter as tk
from tkinter import filedialog
import os
import webbrowser

window = tk.Tk()
window.title("Quill")
window.geometry("800x600")

menuBar = tk.Menu(window)
window.config(menu=menuBar)
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

textWidget = tk.Text(window, wrap="word")
textWidget.pack(expand="yes", fill="both")

def start_screen():
    titleLabel = tk.Label(window, text="Quill", font=("Helvetica", 36))
    subtitleLabel = tk.Label(window, text="Unbloated text editor", font=("Helvetica", 18))
    createButton = tk.Button(window, text="Create", command=create_new)
    openButton = tk.Button(window, text="Open", command=open_file)
    sourceButton = tk.Button(window, text="Source", command=open_source)

def open_file():
    filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        with open(filePath, 'r') as file:
            fileContents = file.read()
            textWidget.delete(1.0, "end")
            textWidget.insert("1.0", fileContents)

def save_file():
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        with open(filePath, 'w') as file:
            fileContents = textWidget.get("1.0", "end-1c")
            file.write(fileContents)

def create_new():
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

def exit_app():
    window.quit()

fileMenu.add_command(label="New", command=create_new)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit_app)

window.mainloop()

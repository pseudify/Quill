import tkinter as tk
from tkinter import filedialog
import webbrowser

window = tk.Tk()
window.title("Quill")
window.geometry("800x600")

menuBar = tk.Menu(window)
window.config(menu=menuBar)
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

textWidget = None
title_frame = None
createButton = None
openButton = None
sourceButton = None

def create_text_widget():
    global textWidget
    textWidget = tk.Text(window, wrap="word")
    textWidget.grid(row=5, column=0, columnspan=3, sticky="nsew")
    textWidget.config(state="normal")

def remove_title_screen():
    global title_frame, createButton, openButton, sourceButton
    if title_frame:
        title_frame.destroy()
        createButton.destroy()
        openButton.destroy()
        sourceButton.destroy()

def open_source():
    github_url = "https://github.com/pseudify/Quill/"
    webbrowser.open(github_url)

def open_file():
    filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        create_text_widget()
        remove_title_screen()
        textWidget.config(state="normal")
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
    if filePath:
        create_text_widget()
        remove_title_screen()
        textWidget.config(state="normal")
        textWidget.delete(1.0, "end")

def exit_app():
    window.quit()

title_frame = tk.Frame(window)
title_frame.grid(row=0, column=0, columnspan=3)

titleLabel = tk.Label(title_frame, text="Quill", font=("Helvetica", 36))
titleLabel.grid(row=0, column=0, columnspan=3, pady=(50, 0))

subtitleLabel = tk.Label(title_frame, text="Unbloated Text Editor", font=("Helvetica", 18))
subtitleLabel.grid(row=1, column=0, columnspan=3)

createButton = tk.Button(window, text="Create", command=create_new)
createButton.grid(row=2, column=1, pady=(20, 0))

openButton = tk.Button(window, text="Open", command=open_file)
openButton.grid(row=3, column=1, pady=(20, 0))

sourceButton = tk.Button(window, text="Source", command=open_source)
sourceButton.grid(row=4, column=1, pady=(20, 0))

window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(1, weight=1)

def open_menu():
    open_file()

def save_menu():
    save_file()

def exit_menu():
    exit_app()

fileMenu.add_command(label="Open", command=open_menu)
fileMenu.add_command(label="Save", command=save_menu)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit_menu)

window.mainloop()

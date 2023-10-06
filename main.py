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
titleFrame = None
createButton = None
openButton = None
sourceButton = None

def createTextWidget():
    global textWidget
    textWidget = tk.Text(window, wrap="word")
    textWidget.grid(row=5, column=0, columnspan=3, sticky="nsew")
    textWidget.config(state="normal")

def removeTitleScreen():
    global titleFrame, createButton, openButton, sourceButton
    if titleFrame:
        titleFrame.destroy()
        createButton.destroy()
        openButton.destroy()
        sourceButton.destroy()

def openSource():
    githubUrl = "https://github.com/pseudify/Quill/"
    webbrowser.open(githubUrl)

def openFile():
    filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        createTextWidget()
        removeTitleScreen()
        textWidget.config(state="normal")
        with open(filePath, 'r') as file:
            fileContents = file.read()
            textWidget.delete(1.0, "end")
            textWidget.insert("1.0", fileContents)

def saveFile():
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        with open(filePath, 'w') as file:
            fileContents = textWidget.get("1.0", "end-1c")
            file.write(fileContents)

def createNew():
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        createTextWidget()
        removeTitleScreen()
        textWidget.config(state="normal")
        textWidget.delete(1.0, "end")

def exitApp():
    window.quit()

titleFrame = tk.Frame(window)
titleFrame.grid(row=0, column=0, columnspan=3)

titleLabel = tk.Label(titleFrame, text="Quill", font=("Helvetica", 36))
titleLabel.grid(row=0, column=0, columnspan=3, pady=(50, 0))

subtitleLabel = tk.Label(titleFrame, text="Unbloated Text Editor", font=("Helvetica", 18))
subtitleLabel.grid(row=1, column=0, columnspan=3)

createButton = tk.Button(window, text="Create", command=createNew)
createButton.grid(row=2, column=1, pady=(20, 0))

openButton = tk.Button(window, text="Open", command=openFile)
openButton.grid(row=3, column=1, pady=(20, 0))

sourceButton = tk.Button(window, text="Source", command=openSource)
sourceButton.grid(row=4, column=1, pady=(20, 0))

window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(1, weight=1)

def openMenu():
    openFile()

def saveMenu():
    saveFile()

def exitMenu():
    exitApp()

fileMenu.add_command(label="Open", command=openMenu)
fileMenu.add_command(label="Save", command=saveMenu)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitMenu)

window.mainloop()

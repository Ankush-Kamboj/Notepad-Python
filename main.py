import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Note():
    cilpboard = ""

    def __init__(self):
        self.initUI()

    def initUI(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Untitled - Notepad")
        print(__file__)
        # Menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menu bar - File
        file_menu = tk.Menu(menu_bar, tearoff = 0)
        file_menu.add_command(label= "New", command= self.newFile)
        file_menu.add_command(label= "New Window", command= self.newWindow)
        file_menu.add_command(label= "Open...", command= self.openFile)
        file_menu.add_command(label= "Save", command=self.saveFile)
        file_menu.add_command(label= "Save As...", command=self.saveAs)
        file_menu.add_separator()
        file_menu.add_command(label= "Exit", command = self.exit)

        # Menu bar - Edit
        edit_menu = tk.Menu(menu_bar, tearoff = 0)
        edit_menu.add_command(label= "Undo", command=self.undo)
        edit_menu.add_command(label= "Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label= "Cut", command=self.cut)
        edit_menu.add_command(label= "Copy", command=self.copy)
        edit_menu.add_command(label= "Paste", command=self.paste)

        # Menu bar - Format
        format_menu = tk.Menu(menu_bar, tearoff = 0)
        format_menu.add_command(label= "Font", command=self.undo)

        # Adding all the menus to Menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Text input box
        self.textbox = tk.Text(self.root, undo=True, maxundo=-1)
        self.textbox.pack(expand=True, fill='both')
        
    # To open a new file
    def newFile(self):
        self.textbox.edit_reset()
        self.textbox.delete('1.0',tk.END)
    
    # To open a new Window
    def newWindow(self):
        self.textbox.edit_reset()
        self.initUI()

    # To open an existing file
    def openFile(self):
        self.file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes = [("txt files","*.txt")])
        with open(self.file) as f:
            file_content = f.read()
            f.close()
        self.textbox.insert(tk.END, file_content)
        self.root.title(self.file + " - Notepad")
    
    # To save the current file
    def saveFile(self):
        if self.root.title() == "Untitled - Notepad":
            self.saveAs()
        else:
            with open(self.file, "w") as f:
                f.write(self.textbox.get("1.0",tk.END))
                f.close()
    
    # To save as a new file
    def saveAs(self):
        fname = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save As", filetypes = [("Text Document","*.txt")])
        with open(fname + ".txt", "w") as f:
            f.write(self.textbox.get("1.0",tk.END))
            f.close()

    # The classic Cut operation
    def cut(self):
        try:
            self.cilpboard = self.textbox.selection_get()
            self.textbox.delete("sel.first", "sel.last")
        except:
            self.cilpboard=""
        
    # The classic Copy operation 
    def copy(self):
        try:
            self.cilpboard = self.textbox.selection_get()
        except:
            self.cilpboard=""

    # The classic Paste operation
    def paste(self):
        try:
            selection = self.textbox.selection_get()
        except:
            selection = ""

        if selection:
            self.textbox.delete("sel.first", "sel.last")
        current = self.textbox.index(tk.INSERT)
        self.textbox.insert(current, self.cilpboard)
    
    # Undo Operation
    def undo(self):
        try:
            self.textbox.edit_undo()
        except:
            pass

    # Redo Operation
    def redo(self):
        try:
            self.textbox.edit_redo()
        except:
            pass

    def exit(self):
        message = messagebox.askyesnocancel("Notepad", "Do you want to exit")
        if message:
            self.root.quit()

    def showDialog(self):
        self.root.mainloop()


if __name__ == "__main__":
    Note().showDialog()
# Video Tutorial: https://youtu.be/A_Sfru99QNA?si=WmT1EQJce5T0gONx
# Credited: https://hacker.io/blog/python-projects
# Status Bar: https://dev.to/emilossola/building-a-text-editor-gui-with-tkinter-in-python-19l

import tkinter as tk
import textwrap
from tkinter.filedialog import askopenfilename, asksaveasfilename

def new_file():
    pass

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    # Line, Character Delete position
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")
    
def main():
    window = tk.Tk()
    # Window Title
    window.title("Text Editor by GrantsGaming1") 
    window.rowconfigure(1, minsize=300)
    window.columnconfigure(0, minsize=300)
    window.iconphoto(False, tk.PhotoImage(file="TextEditorPython\grantsgamingyt2023aprofilepic.png"))
    
    # Text Editing Widget
    text_edit = tk.Text(window, font="Helvetica 16", background="black", foreground="White")
    
   
    # Render on Screen
    text_edit.grid(row=1, column=0)
        
    # Place Buttons
    # lambda: Defines function
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    new_button = tk.Button(frame, text="New")
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    
    # Render (Sticky expands buttons)
    new_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    open_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    # NS (Sticky = North Side, South Side)
    frame.grid(row=0, column=0, sticky="nw")
    
    # Keyboard Shortcuts
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    
    
    window.mainloop()
    
main()
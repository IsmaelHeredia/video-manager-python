#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Video Manager GUI 1.0
# Written by Ismael Heredia
# pip install pyperclip

import win32gui, win32con
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import scrolledtext 
import pyperclip
import subprocess
import threading
import sys

win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)

logs = []

def update_logs():
    while len(logs) != 0:
        txtConsole.insert("end", logs.pop(0))
    txtConsole.after(100, update_logs)

def executeThread():

    link = txtLink.get()
    output_name = txtOutputName.get()
    output_folder = txtOutputFolder.get()
    option = vo.get()

    option_string = ""

    if option == "1":
        option_string = "-download-video "
    else:
        option_string = "-download-song "

    cmd = "video.py " + option_string + "\"" + link + "\""

    if output_name != "":
        cmd = cmd + " -output-name " + "\"" + output_name + "\""

    if output_folder != "":
        cmd = cmd + " -output-folder " + "\"" + output_folder + "\""

    #print(cmd)

    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            txtConsole.insert(END, line)
            txtConsole.see(END)
        txtConsole.configure(state="disabled")
        messagebox.showinfo(title = "Result", message = "Process Executed")

def clearForm():
    txtLink.delete(0, END)
    txtOutputName.delete(0, END)
    txtOutputFolder.delete(0, END)
    txtConsole.configure(state="normal")
    txtConsole.delete("1.0", END)
    txtConsole.configure(state="disabled")
    vo.set(1)

def executeScript():
    if txtLink.get() == "":
        messagebox.showwarning(title = "App", message = "You must insert the link to download")
    else:
        txtConsole.configure(state="normal")
        txtConsole.delete("1.0", END)
        txtConsole.insert(END, "[+] Executing ...\n\n")
        txtConsole.see(END)
        new_thread = threading.Thread(target=executeThread, daemon=True)
        new_thread.start()
     
def showAbout():
    messagebox.showinfo(title = "About", message = "Written by Ismael Heredia")

def closeApp():
    sys.exit(1)

if __name__ == "__main__" : 

    link_value = ""

    data = pyperclip.paste()

    if data.startswith("https://") or data.startswith("http://"):
        link_value = data
   
    background_color = "#002B36"
    foreground_color = "#FFFFFF"
    active_color = "#002B36"

    root = Tk()
   
    root.configure(background = background_color) 
   
    root.geometry("460x460") 

    fontApp = tkFont.Font(family="Helvetica", size = 10, weight = "bold")
   
    root.title("Video Manager GUI 1.0")
       
    lblLink = Label(root, text = "Link : ", fg = foreground_color, bg = background_color, font = fontApp) 
    lblOutputName = Label(root, text = "Output name : ", fg = foreground_color, bg = background_color, font = fontApp) 
    lblOutputFolder = Label(root, text = "Output folder : ", fg = foreground_color, bg = background_color, font = fontApp)
  
    lblLink.place(x = 10, y = 10)  
    lblOutputName.place(x = 10, y = 40)  
    lblOutputFolder.place(x = 10, y = 70)

    vl = StringVar(root, value = link_value)
 
    txtLink = Entry(root, width = 48, fg = foreground_color, bg = background_color, insertbackground = foreground_color, font = fontApp, textvariable = vl)  
    txtOutputName = Entry(root, width = 48, fg = foreground_color, bg = background_color, insertbackground = foreground_color, font = fontApp)  
    txtOutputFolder = Entry(root, width = 48, fg = foreground_color, bg = background_color, insertbackground = foreground_color, font = fontApp)
      
    txtLink.place(x = 110, y = 10)  
    txtOutputName.place(x = 110, y = 40)  
    txtOutputFolder.place(x = 110, y = 70)

    lblOption = Label(root, text = "Option : ", fg = foreground_color, bg = background_color, font = fontApp)  
    lblOption.place(x = 10, y = 100)  

    vo = StringVar(root, "1")
    Radiobutton(root, text = "Video", padx = 5, variable = vo, value = 1, fg = foreground_color, bg = background_color, highlightbackground = active_color, activebackground = active_color, selectcolor = background_color, font = fontApp).place(x = 110, y = 100)  
    Radiobutton(root, text = "Song", padx = 20, variable = vo, value = 2, fg = foreground_color, bg = background_color, highlightbackground = active_color, activebackground = active_color, selectcolor = background_color, font = fontApp).place(x = 190, y = 100)  

    lblConsole = Label(root, text = "Console", fg = foreground_color, bg = background_color, font = fontApp) 
    lblConsole.place(x = 190, y = 160)

    txtConsole = scrolledtext.ScrolledText(root, wrap = WORD, width= 52, height = 10, fg = foreground_color, bg = background_color, insertbackground = foreground_color, state="disabled")
    txtConsole.place(x = 10, y = 200)
 
    btnExecute = Button(root, width = 9, text = "Execute", bg = background_color, fg = foreground_color, highlightbackground = active_color, activebackground = active_color, activeforeground = foreground_color, font = fontApp, command = executeScript) 
    btnClear = Button(root, width = 9, text = "Clear", bg = background_color, fg = foreground_color, highlightbackground = active_color, activebackground = active_color, activeforeground = foreground_color, font = fontApp, command = clearForm)
    btnAbout = Button(root, width = 9, text = "About", bg = background_color, fg = foreground_color, highlightbackground = active_color, activebackground = active_color, activeforeground = foreground_color, font = fontApp, command = showAbout)
    btnExit = Button(root, width = 9, text = "Exit", bg = background_color, fg = foreground_color, highlightbackground = active_color, activebackground = active_color, activeforeground = foreground_color, font = fontApp, command = closeApp)

    btnExecute.place(x = 53, y = 400) 
    btnClear.place(x = 143, y = 400)
    btnAbout.place(x = 233, y = 400)
    btnExit.place(x = 325, y = 400)
 
    root.resizable(False,False)

    update_logs()

    root.mainloop()
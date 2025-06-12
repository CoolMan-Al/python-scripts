from subprocess import run
from tkinter import Tk, font, Frame
from tkinter.ttk import Button, Label
from PIL import Image, ImageTk
from datetime import datetime


def confirmStop():
    # Window
    stopWindow = Tk()
    stopWindow.geometry('300x100')
    stopWindow.title("Exit Service?")

    # Frames
    stopPanel = Frame(stopWindow, relief='flat', bd=1)
    stopPanel.place(x=20, y=55)

    # Content
    stop_label = Label(stopWindow, text="Are you sure you want to stop the program? \n The device will stop collecting data!")
    stop_label.pack(side='top')

    exitYes = Button(stopPanel,text="Confirm Exit", command=stopService)
    exitYes.pack(side='right', padx=15)

    exitNo = Button(stopPanel, text="Back to Application", command=stopWindow.destroy)
    exitNo.pack(side='left', padx=15)

    # Execute
    stopWindow.mainloop()


def stopService():
    quit()


def update():
    date.configure(text="Date: " + str(datetime.now())[0:-16])
    time.configure(text="Time: " + str(datetime.now())[11:-7])
    window.after(1000, update)


if __name__ == "__main__": 
    # Window
    window = Tk()
    window.title("Graphical User Interface")
    window.geometry('800x480')

    # Options
    window.defaultFont = font.nametofont("TkDefaultFont")
    window.defaultFont.configure(family = "Courier",
                                size = 32,
                                weight = font.BOLD)

    # External

    # Frames
    detail = Frame(window, relief='flat', bd=1)
    detail.place(x=0,y=0)
    
    # Content
    title = Label(detail, text="Team Project", font=("Courier", 64, 'bold'), compound='left')
    title.pack(side='top')
        
    date = Label(detail, text=str(datetime.now())[0:-16])
    date.pack(anchor='w', padx=10, pady=5)
    
    time = Label(detail, text=str(datetime.now())[11:-7])
    time.pack(anchor='w', padx=10, pady=5)

    exit_button = Button(detail, text="Exit", command=confirmStop)
    exit_button.pack(side='left', padx=10, pady=0)
    
    # Final
    window.protocol("WM_DELETE_WINDOW", confirmStop)
    update()
    window.mainloop()

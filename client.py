import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTK,Image
SERVER = None
PORT = 6000
IP_ADDRESS = '127.0.0.1'




def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    #sending message to server
    SERVER.send(playerName.encode())
    

def askPlayerName() :
    global playerName
    global nameEntry 
    global namewindow
    global canvas1

    nameWindow = Tk()
    nameWindow.title('Tanbola Family Fun')
    nameWindow.geometry ( '800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTK.PhotoImage(file ="./assets/background.png")
    canvas1 = Canvas( nameWindow,width =500 ,height = 580)
    canvas1. pack(fill = "both", expand =True)

    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text(screen_width/4.5, screen_height/8,text = "Enter Name", font=( "Chalkboard SE",68), fill="black")
    nameEntry = Entry(nameWindow, width=15, justify='center', font=("Chalkboard SE", 38), bd=5, fill="white")
    nameEntry.place(x = screen_width/7, y=screen_height/5.5 )
    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 38),width=11, command=saveName, height=2, bg="white", bd=3) 
    button.place(x = screen_width/6, y=screen_height/4)
    nameWindow.resizable( True, True)
    nameWindow.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    #thread = Thread(target=recivedMsg)
    #thread.start
    
    askPlayerName()


  
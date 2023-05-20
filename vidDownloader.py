import tkinter as tk
from tkinter import *
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

myPath = "C:\\Users\\Acer\\Downloads\\Downloaded Files" #downloaded files will go here (provide your own)

class methods():
    #Pinaka bwiset na part (Pagod na pagod na'ko)
    #To-do: 1. video&audio option, 2.search bar and results, 3.record history(optional)
    def download():
        link = userIn.get()
        if(link != ""):
            ytV = YouTube(link)
            title = ytV.title
            #Top 2 na pinaka bwiset na part
            if("1" == opt.get()):
                try: 
                    ytV.streams.filter(file_extension='mp4')
                    downloadable = ytV.streams.get_by_resolution("720p")
                    downloadable.download(myPath)
                except VideoUnavailable:
                    print("Video unavailable")
            else:
                try: 
                    ytV.streams.filter(only_audio=True)
                    downloadable = ytV.streams.get_audio_only()
                    downloadable.download(myPath)
                except VideoUnavailable:
                    print("Video unavailable")
            label2.config(text="Download completed")
        else:
             print("Error no Link Found")     

    def add_label():
        label = tk.Label(window, text="New Label")
        label.place(x=50, y=50)

m = methods

if __name__ == "__main__":
    #Gui and widgets placement
    window = tk.Tk()
    window.geometry("300x300")
    window.resizable(width=False, height=False)
    opt = StringVar(window)

    
    radBtn1 = tk.Radiobutton(window, text="Video", variable=opt, value="1")
    radBtn2 = tk.Radiobutton(window, text="Audio_only", variable=opt, value="2")
    label1 = tk.Label(text="Paste link here")
    label2 = tk.Label(text="")
    userIn = tk.Entry(window)
    downloadBtn = tk.Button(window, text="Download",command=m.download)
            
    label1.place(x=20, y=20)
    label2.place(x=10, y=70)
    userIn.place(x=110, y=20)
    downloadBtn.place(x=210, y=250)
    radBtn1.place(x=150, y=40)
    radBtn2.place(x=50, y=40)

    window.mainloop()
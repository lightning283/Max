import wget
from tkinter import *
from pytube import YouTube
import webbrowser
from PIL import Image,ImageTk
from resources import *
import os
if not os.path.exists(f"/home/{user_name}/Desktop/pydown"):
    os.mkdir(f"/home/{user_name}/Desktop/pydown")
pydown_root = Tk()
pydown_root.geometry("172x200")
pydown_root.title("Wget Downloader")
pydown_root.resizable(0, 0)#makes the window un-resizable.
loadimg = Image.open(f'{homedir}/assets/res/2.jpg')
renderimg = ImageTk.PhotoImage(loadimg)
imgpydown = Label(pydown_root,image=renderimg)
imgpydown.place(x= 0, y= 0)
p1 = PhotoImage(file = f'{homedir}/assets/res/icon.png')
pydown_root.iconphoto(False, p1)##
###################################################################
def gui_wget():
    wgetgui = Tk()
    entry1 = Entry(wgetgui,width=25)
    entry1.pack()
    def wgt():
        txt = entry1.get()
        path = '~/Desktop/pydown/'
        wget.download(txt , out=path)

    btn = Button(wgetgui,text="Download", command=wgt).pack()    
    wgetgui.mainloop()
##################################################################
def youtube_download():
    yt = Tk()
    yt.title("YouTube-Video-Downloader")
    ytdd = Entry(yt, width = 30)
    ytdd.pack()
    def ytaudio():
        infodd = ytdd.get()
        youtube_downloaddd = YouTube(infodd)
        stream = youtube_downloaddd.streams.filter(only_audio=True, subtype="webm" , abr='160kbps').first().download('~/Downloads')
    def ddd():
        infodd = ytdd.get()
        youtube_downloaddd = YouTube(infodd).streams.get_highest_resolution().download()
    btn = Button(yt,text="Download-Video",command=ddd).pack()
    btn = Button(yt,text="Download-Audio",command=ytaudio).pack()     
    yt.mainloop()
####################################################################
def youtubeserch():
    yt  = Tk()
    yt.title("YoutubeSearch")

    def ytserch():
        whatlink = bar.get()
        text = ("https://www.youtube.com/results?search_query=" + whatlink)
        webbrowser.open(text)
    bar = Entry(yt, width=30)
    bar.pack()
    btn = Button(yt,text="Search", command=ytserch).pack()    
    yt.mainloop()
##################################################################
def googlesearch():
    gsearch = Tk()
    gsearch.title("GoogleSearch")

    def serch():
        whatlink = bar.get()
        text = ("https://www.google.com/search?q=" + whatlink)
        webbrowser.open(text)
    bar = Entry(gsearch, width=30)
    bar.pack()
    btn = Button(gsearch,text="Search", command=serch).pack()    
    gsearch.mainloop()


###################################################################
button_yt = Button(pydown_root,text="Youtube\ndownload",bg="black" , fg="red" ,command=youtube_download).grid(column=1, row=1)
button_Down = Button(pydown_root,text="wget\ndownload",bg="black", fg="red" ,command=gui_wget).grid(column=2,row=1)
button_Google = Button(pydown_root,text="Google\nsearch", bg="black" , fg="red" , command=googlesearch).grid(column=2,row=2 , sticky="nesw")
button_YoutubeSearch = Button(pydown_root,text="Youtube\nsearch", bg="black" , fg="red", command=youtubeserch).grid(column=1,row=2, sticky="nesw")
pydown_root.mainloop() 

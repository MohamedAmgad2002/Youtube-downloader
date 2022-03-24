# Description : This program download videos and audio from youtube
# Author : Mohamed Amgad
# Version : 1.0
# Date : 24/03/2022


import tkinter
from pytube import YouTube
from tkinter import messagebox,filedialog,font

def main():
    global video
    video = YouTube(link_index.get())
    if decision.get() == 1:
        video.streams.get_highest_resolution().download(output_path=o_path)
        ok_win("video")
    elif decision.get() == 2:
        video.streams.get_audio_only().download(output_path=o_path)
        ok_win("audio")

def ok_win(download):
    prompt = messagebox.showinfo(
        'Confirmation',
        f'The {download} has successfully downloaded!!\nCheck your files.')
    return prompt

def create_path():
    global o_path
    o_path = filedialog.askdirectory(
        parent=screen,
        initialdir="/",
        title='Select a directory')


screen = tkinter.Tk()
screen.geometry("750x250")
screen.title("Youtube Downloader")
link = tkinter.Label(
    screen,
    text="Enter Youtube link",
    font=('Aerial 11'))
link.place(relx=.08, rely=.15, anchor=tkinter.CENTER)
browse_font = font.Font(size=12)

path = tkinter.Label(
    screen,
    text="Were you want to save it",
    font=('Aerial 11'))
path.place(relx=.11, rely=.38, anchor=tkinter.CENTER)

browse_button_f1 = tkinter.Button(
    screen,
    command=create_path,
    text="Browse",
    width="10",
    height="1")
browse_button_f1.place(relx=.29, rely=.38, anchor=tkinter.CENTER)
browse_button_f1['font'] = browse_font

link_index = tkinter.Entry(screen, width=55, font="Helvetica 12 bold")
link_index.place(relx=.50, rely=.15, anchor=tkinter.CENTER)

Download_button = tkinter.Button(
    screen,
    command=main,
    text="Download",
    width="20",
    height="2"
    , bg='#FF0000', 
    fg='#ffffff',
    font="Helvetica 12 bold")
Download_button.place(relx=.45, rely=.8, anchor=tkinter.CENTER)

decision = tkinter.IntVar()

choice1 = tkinter.Checkbutton(screen, text="Video",variable=decision,onvalue=1, offvalue=0,font="Helvetica 12")
choice1.place(relx=.35, rely=.53, anchor=tkinter.CENTER)

choice2 = tkinter.Checkbutton(screen, text="Audio",variable=decision,onvalue=2, offvalue=0,font="Helvetica 12")
choice2.place(relx=.50, rely=.53, anchor=tkinter.CENTER)

screen.mainloop()
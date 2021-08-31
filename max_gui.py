#!/usr/bin/python
import sys
from tkinter import *
from assets.resources import *
# from assets.tasks import *
from datetime import datetime
#########################################################################################
window = Tk()
#########################################################################################
def main():
    # greet()
    try:
        voicerec()
    except sr.UnknownValueError:
        main()
    if "open" in voicerec.text:
        voiceok()
        wfilter("open")
        os.chdir(f"{homedir}/apps/")
        os.system(f"gtk-launch {wfilter.edited_word}.desktop")
    elif ("install" and "package") in voicerec.text:
        voiceok()
        packageinstall()
    elif "time" in voicerec.text:
        now = datetime.now()
        time = now.strftime('%I:%M:%S')
        from gtts import gTTS
        tts = gTTS("Now The Time Is" + time)
        tts.save(f'{voice_dir}/time.mp3')
        playsound(f"{voice_dir}/time.mp3")
    elif "date" in voicerec.text:
        now = datetime.now()
        date = now.strftime('%Y/%m/%d')
        from gtts import gTTS
        tts = gTTS("Today's Date Is" + date)
        tts.save(f'{voice_dir}/date.mp3')
        playsound(f"{voice_dir}/date.mp3")
    elif "launch task" in voicerec.text:
        voiceok()
        os.chdir("tasks/")
        if os.path.isfile("*.sh"):
            wfilter("task")
            os.system("bash {wfilter.edited_word}.sh")
        else:
            playsound(f"{voice_dir}/no_tasks_detected.mp3")
            os.system("bash config.sh")
    elif "add task" in voicerec.text:
        voiceok()
        os.system("bash config.sh")

    elif ("google") or ("google" and "search") in voicerec.text:
        playsound(f"{voice_dir}/what_would_you_like_to_search.mp3")
        voicerec()
        content = voicerec.text
        url_g = f"https://www.google.com/search?q={content}"
        webbrowser.open_new_tab(url_g)
        playsound(f"{voice_dir}/results.mp3")

    elif ("youtube") or ("youtube" and "search") in voicerec.text:
        playsound(f"{voice_dir}/what_would_you_like_to_search.mp3")
        voicerec()
        content = voicerec.text
        url_g = f"https://www.youtube.com/results?search_query={content}"
        webbrowser.open_new_tab(url_g)
        playsound(f"{voice_dir}/results.mp3")
    elif ("shutdown" or "poweroff") or ("shut" and "down") or ("power" and "off") in voicerec.text or "poweroff" in voicerec.text:
        playsound(f"{voice_dir}/poweroff.mp3")
        sleep(10)
        os.system("poweroff")

def exit():
    window.quit()
def debugmode():
    os.system(f"konsole -e python {homedir}max_gui.py")
    
#########################################################################################
photo_mic = PhotoImage(file = f"{homedir}assets/res/mic.png")
photoimage_mic = photo_mic.subsample(3, 3)
Button(window,text = 'Listen', bg="black", fg="green" , command=main,  image = photoimage_mic,compound = LEFT).place(x=50, y=4)
#####################################################
photo = PhotoImage(file = f"{homedir}assets/res/bug.png")
photoimage = photo.subsample(3, 3)
Button(window,text = 'DebugMode', bg="black", fg="green" , command=debugmode ,  image = photoimage,compound = LEFT).place(x=1, y=166)
########################################################
btn = Button(window, text="Exit", bg="black", fg="red", command=exit)
btn.place(x=150, y=170)
#########################################################################################
window.mainloop()

import time
import os
import speech_recognition as sr
from random import random
from datetime import datetime
from resources import *
greet()
def voicerecmain():
    try:
        os.system("pyfiglet -f slant Main Menu")
        voicerec()
        def somethingelse():
            playsound('voices/somethingelse.mp3')
            print("listening..")
            print("say 'yes'")
            voicerec()
            if "yes" in voicerec.text:
                greet()
                voicerecmain()
            else:
                playsound("voices/shutdown.mp3")
                exit()
#########################################################################################
        if "open discord" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch discord.desktop")
            somethingelse()
        elif "open telegram" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch telegram.desktop")
            somethingelse()
        elif "open stremio" in voicerec.text:
            playsound('voices/surething.mp3')
            if not os.path.isfile("/opt/stremio/stremio"):
                playsound("voices/install_pkg.mp3")
                voicerec()
                if "yes" in voicerec.text:
                    playsound("voices/installing_now.mp3")
                    os.system("yay -S aur/stremio")
                else:
                    missedit()
                    voicerecmain()
            else:
                os.system("cd apps && gtk-launch stremio.desktop")
                somethingelse()
        elif "open brave" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch brave.desktop")
            somethingelse()
        elif "open vscode" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch vscode.desktop")
            somethingelse()
        elif "open spotify" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch spotify.desktop")
            somethingelse()
        elif "open konsole" in voicerec.text:
            playsound('voices/surething.mp3')
            os.system("cd apps && gtk-launch konsole.desktop")
            somethingelse()
        elif voicerec.text == "list features":
            clearterm()
            voicesvar("voices/features.mp3")
            os.system("cat assets/features.md")
            done_reading = input("\n\n\nDone Reading? Press Enter")
            somethingelse()
        elif "install" in voicerec.text:
            packageinstall()
        elif "list runnable applications" in voicerec.text:
            voicesvar("voices/options.mp3")
            appliacations()
            done_reading = input("\n\n\nDone Reading? Press Enter")
            somethingelse()
        elif "time" in voicerec.text:
            now = datetime.now()
            time = now.strftime('%I:%M:%S')
            from gtts import gTTS
            tts = gTTS("Now The Time Is" + time)
            tts.save('time.mp3')
            voicesvar("time.mp3")
        elif "date" in voicerec.text:
            now = datetime.now()
            date = now.strftime('%Y/%m/%d')
            from gtts import gTTS
            tts = gTTS("Today's Date Is" + date)
            tts.save('date.mp3')
            voicesvar("date.mp3")
        else:
            srry = input("Sorry I Didnt Catch You There Press Enter To Re-run Script")
            voicerecmain()
#########################################################################################
    except sr.UnknownValueError:
        missedit()
        tryagain()
voicerecmain()
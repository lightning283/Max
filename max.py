#!/usr/bin/python
from logging import shutdown
from random import random
import time
from playsound import playsound
import speech_recognition as sr
import os
import random
voice= sr.Recognizer()
greet  = ['.voices/greeting.mp3' , '.voices/g2.mp3']
var = random.choice(greet)
playsound(var)
print("here")
os.system("clear")
def mainfunc():
    try:
        with sr.Microphone() as source:
            os.system("clear")
            def greet():
                os.system("pyfiglet -f slant Main Menu")
                print("Listening...")
                print("Say 'Help' if you dont know how to operate.")
            greet()
            audio = voice.listen(source , phrase_time_limit=4)
            text = voice.recognize_google(audio)
            print(f"--> {text}")
            if "application" in text:
                os.system("clear")
                randd = ['.voices/oksir.mp3' , '.voices/onit.mp3', '.voices/surething.mp3' ]
                vareee = random.choice(randd)
                playsound(vareee)
                playsound(".voices/options.mp3")
                print("""
1.Brave
2.VisualStudioCode
3.Spotify
4.Stremio
5.Discord
6.Konsole
7.Teams
                """)
                try:
                    audio_app = voice.listen(source ,  phrase_time_limit=4)
                    text_app = voice.recognize_google(audio_app)
                    print(f"-->{text_app}")
                except sr.UnknownValueError: 
                    playsound(".voices/missedit.mp3")
                    audio_app = voice.listen(source ,  phrase_time_limit=4)
                    text_app = voice.recognize_google(audio_app)
                    print(f"-->{text_app}")
                def apps():
                    if "rave" in text_app:
                        playsound('.voices/surething.mp3')
                        os.system("cd apps && gtk-launch brave.desktop")
                        os.system("clear")
                        def somethingelse():
                            playsound('.voices/somethingelse.mp3')
                            smthelse  = voice.listen(source , phrase_time_limit=4)
                            txt = voice.recognize_google(smthelse)
                            print(f"-->{txt}")
                            if "yes" in txt:
                                playsound(".voices/affirmative.mp3")
                                mainfunc()
                            else:
                                playsound(".voices/shutdown.mp3")
                                exit()
                        somethingelse()
                    elif "iscord" in text_app:
                        playsound('.voices/surething.mp3')
                        os.system("cd apps && gtk-launch discord.desktop")
                        os.system("clear")
                        playsound('.voices/somethingelse.mp3')
                        smthelse  = voice.listen(source , phrase_time_limit=4)
                        txt = voice.recognize_google(smthelse)
                        print(f"-->{txt}")
                        if "yes" in txt:
                            playsound(".voices/affirmative.mp3")
                            playsound(".voices/what_you_again.mp3")
                            print("say 'yes'")
                            mainfunc()
                        else:
                            playsound(".voices/shutdown.mp3")
                            exit()
                    else:
                        print("Im Sorry I Didnt Catch That Please Try Again")
                        input("would you like to run the ai again?")
                        os.system("python max.py")
                apps()
            if "kill" in text:
                playsound(".voices/which_app_terminate.mp3")
                print("USAGE: Say Terminate + 'TheNameOfTheApp'")
                print("EXAMPLE: kill brave")
                audio_close = voice.listen(source ,  phrase_time_limit=4)
                text_close = voice.recognize_google(audio_close)
                print(f"-->{text_close}")
                edited1 = text_close.lower().split("kill" , 1)[1]
                os.system(f"pkill{edited1}")
                playsound('.voices/somethingelse.mp3')
                smthelse  = voice.listen(source , phrase_time_limit=4)
                txt = voice.recognize_google(smthelse)
                print(f"-->{txt}")
                if "yes" in txt:
                    playsound(".voices/affirmative.mp3")
                    playsound(".voices/what_you_want_again.mp3")
                    mainfunc()
                else:
                    playsound(".voices/shutdown.mp3")
                    exit()
            if "help" in text:
                os.system("pyfiglet -f slant Features")
                playsound(".voices/what_you_again.mp3")
                playsound(".voices/features.mp3")
                print("""
1.Open Applications. [keyword:[application]]
2.Search In Brower.  [keyword:[search + what to search ]] eg -> max google search search 'how to cook eggs'
3.Time Or date.      [keyword:[time][date]] eg -> max whats the time or max whats the date today?
4.Check Net Speed.   [keyword:[netspeed]] eg-> max whats my net speed.
5.Help(display this) [keyword:[help]]
6.Kill(Terminate A Application) [keyword[kill + name of app]] eg-> max kill (then it will ask name) , kill brave
7.ShutDown [keyword[shutdown pc]] eg-> max shutdown pc
                """)
                done = input("Done Reading? Press Enter!!")
                mainfunc()
            if "shutdow" in text:
                playsound(".voices/are_you_sure.mp3")
                shutdown_voice = voice.listen(source)
                shutdown_text = voice.recognize_google(shutdown_voice)
                if "yes" in shutdown_text:
                    playsound(".voices/shutting_down.mp3")
                    os.system("systemctl shutdown now")
                else:
                    playsound(".voices/shutdown_cancel.mp3")
    except sr.UnknownValueError:
        os.system("clear")
        playsound(".voices/missedit.mp3")
        mainfunc()

mainfunc()
os.system("clear")

from playsound import playsound
import speech_recognition as sr
import os
import random
import getpass
user_name = getpass.getuser()
DEBUG = True
if DEBUG:
    homedir = ""
else:
    homedir = f"/home/{user_name}/Documents/max/"
voice_dir = f"{homedir}voices/"

def voicerec():          
    voice= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = voice.listen(source)
        voicerec.text = voice.recognize_google(audio)
        voicerec.text = voicerec.text.lower()
        print(f"--> {voicerec.text}")
def missedit():
    playsound(f"{voice_dir}/missedit.mp3") 
    
def tryagain():
    try:
        voicerec()
    except sr.UnknownValueError:
        missedit()
        voicerec()
def packageinstall():
    if os.path.isfile("/usr/bin/yay"):
        edited_install = voicerec.text.lower().split("install" , 1)[1]
        edited_install_1 = edited_install.replace(" " , "")
        install_pkg = f"yay -S {edited_install_1}"
        edited_install_2 = install_pkg.replace("dash" , "-")
        print(edited_install_2)
        os.system(f'''
        konsole -e {edited_install_2}
        ''')
    else:
        os.system("""konsole -e 'python -c print("This Package Manager Is Not Supported yet")'""")

def clearterm():
    os.system("clear")

def appliacations():
    os.system(f"cat {homedir}assets/apps.md")

def wfilter(word):
    program_name = voicerec.text.lower().split(word , 1)[1]
    edited_word = program_name.replace(" " , "")
    return edited_word

def voiceok():
    voices = [f"{voice_dir}/on_it.mp3" , f"{voice_dir/ok.mp3}"]
    choice = random.choice(voices)
    playsound(choice)
############################# Reply Lists ##############################################
def greet():
    greeting = [
        f'{voice_dir}/hellosir.mp3',
        f'{voice_dir}/how_was_your_day.mp3',
        f'{voice_dir}/can_i_help_you.mp3',
        f'{voice_dir}/how_can_i_help_you.mp3'
    ]
    greeting = random.choice(greeting)
    playsound(greeting)

def voiceok():
    ok = [
        f'{voice_dir}/onit.mp3',
        f'{voice_dir}/surething.mp3',
        f'{voice_dir}/ok.mp3',
    ]
    ok = random.choice(ok)
    playsound(ok)
########################################################################################

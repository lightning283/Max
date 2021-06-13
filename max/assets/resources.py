from playsound import playsound
import speech_recognition as sr
import os
import random
import getpass
user_name = getpass.getuser()
homedir = f"/home/{user_name}/.config/max"
voice_dir = f"{homedir}/voices"
def greet():
    greet  = [f'{voice_dir}/greeting.mp3' , f'{voice_dir}/g2.mp3' , f'{voice_dir}/g3.mp3']
    greet_choice = random.choice(greet)
    playsound(greet_choice)

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

def voicesvar(dir):
    playsound(dir)

def onit():
    listvar = [f"{voice_dir}/onit.mp3" , f"{voice_dir}/oksir.mp3"]
    ran =  random.choice(listvar)
    playsound(ran)
def appliacations():
    os.system(f"cat {homedir}assets/apps.md")
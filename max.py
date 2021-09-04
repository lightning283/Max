#!/usr/bin/env python3
import os, webbrowser
from assets.resources import *
from datetime import datetime
from time import sleep
from neuralintents import GenericAssistant

bot = GenericAssistant('intents.json')
bot.train_model()
bot.save_model()

def main():
    # greet()
    try:
        voicerec()
    except sr.UnknownValueError:
        main()
    if "open" in voicerec.text:
        voiceok()
        file_name = wfilter("open")
        os.chdir(f"{homedir}/apps/")
        os.system(f"gtk-launch {file_name}.desktop")
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

    elif "google" in voicerec.text or "google" and "search" in voicerec.text:
        playsound(f"{voice_dir}/what_would_you_like_to_search.mp3")
        voicerec()
        content = voicerec.text
        url_g = f"https://www.google.com/search?q={content}"
        webbrowser.open_new_tab(url_g)
        playsound(f"{voice_dir}/results.mp3")

    elif "youtube" in voicerec.text or "youtube" and "search" in voicerec.text:
        playsound(f"{voice_dir}/what_would_you_like_to_search.mp3")
        voicerec()
        content = voicerec.text
        url_g = f"https://www.youtube.com/results?search_query={content}"
        webbrowser.open_new_tab(url_g)
        playsound(f"{voice_dir}/results.mp3")

    elif "shutdown" in voicerec.text or "poweroff" in voicerec.text or "shut" and "down" in voicerec.text or "power" and "off" in voicerec.text:
        playsound(f"{voice_dir}/poweroff.mp3")
        sleep(10)
        os.system("poweroff")
    elif "server" and "start":
        playsound(f"{voice_dir}/server.mp3")
        os.system(f"python {base_dir}/assets/server.py")
    else:
        response = bot.request(voicerec.text)
        print(response)
        audio = "voices/" + response
        playsound(audio)
        if response == "dontbesad.mp3":
            webbrowser.open_new_tab("https://www.producthunt.com") # les go hunting
        elif response == "dontbesad2.mp3" :
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=funny+memes") #the best i got lol
while True:
    main()

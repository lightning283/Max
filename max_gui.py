#!/usr/bin/python
import sys
from tkinter import *
from sklearn.feature_extraction import image
from assets.resources import *
from assets.tasks import *
from datetime import datetime
from PIL import Image, ImageTk
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton, QLineEdit, QMessageBox
#########################################################################################
window = Tk()
window.title("Max")
window.geometry("200x200")
load = Image.open(f"{homedir}/assets/res/bg3.png")
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.place(x=0, y=0)
window.resizable(0, 0)#makes the window un-resizable.
#############################################################################################

#########################################################################################
def mkbrowser():
    class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.title = 'Build A Browser'
            self.left = 10
            self.top = 10
            self.width = 300
            self.height = 190
            self.initUI()
        
        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
        
            self.label = QLabel('<u>Enter URL</u>', self)
            self.label.move(100 , 0)
            self.label = QLabel('<u>Enter Name</u>', self)
            self.label.move(100 , 70)

            self.text_url = QLineEdit(self)
            self.text_url.move(20, 30)
            self.text_url.resize(260,40)

            self.text_name = QLineEdit(self)
            self.text_name.move(20, 100)
            self.text_name.resize(260,40)

            self.button_submit = QPushButton('Submit', self)
            self.button_submit.move(20,150)

            self.button = QPushButton('Help', self)
            self.button.move(180,150)

            self.button_submit.clicked.connect(self.mkbrowser)
            self.show()
            self.button.clicked.connect(self.on_click)
            self.show()
        
        @pyqtSlot()
        def on_click(self):
            textboxValue = ""
            QMessageBox.question(self, 'Help', "This Tool Helps You To Build A Browser That Will Only Show A Specifc Website Thus Making This Fast And Efficent." + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        def mkbrowser(self):
            url = self.text_url.text()
            file_name = self.text_name.text()
            import getpass
            username = getpass.getuser()
            os.mkdir(f"/home/{username}/Desktop/pyqt_browser")
            f = open(f"/home/{username}/Desktop/pyqt_browser/{file_name}.py" , 'a')
            browser_qt = f"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("{url}"))
        
        self.setCentralWidget(self.browser)

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()
            """
            f.write(browser_qt)
            f.close()
            playsound(f'{voice_dir}/compiling.mp3')
            os.system(f"cd ~/Desktop/pyqt_browser/ && nuitka3 {file_name}.py")
            playsound(f"{homedir}/voices/comp_done.mp3")
            exit()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

#########################################################################################
def voicerecmain():
    greet()
    voicerec()
    if "open discord" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch discord.desktop")
    elif "open telegram" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch telegram.desktop")
    elif "open stremio" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        if not os.path.isfile("/opt/stremio/stremio"):
            playsound(f"{voice_dir}/install_pkg.mp3")
            voicerec()
            if "yes" in voicerec.text:
                playsound(f"{voice_dir}/installing_now.mp3")
                os.system("konsole -e yay -S aur/stremio")
        else:
            os.system(f"cd {homedir}/assets/apps && gtk-launch stremio.desktop")
    elif "open brave" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch brave.desktop")
    elif "open vscode" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch vscode.desktop")
    elif "open spotify" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch spotify.desktop")
    elif "open konsole" in voicerec.text:
        playsound(f'{voice_dir}/surething.mp3')
        os.system(f"cd {homedir}/assets/apps && gtk-launch konsole.desktop")
    elif voicerec.text == "list features":
        voicesvar(f"{voice_dir}/features.mp3")
        os.system(f"konsole -e bash {homedir}/assets/features.sh")
    elif "install" in voicerec.text:
        packageinstall()
    elif "list runnable application" in voicerec.text:
        voicesvar(f"{voice_dir}/options.mp3")
        os.system(f"konsole -e bash {homedir}/assets/apps.sh")
    elif "list features" in voicerec.text:
        os.system(f"konsole -e bash {homedir}/assets/features.sh")
    elif "time" in voicerec.text:
        now = datetime.now()
        time = now.strftime('%I:%M:%S')
        from gtts import gTTS
        tts = gTTS("Now The Time Is" + time)
        tts.save(f'{voice_dir}/time.mp3')
        voicesvar(f"{voice_dir}/time.mp3")
    elif "date" in voicerec.text:
        now = datetime.now()
        date = now.strftime('%Y/%m/%d')
        from gtts import gTTS
        tts = gTTS("Today's Date Is" + date)
        tts.save(f'{voice_dir}/date.mp3')
        voicesvar(f"{voice_dir}/date.mp3")
    elif "task" in voicerec.text:
        playsound(f"{voice_dir}/tasks.mp3")
        os.system(f"konsole -e nano {homedir}/assets/tasks.py")
        playsound(f"{voice_dir}/edit_task_script.mp3")
        voicerec()
        if voicerec.text == "yes":
            os.system(f"konsole -e nano {script_location}")
        else:
            playsound(f"{voice_dir}/verywell.mp3")
    elif task_name in voicerec.text:
        os.system(f"bash {script_location}")
    elif "build browser" in voicerec.text:
        mkbrowser()
    elif "open download" in voicerec.text:
        voicesvar(f"{homedir}/voices/onit.mp3")
        pydown()
    elif "system status" in voicerec.text:
        playsound(f"{homedir}/voices/sysstat.mp3")
        os.system("konsole -e htop")
        os.system("konsole -e neofetch")
    else:
        exit
#########################################################################################
def exit():
    window.quit()
def debugmode():
    os.system(f"konsole -e python {homedir}/max_gui.py")
    
#########################################################################################
photo_mic = PhotoImage(file = f"{homedir}/assets/res/mic.png")
photoimage_mic = photo_mic.subsample(3, 3)
Button(window,text = 'Listen', bg="black", fg="green" , command=voicerecmain ,  image = photoimage_mic,compound = LEFT).place(x=50, y=50)
photo = PhotoImage(file = f"{homedir}/assets/res/bug.png")
photoimage = photo.subsample(3, 3)
Button(window,text = 'DebugMode', bg="black", fg="green" , command=debugmode ,  image = photoimage,compound = LEFT).place(x=1, y=166)
########################################################
photo = PhotoImage(file = f"{homedir}/assets/res/menu.png")
photoimage = photo.subsample(3, 3)
Button(window, command=pydown,  image = photoimage,compound = LEFT).place(x=1, y=1)
########################################################
btn = Button(window, text="Exit", bg="black", fg="red", command=exit)
btn.place(x=150, y=170)
#########################################################################################
window.mainloop()

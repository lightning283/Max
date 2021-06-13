import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QMainWindow , QLabel , QDialog , QVBoxLayout
from PyQt5.QtGui import QIcon , QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import title
from resources import *
from assets.tasks import *
from datetime import datetime

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "TestWindow"
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 400
        # self.iconName = "icon.png"
        self.InitWindow()

        
    def InitWindow(self):
        labelImage = QLabel(self)
        pixmap = QPixmap("assets/res/bg3.png")
        labelImage.setPixmap(pixmap)

        button = QPushButton('Listen', self)
        button.move(100,70)
        button.clicked.connect(self.voicerecmain)

        # self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left , self.top, self.width , self.height)
        self.setWindowTitle(self.title)

        self.show()
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
    def voicerecmain(self):
        greet()
        voicerec()
        if "open discord" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch discord.desktop")
        elif "open telegram" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch telegram.desktop")
        elif "open stremio" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            if not os.path.isfile("/opt/stremio/stremio"):
                playsound(f"{voice_dir}/install_pkg.mp3")
                voicerec()
                if "yes" in voicerec.text:
                    playsound(f"{voice_dir}/installing_now.mp3")
                    os.system("yay -S aur/stremio")
            else:
                os.system("cd assets/apps && gtk-launch stremio.desktop")
        elif "open brave" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch brave.desktop")
        elif "open vscode" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch vscode.desktop")
        elif "open spotify" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch spotify.desktop")
        elif "open konsole" in voicerec.text:
            playsound(f'{voice_dir}/surething.mp3')
            os.system("cd assets/apps && gtk-launch konsole.desktop")
        elif voicerec.text == "list features":
            voicesvar(f"{voice_dir}/features.mp3")
            os.system("konsole -e bash assets/features.sh")
        elif "install" in voicerec.text:
            packageinstall()
        elif "list runnable application" in voicerec.text:
            voicesvar(f"{voice_dir}/options.mp3")
            os.system("konsole -e bash assets/apps.sh")
        elif "list features" in voicerec.text:
            os.system("konsole -e bash assets/features.sh")
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
            os.system("konsole -e nano assets/tasks.py")
            playsound(f"{voice_dir}/edit_task_script.mp3")
            voicerec()
            if voicerec.text == "yes":
                os.system(f"konsole -e nano {script_location}")
            else:
                playsound(f"{voice_dir}/verywell.mp3")
        elif task_name in voicerec.text:
            os.system(f"bash {script_location}")
        elif "build browser" in voicerec.text:
            # mkbrowser()
            pass
        else:
            exit


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
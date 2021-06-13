#!/usr/bin/python
from PyQt5.QtWidgets import QApplication, QPushButton , QMainWindow , QLabel ,QMessageBox
from PyQt5.QtCore import pyqtSlot
import sys , os
from resources import voice_dir
from playsound import playsound
from PyQt5.QtWidgets import QLineEdit

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
        os.system(f"cd ~/Desktop/pyqt_browser/ && pyinstaller --onefile {file_name}.py")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

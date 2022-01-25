from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QLabel, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.label1=QLabel(self)
        self.label1.setText("Itt nem nyílnak")
        self.label1.move(50,50)
        
        button1=QPushButton(self)
        button1.setText("Semmi")
        button1.move(100,140)
        button1.clicked.connect(self.on_click_mehet_button)
        
        self.setGeometry(100,100,300,200)
        self.setWindowTitle("Itt vagyok")
        self.show()
        
    def on_click_mehet_button(self):
        print("Nem működik")
        self.label1.setText("Itt se")
        self.setWindowTitle("Nem vagyok itt")

application=QApplication(sys.argv)
mainWindow=MainWindow()
sys.exit(application.exec_())


        


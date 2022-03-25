from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys
import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
############Ouverture et  Titre de la fenetre############
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
##########################################################
        

        self.label1 = QLabel("Enter your IP:", self)
        self.label2 = QLineEdit(self)
        self.label2.move(10, 20)
        



        self.label4 = QLabel("Enter your API KEY: ",self)
        self.label4.move(10, 40)
        self.label5 = QLineEdit(self)
        self.label5.move(10, 60)

        self.label6 = QLabel("Enter your hostname:", self)
        self.label6.move(10, 80)
        self.label7 = QLineEdit(self)
        self.label7.move(10, 100)        


        
        #############################################################
        
        #######code de base du bouton #########
        self.button = QPushButton("Send", self)
        self.button.move(10, 120)
        #######Fin du code de base du bouton######



        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.label7.text()
        ipd = self.label2.text()
        apik = self.label5.text()        


        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ipd,apik)
            if res:                
                self.label2.adjustSize()
                self.label5.adjustSize()
                self.show()
                url2 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"], res["Longitude"])
                #webbrowser.open_new_tab(url2)
                webbrowser.open(url2)

    def __query(self, hostname,ipd,apik):
        url = "http://%s/ip/%s?key=%s" % (hostname,ipd,apik)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()

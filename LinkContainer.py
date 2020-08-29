# Created by: PyQt5 UI code generator 5.13.2
#
# LinkContainer 1.0, creato da AbdelmounaimOmri aka tpx1sc

# LinkContainer 1.0 é un programma che permette di salvare qualsiasi tipo di link, nascondendoli
# rendendoli accessibili solo al programma in questione
#

# Importazione dei moduli
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMessageBox
    import codecs, os, sys
except:
    print("Prima di usare il programma devi scaricare PyQt5 e codecs")


___autore___ = '''AbdelmounaimOmri aka tpx1sc'''

nome_del_file = ("links.txt") # Nome del file nel quale verranno salvate le password
nome_del_programma = ("LinkContainer") # Variabile contente il nome del programma
versione = ("{} 1.0".format(nome_del_programma)) # Variabile contente la Versione

class Ui_MainWindow(object): # Classe della gui
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 463)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.AddLinks = QtWidgets.QPushButton(self.centralwidget) # Creazione del bottone 'Salva i link'
        self.AddLinks.setGeometry(QtCore.QRect(464, 142, 101, 61))
        self.AddLinks.setObjectName("AddLinks")

        self.ShowLink = QtWidgets.QPushButton(self.centralwidget) # Creazione del bottone 'Visualizza i link salvati'
        self.ShowLink.setGeometry(QtCore.QRect(464, 212, 101, 61))

        font = QtGui.QFont()
        font.setPointSize(8)

        self.ShowLink.setFont(font)
        self.ShowLink.setObjectName("ShowLink")

        self.RemoveLink = QtWidgets.QPushButton(self.centralwidget) # Creazione del bottone 'Cancella i link'
        self.RemoveLink.setGeometry(QtCore.QRect(464, 280, 101, 101))
        self.RemoveLink.setObjectName("RemoveLink")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget) # Creazione della scritta "LinkContainer"
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 501, 80))

        font = QtGui.QFont()
        font.setFamily("Ariel")
        font.setPointSize(22)

        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget) # Creazione del campo input 'aggiungi link'
        self.textEdit.setGeometry(QtCore.QRect(40, 210, 411, 171))
        self.textEdit.setObjectName("textEdit")

        self.TextArea = QtWidgets.QLineEdit(self.centralwidget) # Creazione del campo output 'mostra link'
        self.TextArea.setGeometry(QtCore.QRect(40, 140, 411, 61))
        self.TextArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TextArea.setObjectName("TextArea")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow) # Creazione della menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)


        self.actionShowSavedLinks = QtWidgets.QAction(MainWindow)
        self.actionShowSavedLinks.setObjectName("actionShowSavedLinks")


        self.actionVersione = QtWidgets.QAction(MainWindow)
        self.actionVersione.setObjectName("actionVersione")

        self.actionInformazioni_sul_programma = QtWidgets.QAction(MainWindow)
        self.actionInformazioni_sul_programma.setObjectName("actionInformazioni_sul_programma")

        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")

        self.menu.addAction(self.actionVersione)
        self.menu.addAction(self.actionInformazioni_sul_programma)

        self.menu.addSeparator()
        self.menu.addAction(self.actionEsci)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textEdit.setReadOnly(True) # Imposta il secondo campo input in campo output

        self.AddLinks.clicked.connect(self.AddLinks_pressed) # Collega il bottone 'AddLinks' alla funzione 'AddLinks_pressed'

        self.ShowLink.clicked.connect(self.ShowLink_pressed) # Collega il bottone 'ShowLinks' alla funzione 'ShowLink_pressed'

        self.RemoveLink.clicked.connect(self.clear_links) # Collega il bottone 'RemoveLink' alla funzione 'clear_links'

        self.actionEsci.triggered.connect(self.actionEsci_pressed) # Collega la voce del menu 'Esci' alla funzione 'actionEsci_pressed'

        self.actionInformazioni_sul_programma.triggered.connect(self.show_Info) # Collega la voce del menu 'Informazioni sul programma' alla funzione 'show_Info'

        self.actionVersione.triggered.connect(self.show_Versione) # Collega la voce del menu 'Versione' alla funzione 'show_Versione'


    def clear_links(self):
        if os.path.exists(nome_del_file):
            os.remove(nome_del_file)
            self.textEdit.clear()
            self.TextArea.clear()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Errore")
            msg.setText("Non hai ancora salvato nessun link")
            msg.setIcon(QMessageBox.Critical)
            #msg.setDetailedText(str(e))
            x = msg.exec_()

    def AddLinks_pressed(self):
        link = codecs.decode(self.TextArea.text(), "rot_13")
        try:
            f = open(nome_del_file, "x")
            f.write('{}\n'.format(link))
        except:
            f = open(nome_del_file, "a")
            f.write('{}\n'.format(link))

    def ShowLink_pressed(self):
        try:
            self.textEdit.clear()
            f = open(nome_del_file, "r")
            encrypted_links = codecs.decode(f.read(), "rot_13")

            self.textEdit.insertPlainText(encrypted_links)
            self.TextArea.clear()
        except FileNotFoundError as e:
            msg = QMessageBox()
            msg.setWindowTitle("Errore")
            msg.setText("Non hai ancora salvato nessun link")
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()

    def actionEsci_pressed(self):
        sys.exit()

    def show_Info(self):
        info = QMessageBox()
        info.setWindowTitle("Informazioni su {}".format(nome_del_programma))
        info.setText('{} é un programma che permette di salvare qualsiasi tipo di link, nascondendoli e rendendoli accessibili solo al programma in questione.'.format(nome_del_programma))
        info.setIcon(QMessageBox.Information)

        y = info.exec_()

    def show_Versione(self):
        ver = QMessageBox()
        ver.setWindowTitle("Versione")
        ver.setText(versione)
        ver.setIcon(QMessageBox.Information)

        z = ver.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("linkcontainer", "LinkContainer"))
        self.AddLinks.setText(_translate("MainWindow", "Aggiungi un link"))
        self.ShowLink.setText(_translate("MainWindow", "Mostra i link salvati"))
        self.groupBox.setTitle(_translate("MainWindow", "LINK CONTAINER"))
        self.TextArea.setText(_translate("MainWindow", ""))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionShowSavedLinks.setText(_translate("MainWindow", "Visualizza i link salvati"))
        self.RemoveLink.setText(_translate("MainWindow", "Cancella i Link"))
        self.actionVersione.setText(_translate("MainWindow", "Versione"))
        self.actionInformazioni_sul_programma.setText(_translate("MainWindow", "Informazioni sul programma"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

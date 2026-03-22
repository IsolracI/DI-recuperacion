from pythonUI.MainWindow import Ui_MainWindow
from src.Connection import *
from PyQt6 import QtWidgets
from styles import Styles
from src.Events import *
from src.Users import *
from src import Globals
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Globals.ui = Ui_MainWindow()
        Globals.ui.setupUi(self)

               ###################
        ####   ##-## GENERAL ##-##   ####
               ###################

        # Style Sheet
        self.setStyleSheet(Styles.load_stylesheet())

        # DB Connection
        Connection.dbConnection()

               #################
        ####   ##-## USERS ##-##   ####
               #################

        # Table
        Users.loadUsersTable()
        Globals.ui.btn_showEmployees.clicked.connect(Users.showEmployees)
        Globals.ui.btn_showAll.clicked.connect(Users.showAll)
        Globals.ui.btn_showClients.clicked.connect(Users.showClients)
        Globals.ui.tbl_users.clicked.connect(Users.loadUserInfo)
        Events.resizeTable(Globals.ui.tbl_users)

        # Buttons
        Globals.ui.btn_saveUser.clicked.connect(Users.saveUser)
        Globals.ui.btn_modifyUser.clicked.connect(Users.modifyUser)
        Globals.ui.btn_clearUser.clicked.connect(Users.clearUsersFields)
        Globals.ui.btn_deleteUser.clicked.connect(Users.deleteUser)

        # Fields
        Globals.ui.txt_userDNI.editingFinished.connect(Users.checkDni)
        Globals.ui.txt_userEmail.editingFinished.connect(lambda: Users.checkMail(Globals.ui.txt_userEmail.text()))
        Globals.ui.txt_userMobile.editingFinished.connect(lambda: Users.checkMobile(Globals.ui.txt_userMobile.text()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
from pythonUI.MainWindow import Ui_MainWindow
from src.Connection import *
from PyQt6 import QtWidgets
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

        # DB Connection
        Connection.dbConnection()

               #################
        ####   ##-## USERS ##-##   ####
               #################

        Users.loadUsersTable()
        Globals.ui.btn_showEmployees.clicked.connect(Users.showEmployees)
        Globals.ui.btn_showAll.clicked.connect(Users.showAll)
        Globals.ui.btn_showClients.clicked.connect(Users.showClients)
        Events.resizeTable(Globals.ui.tbl_users)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
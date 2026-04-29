from pythonUI.MainWindow import Ui_MainWindow
from src.Connection import *
from PyQt6 import QtWidgets
from styles import Styles
from src.Reports import *
from src.Events import *
from src.Users import *
from src.Tasks import *
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

        # Menu bar
        Globals.ui.actionUsers_Report.triggered.connect(Reports.usersReport)

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
        Globals.ui.txt_userName.editingFinished.connect(Users.checkName)
        Globals.ui.txt_userAddress.editingFinished.connect(Users.checkAddress)
        Globals.ui.txt_userDNI.editingFinished.connect(Users.checkDni)
        Globals.ui.txt_userEmail.editingFinished.connect(lambda: Users.checkMail(Globals.ui.txt_userEmail.text()))
        Globals.ui.txt_userMobile.editingFinished.connect(lambda: Users.checkMobile(Globals.ui.txt_userMobile.text()))

               #################
        ####   ##-## TASKS ##-##   ####
               #################

        Tasks.loadTasksAssets()

        # Table
        Tasks.loadAllTasks()
        Globals.ui.tbl_tasks.clicked.connect(Tasks.loadTaskInfo)
        Events.resizeTable(Globals.ui.tbl_tasks)

        # Buttons
        Globals.ui.btn_saveTask.clicked.connect(Tasks.saveTask)
        Globals.ui.btn_modifyTask.clicked.connect(Tasks.modifyTask)
        Globals.ui.btn_deleteTask.clicked.connect(Tasks.deleteTask)
        Globals.ui.btn_reloadTask.clicked.connect(Tasks.loadAllTasks)
        Globals.ui.btn_clearTask.clicked.connect(Tasks.clearTasksFields)
        Globals.ui.btn_searchClient.clicked.connect(Tasks.loadClientTasks)
        Globals.ui.btn_searchEmployee.clicked.connect(Tasks.loadEmployeesTasks)

        # Fields
        Tasks.loadStatusOptions()
        Globals.ui.txt_employeeName.editingFinished.connect(Tasks.checkEmployee)
        Globals.ui.txt_clientName.editingFinished.connect(Tasks.checkClient)
        Globals.ui.txt_taskPrice.editingFinished.connect(Tasks.checkPrice)
        Globals.ui.txt_taskHours.editingFinished.connect(Tasks.checkTasksHours)
        Globals.ui.txt_taskService.editingFinished.connect(Tasks.checkService)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
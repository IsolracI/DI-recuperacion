from pythonUI.MainWindow import Ui_MainWindow
from src.Tasks.TasksTable import TasksTable
from src.Users.UsersTable import *
from src.Users.UsersForm import *
from src.Tasks.TasksForm import *
from styles import Styles
from src.Reports import *
from src.Events import *
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
        Globals.ui.actionTasks_Report.triggered.connect(Reports.tasksReport)

               #################
        ####   ##-## USERS ##-##   ####
               #################

        UsersTable.setNumPages()

        # Table
        UsersTable.loadUsersTable()
        Globals.ui.btn_showEmployees.clicked.connect(UsersTable.showEmployees)
        Globals.ui.btn_showAll.clicked.connect(UsersTable.showAll)
        Globals.ui.btn_showClients.clicked.connect(UsersTable.showClients)
        Globals.ui.tbl_users.clicked.connect(UsersForm.loadUserInfo)
        Events.resizeTable(Globals.ui.tbl_users)

        # Buttons
        Globals.ui.btn_saveUser.clicked.connect(UsersForm.saveUser)
        Globals.ui.btn_modifyUser.clicked.connect(UsersForm.modifyUser)
        Globals.ui.btn_clearUser.clicked.connect(UsersForm.clearUsersFields)
        Globals.ui.btn_deleteUser.clicked.connect(UsersForm.deleteUser)
        Globals.ui.btn_usersTablePrevPage.clicked.connect(UsersTable.goToPreviousPage)
        Globals.ui.btn_usersTableNextPage.clicked.connect(UsersTable.goToNextPage)

        # Fields
        Globals.ui.txt_userName.editingFinished.connect(UsersForm.checkName)
        Globals.ui.txt_userAddress.editingFinished.connect(UsersForm.checkAddress)
        Globals.ui.txt_userDNI.editingFinished.connect(UsersForm.checkDni)
        Globals.ui.txt_userEmail.editingFinished.connect(lambda: UsersForm.checkMail(Globals.ui.txt_userEmail.text()))
        Globals.ui.txt_userMobile.editingFinished.connect(lambda: UsersForm.checkMobile(Globals.ui.txt_userMobile.text()))

               #################
        ####   ##-## TASKS ##-##   ####
               #################

        TasksForm.loadTasksAssets()

        # Table
        TasksTable.loadAllTasks()
        Globals.ui.tbl_tasks.clicked.connect(TasksForm.loadTaskInfo)
        Events.resizeTable(Globals.ui.tbl_tasks)

        # Buttons
        Globals.ui.btn_saveTask.clicked.connect(TasksForm.saveTask)
        Globals.ui.btn_modifyTask.clicked.connect(TasksForm.modifyTask)
        Globals.ui.btn_deleteTask.clicked.connect(TasksForm.deleteTask)
        Globals.ui.btn_reloadTask.clicked.connect(TasksTable.loadAllTasks)
        Globals.ui.btn_clearTask.clicked.connect(TasksForm.clearTasksFields)
        Globals.ui.btn_searchClient.clicked.connect(TasksTable.loadClientTasks)
        Globals.ui.btn_searchEmployee.clicked.connect(TasksTable.loadEmployeesTasks)
        Globals.ui.btn_tasksTablePrevPage.clicked.connect(TasksTable.goToPreviousPage)
        Globals.ui.btn_tasksTableNextPage.clicked.connect(TasksTable.goToNextPage)

        # Fields
        TasksForm.loadStatusOptions()
        Globals.ui.txt_employeeName.editingFinished.connect(TasksForm.checkEmployee)
        Globals.ui.txt_clientName.editingFinished.connect(TasksForm.checkClient)
        Globals.ui.txt_taskPrice.editingFinished.connect(TasksForm.checkPrice)
        Globals.ui.txt_taskHours.editingFinished.connect(TasksForm.checkTasksHours)
        Globals.ui.txt_taskService.editingFinished.connect(TasksForm.checkService)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
from src.Connection import *
from PyQt6 import QtCore
from src import Globals
import math

class TasksTable:
    tasks = []
    tableIndex = 0
    rowsPerPage = 13
    numPages = 1

    @staticmethod
    def setNumPages():
        try:
            TasksTable.numPages = max(1, math.ceil(len(TasksTable.tasks) / TasksTable.rowsPerPage))

        except Exception as error:
            print("(TasksTable.setTableSettings) an error occurred while trying to set the table's settings: ", error)


    @staticmethod
    def _checkButtons():
        try:
            if TasksTable.tableIndex <= 0:
                Globals.ui.btn_tasksTablePrevPage.setEnabled(False)
            else:
                Globals.ui.btn_tasksTablePrevPage.setEnabled(True)

            if TasksTable.tableIndex >= TasksTable.numPages - 1:
                Globals.ui.btn_tasksTableNextPage.setEnabled(False)
            else:
                Globals.ui.btn_tasksTableNextPage.setEnabled(True)

        except Exception as error:
            print("(TasksTable._checkButtons) an error occurred while trying to check the butons: ", error)


    @staticmethod
    def _loadTasksTable():
        """

        Carga una lista de tareas en la tabla de tareas
        de la interfaz.

        :param tasks: Lista de tareas obtenidas desde la base de datos.
        :type tasks: list
        :return: None

        """
        try:
            start = TasksTable.tableIndex * TasksTable.rowsPerPage
            end = start + TasksTable.rowsPerPage

            tasks = TasksTable.tasks[start:end]

            index = 0
            uiTable = Globals.ui.tbl_tasks
            uiTable.clearContents()

            for task in tasks:
                uiTable.setRowCount(index + 1)
                uiTable.setItem(index, 0, QtWidgets.QTableWidgetItem(str(task[0])))
                uiTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(task[1])))
                uiTable.setItem(index, 2, QtWidgets.QTableWidgetItem(str(task[2])))
                uiTable.setItem(index, 3, QtWidgets.QTableWidgetItem(str(task[3])))
                uiTable.setItem(index, 4, QtWidgets.QTableWidgetItem(str(task[4])))
                uiTable.setItem(index, 5, QtWidgets.QTableWidgetItem(str(task[5])))
                uiTable.setItem(index, 6, QtWidgets.QTableWidgetItem(str(task[6])))

                uiTable.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                index += 1

        except Exception as error:
            print("(TasksTable.loadTasksTable) an error occurred while trying to load the tasks table: ", error)


    @staticmethod
    def loadAllTasks():
        """

        Carga todas las tareas almacenadas en la base de datos
        y las muestra en la tabla de tareas.

        :return: None

        """
        try:
            TasksTable.tasks = Connection.getTasks()
            TasksTable.tableIndex = 0
            TasksTable.setNumPages()
            TasksTable._checkButtons()

            TasksTable._loadTasksTable()

        except Exception as error:
            print("(TasksTable.loadAllTasks) An error occurred while trying to load all tasks on the table: ", error)

    @staticmethod
    def loadEmployeesTasks():
        """

        Carga en la tabla las tareas asociadas
        al empleado introducido.

        Si el campo del empleado está vacío, se muestra
        un mensaje de error.

        :return: None

        """
        try:
            employee = Globals.ui.txt_employeeName.text()

            if not employee:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("The employee's field is empty")
                mbox.exec()
                return

            TasksTable.tasks = Connection.getEmployeeTasks(employee)
            TasksTable.tableIndex = 0
            TasksTable.setNumPages()
            TasksTable._checkButtons()
            TasksTable._loadTasksTable()

        except Exception as error:
            print(
                "(TasksTable.loadEmployeesTasks) an error occurred while trying to load the employee's tasks on the table: ", error)

    @staticmethod
    def loadClientTasks():
        """

        Carga en la tabla las tareas asociadas
        al cliente introducido.

        Si el campo del cliente está vacío, se muestra
        un mensaje de error.

        :return: None

        """
        try:
            client = Globals.ui.txt_clientName.text()

            if not client:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("The client's field is empty")
                mbox.exec()
                return

            TasksTable.tasks = Connection.getClientTasks(client)
            TasksTable.tableIndex = 0
            TasksTable.setNumPages()
            TasksTable._checkButtons()
            TasksTable._loadTasksTable()

        except Exception as error:
            print("(TasksTable.loadClientTasks) an error occurred while trying to load the client's tasks on the table: ", error)


    @staticmethod
    def goToNextPage():
        try:
            if TasksTable.tableIndex < TasksTable.numPages - 1:
                TasksTable.tableIndex += 1

            TasksTable._checkButtons()
            TasksTable._loadTasksTable()

        except Exception as error:
            print("(TasksTable.goToNextPage) an error occurred while trying to go to the next page: ", error)


    @staticmethod
    def goToPreviousPage():
        try:
            if TasksTable.tableIndex > 0:
                TasksTable.tableIndex -= 1

            TasksTable._checkButtons()
            TasksTable._loadTasksTable()

        except Exception as error:
            print("(TasksTable.goToPreviousPage) an error occurred while trying to go to the previous page: ", error)
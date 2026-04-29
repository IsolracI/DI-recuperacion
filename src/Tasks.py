from PyQt6 import QtWidgets, QtCore, QtGui
from src.Connection import *
from src import Globals
import re

class Tasks:

    @staticmethod
    def loadTasksAssets():
        try:
            employeeIcon = QtGui.QPixmap("../assets/employee_icon.png")
            ClientIcon = QtGui.QPixmap("../assets/client_icon.png")
            lensIcon = QtGui.QIcon("../assets/lens_icon.png")

            Globals.ui.employeePortrait.setPixmap(employeeIcon)
            Globals.ui.clientPortrait.setPixmap(ClientIcon)
            Globals.ui.btn_searchEmployee.setIcon(lensIcon)
            Globals.ui.btn_searchClient.setIcon(lensIcon)

        except Exception as error:
            print("(Tasks.loadAssets) An error occurred while trying load the assets: ", error)

    @staticmethod
    def loadStatusOptions():
        statusOptions = ["  -- selecciona --", "Pendiente", "En curso", "Finalizada", "Facturada"]
        Globals.ui.cmb_taskStatus.addItems(statusOptions)


    @staticmethod
    def checkEmployee():
        existingEmployees = Connection.getEmployeesName()
        employee = Globals.ui.txt_employeeName.text().strip()

        if employee not in existingEmployees:
            Globals.ui.txt_employeeName.setStyleSheet("background-color: #FFC0CB; color black")
            Globals.ui.txt_employeeName.clear()
            Globals.ui.txt_employeeName.setPlaceholderText("The employee entered doesn't exist in the database.")
        else:
            Globals.ui.txt_employeeName.setStyleSheet("background-color: rgb(255, 255, 220)")


    @staticmethod
    def checkClient():
        existingClients = Connection.getClientsName()
        client = Globals.ui.txt_clientName.text().strip()

        if not client or client not in existingClients:
            Globals.ui.txt_clientName.setStyleSheet("background-color: #FFC0CB; color black")
            Globals.ui.txt_clientName.clear()
            Globals.ui.txt_clientName.setPlaceholderText("The client entered doesn't exist in the database.")
        else:
            Globals.ui.txt_clientName.setStyleSheet("background-color: rgb(255, 255, 220)")


    @staticmethod
    def checkPrice():
        try:
            pattern = r'^\d+([.,]\d{1,2})?$'
            price = Globals.ui.txt_taskPrice.text().strip()

            if re.match(pattern, price):
                Globals.ui.txt_taskPrice.setStyleSheet("background-color: rgb(255, 255, 220)")
            else:
                Globals.ui.txt_taskPrice.setStyleSheet("background-color: #FFC0CB; color black")
                Globals.ui.txt_taskPrice.clear()
                Globals.ui.txt_taskPrice.setPlaceholderText("Format: 0.00")

        except Exception as error:
            print("(Tasks.checkPrice) An error occurred while trying check the price: ", error)


    @staticmethod
    def checkService():
        try:
            service = Globals.ui.txt_taskService.text().strip()

            if not service:
                Globals.ui.txt_taskService.setStyleSheet("background-color: #FFC0CB; color black")
                Globals.ui.txt_taskService.clear()
                Globals.ui.txt_taskService.setPlaceholderText("Please specify the service.")
            else:
                Globals.ui.txt_taskService.setStyleSheet("background-color: rgb(255, 255, 220)")

        except Exception as error:
            print("(Tasks.checkService) An error occurred while trying check the service: ", error)


    @staticmethod
    def checkTasksHours():
        try:
            hours = Globals.ui.txt_taskHours.text().strip()

            if not hours:
                Globals.ui.txt_taskHours.setStyleSheet("background-color: #FFC0CB; color black")
                Globals.ui.txt_taskHours.clear()
                Globals.ui.txt_taskHours.setPlaceholderText("0")
                return

            intHours = int(hours)

            if intHours <= 0:
                Globals.ui.txt_taskHours.setStyleSheet("background-color: #FFC0CB; color black")
                Globals.ui.txt_taskHours.clear()
                Globals.ui.txt_taskHours.setPlaceholderText("0")
            else:
                Globals.ui.txt_taskHours.setStyleSheet("background-color: rgb(255, 255, 220)")

        except Exception as error:
            print("(Tasks.checkTaskHours) An error occurred while trying check the hours: ", error)


    @staticmethod
    def _checkFields():
        try:
            fields = [Globals.ui.txt_taskID.text(),
                      Globals.ui.txt_clientName.text(),
                      Globals.ui.txt_employeeName.text(),
                      Globals.ui.txt_taskService.text(),
                      Globals.ui.txt_taskPrice.text(),
                      Globals.ui.txt_taskHours.text(),
                      Globals.ui.cmb_taskStatus.currentText()]

            if all(fields):
                return True
            else:
                return False

        except Exception as error:
            print("(Tasks.checkFields) An error occurred while trying to check the fields: ", error)

    @staticmethod
    def _loadTasksTable(tasks):
        try:
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
                index += 1

        except Exception as error:
            print("(Tasks.loadTasksTable) an error occurred while trying to load the tasks table: ", error)


    @staticmethod
    def loadAllTasks():
        try:
            tasks = Connection.getTasks()
            Tasks._loadTasksTable(tasks)

        except Exception as error:
            print("(Tasks.loadAllTasks) An error occurred while trying to load all tasks on the table: ", error)


    @staticmethod
    def loadEmployeesTasks():
        try:
            employee = Globals.ui.txt_employeeName.text()

            if not employee:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("The employee's field is empty")
                mbox.exec()
                return

            employeeTasks = Connection.getEmployeeTasks(employee)
            Tasks._loadTasksTable(employeeTasks)

        except Exception as error:
            print("(Tasks.loadEmployeesTasks) an error occurred while trying to load the employee's tasks on the table: ", error)


    @staticmethod
    def loadClientTasks():
        try:
            client = Globals.ui.txt_clientName.text()

            if not client:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("The client's field is empty")
                mbox.exec()
                return

            clientTasks = Connection.getClientTasks(client)
            Tasks._loadTasksTable(clientTasks)

        except Exception as error:
            print("(Tasks.loadClientTasks) an error occurred while trying to load the client's tasks on the table: ", error)


    @staticmethod
    def loadTaskInfo():
        try:
            selectedRow = Globals.ui.tbl_tasks.currentRow()
            taskId = Globals.ui.tbl_tasks.item(selectedRow, 0).text()

            taskInfo = Connection.getTaskInfo(taskId)

            widgets = [Globals.ui.txt_taskID,
                       Globals.ui.txt_clientName,
                       Globals.ui.txt_employeeName,
                       Globals.ui.txt_taskService,
                       Globals.ui.txt_taskPrice,
                       Globals.ui.txt_taskHours,
                       Globals.ui.cmb_taskStatus]

            for widget in widgets:
                widget.setStyleSheet("background-color: white;")

            for i in range(len(taskInfo)):
                if hasattr(widgets[i], "setText"):
                    widgets[i].setText(str(taskInfo[i]))
                if hasattr(widgets[i], "setCurrentText"):
                    widgets[i].setCurrentText(str(taskInfo[i]))

        except Exception as error:
            print("(Tasks.loadTaskInfo) an error occurred while trying to load the tasks' info:", error)


    @staticmethod
    def saveTask():
        try:
            fieldsData = [Globals.ui.txt_clientName.text(),
                          Globals.ui.txt_employeeName.text(),
                          Globals.ui.txt_taskService.text(),
                          Globals.ui.txt_taskPrice.text(),
                          Globals.ui.txt_taskHours.text(),
                          Globals.ui.cmb_taskStatus.currentText()]

            if not all(fieldsData):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("Please fill all the fields.")
                mbox.exec()
                return

            if Globals.ui.cmb_taskStatus.currentText() == "  -- selecciona --":
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("Please specify the current status of the task.")
                mbox.exec()
                return

            if Connection.insertTask(fieldsData):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("The task has been added successfully.")
                mbox.exec()
                Tasks.loadAllTasks()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("An error has occurred while trying to add the task.")
                mbox.exec()

        except Exception as error:
            print("(Tasks.saveTask) an error occurred while trying to save the new task: ", error)


    @staticmethod
    def modifyTask():
        try:
            fieldsData = [Globals.ui.txt_taskID,
                          Globals.ui.txt_clientName,
                          Globals.ui.txt_employeeName,
                          Globals.ui.txt_taskService,
                          Globals.ui.txt_taskPrice,
                          Globals.ui.txt_taskHours,
                          Globals.ui.cmb_taskStatus]

            if not Tasks._checkFields():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("Please fill all the fields")
                mbox.exec()
                return

            if Globals.ui.cmb_taskStatus.currentText() == "  -- selecciona --":
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("Please specify the current status of the task.")
                mbox.exec()
                return

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Modify")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("Do you want to modify the task's information?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.No:
                mbox.hide()
                return

            if Connection.updateTask(fieldsData):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("The task's information has been modified successfully.")
                mbox.exec()
                Tasks.loadAllTasks()

        except Exception as error:
            print("(Tasks.modifyTask) an error occurred while trying to modify the task: ", error)


    @staticmethod
    def deleteTask():
        try:
            taskId = Globals.ui.txt_taskID.text()

            if not taskId:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("No task selected.")
                mbox.exec()
                return

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Warning")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Delete Task?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                if Connection.deleteTask(taskId):
                    successMbox = QtWidgets.QMessageBox()
                    successMbox.setWindowTitle("Information")
                    successMbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    successMbox.setText("The task has been deleted successfully.")
                    successMbox.exec()
                    Tasks.loadAllTasks()
                    return

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("An error has occurred while trying to delete the task.")
                mbox.exec()
                return

            else:
                return

        except Exception as error:
            print("(Tasks.deleteTask) an error occurred while trying to delete the task: ", error)


    @staticmethod
    def clearTasksFields():
        try:
            fields = [Globals.ui.txt_taskID,
                      Globals.ui.txt_clientName,
                      Globals.ui.txt_employeeName,
                      Globals.ui.txt_taskService,
                      Globals.ui.txt_taskPrice,
                      Globals.ui.txt_taskHours]

            for field in fields:
                field.clear()
                field.setStyleSheet("background-color: rgb(255, 255, 255);")

            Globals.ui.txt_employeeName.setPlaceholderText("Enter the employee's name")
            Globals.ui.txt_clientName.setPlaceholderText("Enter the client's name")
            Globals.ui.txt_taskService.setPlaceholderText("Enter the service given to the client")
            Globals.ui.txt_taskPrice.setPlaceholderText("0.00")
            Globals.ui.txt_taskHours.setPlaceholderText("0")
            Globals.ui.cmb_taskStatus.setCurrentIndex(0)

        except Exception as error:
            print("(Tasks.clearTasksFields) an error occurred while trying to clear the fields:", error)
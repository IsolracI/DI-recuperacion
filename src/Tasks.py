from PyQt6 import QtWidgets, QtCore
from src.Connection import *
from src import Globals


class Tasks:

    @staticmethod
    def loadStatusOptions():
        statusOptions = ["  -- selecciona --", "Pendiente", "En curso", "Finalizada", "Facturada"]
        Globals.ui.cmb_taskStatus.addItems(statusOptions)


    @staticmethod
    def checkEmployee():
        existingEmployees = Connection.getEmployeesName()
        employee = Globals.ui.txt_employeeName.text()

        if employee not in existingEmployees:
            Globals.ui.txt_employeeName.setStyleSheet("background-color: #FFC0CB; color black")
            Globals.ui.txt_employeeName.setText(None)
            Globals.ui.txt_employeeName.setPlaceholderText("The employee entered doesn't exist in the database.")
        else:
            Globals.ui.txt_employeeName.setStyleSheet("background-color: rgb(255, 255, 220)")


    @staticmethod
    def checkClient():
        existingClients = Connection.getClientsName()
        client = Globals.ui.txt_clientName.text()

        if client not in existingClients:
            Globals.ui.txt_clientName.setStyleSheet("background-color: #FFC0CB; color black")
            Globals.ui.txt_clientName.setText(None)
            Globals.ui.txt_clientName.setPlaceholderText("The client entered doesn't exist in the database.")
        else:
            Globals.ui.txt_clientName.setStyleSheet("background-color: rgb(255, 255, 220)")


    @staticmethod
    def loadTasksTable():
        try:
            tasks = Connection.getTasks()

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
    def loadTaskInfo():
        try:
            selectedRow = Globals.ui.tbl_tasks.currentRow()
            taskId = Globals.ui.tbl_tasks.item(selectedRow, 0).text()

            taskInfo = Connection.getTaskInfo(taskId)

            widgets = [Globals.ui.lbl_taskID,
                       Globals.ui.txt_employeeName,
                       Globals.ui.txt_clientName,
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
            fieldsData = [Globals.ui.txt_employeeName.text(),
                          Globals.ui.txt_clientName.text(),
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

            if Globals.ui.cmb_taskService.currentText() == "  -- selecciona --":
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
                Tasks.loadTasksTable()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("An error has occurred while trying to add the task.")
                mbox.exec()

        except Exception as error:
            print("(Users.saveTask) an error occurred while trying to save the new task: ", error)



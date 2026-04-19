from PyQt6 import QtWidgets, QtCore
from src.Connection import *
from src import Globals


class Tasks:

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
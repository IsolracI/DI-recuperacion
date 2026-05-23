from PyQt6 import QtGui, QtWidgets, QtCore
from src.Users.UsersForm import *
from src.Connection import *
from src import Globals
import math

class UsersTable:
    show = "All"
    tableIndex = 0
    rowsPerPage = 13
    numPages = 1

    @staticmethod
    def setTableSettings():
        try:
            users = Connection.getUsers(UsersTable.show)
            UsersTable.numPages = max(1,math.ceil(len(users) / UsersTable.rowsPerPage))

        except Exception as error:
            print("(UsersTable.setTableSettings) an error occurred while trying to set the table's settings: ", error)


    @staticmethod
    def _checkButtons():
        try:
            if UsersTable.tableIndex <= 0:
                Globals.ui.btn_userTablePrevPage.setEnabled(False)
            else:
                Globals.ui.btn_userTablePrevPage.setEnabled(True)

            if UsersTable.tableIndex >= UsersTable.numPages - 1:
                Globals.ui.btn_userTableNextPage.setEnabled(False)
            else:
                Globals.ui.btn_userTableNextPage.setEnabled(True)

            UsersTable.loadUsersTable()

        except Exception as error:
            print("(UsersTable.checkButtons) an error occurred while trying to check the buttons: ", error)


    @staticmethod
    def loadUsersTable():
        """

        Carga los usuarios de la base de datos en la tabla de usuarios.

        :return: None

        """
        try:
            offset = UsersTable.rowsPerPage * UsersTable.tableIndex
            users = Connection.getUsersPage(UsersTable.rowsPerPage, offset, UsersTable.show)

            index = 0
            uiTable = Globals.ui.tbl_users
            uiTable.clearContents()
            uiTable.selectRow(0)

            for user in users:
                uiTable.setRowCount(index + 1)
                uiTable.setItem(index, 0, QtWidgets.QTableWidgetItem(str(user[1])))
                uiTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(user[2])))
                uiTable.setItem(index, 2, QtWidgets.QTableWidgetItem(str(user[3])))
                uiTable.setItem(index, 3, QtWidgets.QTableWidgetItem(str(user[4])))
                uiTable.setItem(index, 4, QtWidgets.QTableWidgetItem(str(user[5])))

                uiTable.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                uiTable.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)

                if user[5] == "Employee":
                    for col in range(uiTable.columnCount()):
                        item = (uiTable.item(index, col))
                        font = item.font()
                        font.setBold(True)
                        item.setFont(font)
                        item.setBackground(QtGui.QColor(250, 245, 245))

                index += 1

        except Exception as error:
            print("(UsersTable.loadUsersTable) an error occurred while trying to load the users table: ", error)

    @staticmethod
    def showAll():
        """

        Cambia la variable 'show' para mostrar todos los usuarios en la tabla de usuarios.

        :return: None

        """
        try:
            UsersTable.show = "All"
            UsersTable.tableIndex = 0
            UsersTable.setTableSettings()
            UsersTable._checkButtons()
            UsersTable.loadUsersTable()
        except Exception as error:
            print("(UsersTable.showAll) an error occurred while trying to change the table's configuration: ", error)

    @staticmethod
    def showEmployees():
        """

        Cambia la variable 'show' para mostrar solo los usuarios que son empleados en la tabla de usuarios.

        :return: None

        """
        try:
            UsersTable.show = "Employee"
            UsersTable.tableIndex = 0
            UsersTable.setTableSettings()
            UsersTable._checkButtons()
            UsersTable.loadUsersTable()
        except Exception as error:
            print("(UsersTable.showEmployees) an error occurred while trying to change the table's configuration: ", error)


    @staticmethod
    def showClients():
        """

        Cambia la variable 'show' para mostrar solo los usuarios que son clientes en la tabla de usuarios.

        :return: None

        """
        try:
            UsersTable.show = "Client"
            UsersTable.tableIndex = 0
            UsersTable.setTableSettings()
            UsersTable._checkButtons()
            UsersTable.loadUsersTable()
        except Exception as error:
            print("(UsersTable.showClients) an error occurred while trying to change the table's configuration: ", error)


    @staticmethod
    def goToNextPage():
        try:
            if UsersTable.tableIndex < UsersTable.numPages - 1:
                UsersTable.tableIndex += 1

            UsersTable._checkButtons()
            UsersTable.loadUsersTable()

        except Exception as error:
            print("(UsersTable.goToNextPage) an error occurred while trying to go to the next page: ", error)


    @staticmethod
    def goToPreviousPage():
        try:
            if UsersTable.tableIndex > 0:
                UsersTable.tableIndex -= 1

            UsersTable._checkButtons()
            UsersTable.loadUsersTable()

        except Exception as error:
            print("(UsersTable.goToPreviousPage) an error occurred while trying to go to the previous page: ", error)
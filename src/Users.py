from src.Connection import Connection
from PyQt6 import QtWidgets, QtCore
from src import Globals


class Users:
    show = "All"

    @staticmethod
    def loadUsersTable():
        try:
            users = Connection.getUsers(Users.show)

            index = 0
            uiTable = Globals.ui.tbl_users
            uiTable.clearContents()

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
                index += 1

        except Exception as error:
            print("(Users.loadUsersTable) an error occurred while trying to load the users table: ", error)


    @staticmethod
    def showAll():
        try:
            Users.show = "All"
            Users.loadUsersTable()
        except Exception as error:
            print("(Users.showAll) an error occurred while trying to change the table's configuration: ", error)


    @staticmethod
    def showEmployees():
        try:
            Users.show = "Employee"
            Users.loadUsersTable()
        except Exception as error:
            print("(Users.showEmployees) an error occurred while trying to change the table's configuration: ", error)


    @staticmethod
    def showClients():
        try:
            Users.show = "Client"
            Users.loadUsersTable()
        except Exception as error:
            print("(Users.showClients) an error occurred while trying to change the table's configuration: ", error)


    @staticmethod
    def loadUserInfo():
        try:
            selectedRow = Globals.ui.tbl_users.currentRow()
            userEmail = Globals.ui.tbl_users.item(selectedRow, 3).text()

            userData = Connection.getUserInfo(userEmail)

            fieldsData = [Globals.ui.txt_userDNI,
                          Globals.ui.txt_userName,
                          Globals.ui.txt_userAddress,
                          Globals.ui.txt_userMobile,
                          Globals.ui.txt_userEmail]

            for i in range(len(fieldsData)):
                if hasattr(fieldsData[i], "setText"):
                    fieldsData[i].setText(str(userData[i]))
                if hasattr(fieldsData[i], "setCurrentText"):
                    fieldsData[i].setCurrentText(str(userData[i]))

            if str(userData[5]) == "Employee":
                Globals.ui.rb_userEmployee.setChecked(True)
            else:
                Globals.ui.rb_userClient.setChecked(True)

        except Exception as error:
            print("(Users.loadUserInfo) There was an error while trying to show the users's info: ", error)


    @staticmethod
    def saveUser():
        try:
            fieldsData = [Globals.ui.txt_userDNI,
                          Globals.ui.txt_userName,
                          Globals.ui.txt_userAddress,
                          Globals.ui.txt_userMobile,
                          Globals.ui.txt_userEmail]

            userType = ""
            if Globals.ui.rb_userEmployee.isChecked():
                userType = "Employee"
            elif Globals.ui.rb_userClient.isChecked():
                userType = "Client"
            fieldsData.append(userType)

            if Connection.insertUser(fieldsData):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("The user has been added successfully.")
                mbox.exec()
                Users.loadUsersTable()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("An error has occurred while trying to add the user.")
                mbox.exec()

        except Exception as error:
            print("(Users.saveUser) an error occurred while trying to add the new user: ", error)


    @staticmethod
    def modifyUser():
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Modify")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("Do you want to modify the customer's information?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.No:
                mbox.hide()
                return

            fieldsData = [Globals.ui.txt_userDNI,
                          Globals.ui.txt_userName,
                          Globals.ui.txt_userAddress,
                          Globals.ui.txt_userMobile,
                          Globals.ui.txt_userEmail]

            userType = ""
            if Globals.ui.rb_userEmployee.isChecked():
                userType = "Employee"
            elif Globals.ui.rb_userClient.isChecked():
                userType = "Client"
            fieldsData.append(userType)

            if Connection.updateUser(fieldsData):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("The User's information has been modified.")
                mbox.exec()
                Users.loadUsersTable()

        except Exception as error:
            print("(Users.modifyUser) There was an error while modifying the customer's data: ", error)


    @staticmethod
    def deleteUser():
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Warning")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Delete User?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                dni = Globals.ui.txt_userDNI.text()

                if Connection.deleteUser(dni):
                    successMbox = QtWidgets.QMessageBox()
                    successMbox.setWindowTitle("Information")
                    successMbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    successMbox.setText("The user has been deleted successfully.")
                    successMbox.exec()
                    Users.loadUsersTable()
                    return

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Error")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setText("An error has occurred while trying to delete the user.")
                mbox.exec()
                return

            else:
                return

        except Exception as error:
            print("(Users.deleteUser) There was an error while trying to delete the user: ", error)


    @staticmethod
    def clearUsersFields():
        try:
            fieldsData = [Globals.ui.txt_userDNI,
                          Globals.ui.txt_userName,
                          Globals.ui.txt_userAddress,
                          Globals.ui.txt_userMobile,
                          Globals.ui.txt_userEmail]

            for data in fieldsData:
                data.clear()

        except Exception as error:
            print("(Users.clearUsersFields) There was an error while trying to clear the users fields: ", error)

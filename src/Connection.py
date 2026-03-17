from PyQt6 import QtWidgets, QtSql
import os


class Connection:

    @staticmethod
    def dbConnection():
        """

        Establece la conexión con la base de datos SQLite y devuelve un booleano
        indicando si la conexión tuvo exito o no

        :return: True si la conexión es válida, False en caso contrario
        :rtype: bool

        """


        dbURL = "../bbdd/bbdd.sqlite"

        if not os.path.isfile(dbURL):
            QtWidgets.QMessageBox.critical(None, "Error", "The database file does not exist.",
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(dbURL)

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Error", "We could not connect to the database.",
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("SELECT  name"
                   "    FROM sqlite_master"
                   "    WHERE type='table';")

        if not query.next():
            QtWidgets.QMessageBox.critical(None, "Error", "The database is empty or invalid",
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

        else:
            QtWidgets.QMessageBox.information(None, "Info", "We successfully connected to the database.",
                                              QtWidgets.QMessageBox.StandardButton.Ok)
            return True


         #######################
    #### ##--## USERS ##--## ####   ##########################################################################################
         #######################

    @staticmethod
    def getUsers(type):
        try:
            usersList = []
            query = QtSql.QSqlQuery()

            if type == "Client" or type == "Employee":
                query.prepare("SELECT  *"
                              "    FROM Users"
                              "    WHERE User_Type = :type")
                query.bindValue(":type", type)

            else:
                query.prepare("SELECT  *"
                              "    FROM Users")

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    usersList.append(row)

            return usersList

        except Exception as error:
            print("(Connection.getUsers) an error occurred while trying to get the users:", error)


    @staticmethod
    def insertUser(data):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO Users "
                          "(DNI, Name, Address, Phone_number, Email, User_Type)"
                          "VALUES "
                          "(:DNI, :Name, :Address, :Phone_number, :Email, :UserType)")

            valuesOrder = [":DNI", ":Name", ":Address", ":Phone_number", ":Email", ":UserType"]
            radialButtons = ["Employee", "Client"]

            for i in range(len(valuesOrder)):
                value = data[i]
                if hasattr(value, "text"):
                    valueText = value.text()
                elif hasattr(value, "currentText"):
                    valueText = value.currentText()
                else:
                    valueText = str(value)
                query.bindValue(valuesOrder[i], valueText)

            if not query.exec():
                print("(Connection.addUser) An error ocurred while trying to add the user: ", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.addUser) an error occurred while trying to add the user to the database.", error)

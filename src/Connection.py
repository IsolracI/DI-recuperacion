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
    def getUsers(type="All"):
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
            print("(Connection.getUsers) an error occurred while trying to get the users from the database:", error)


    @staticmethod
    def getUsersOrderByName():
        try:
            usersList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  *"
                          "    FROM Users"
                          "    ORDER BY Name")

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    usersList.append(row)

            return usersList

        except Exception as error:
            print("(Connection.getUsersOrderByName) an error occurred while trying to get the users from the database:", error)


    @staticmethod
    def getClientsName():
        try:
            clientsList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  Name"
                          "    FROM Users"
                          "    WHERE User_Type = 'Client'")

            if query.exec():
                while query.next():
                    clientsList.append(query.value("Name"))

            return clientsList

        except Exception as error:
            print("(Connection.getClientsName) an error occurred while trying to get the clients' name from the database:", error)


    @staticmethod
    def getEmployeesName():
        try:
            employeesList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  Name"
                          "    FROM Users"
                          "    WHERE User_Type = 'Employee'")

            if query.exec():
                while query.next():
                    employeesList.append(query.value("Name"))

            return employeesList

        except Exception as error:
            print("(Connection.getEmployeesName) an error occurred while trying to get the employees' name from the database:", error)


    @staticmethod
    def getUserInfo(email):
        try:
            userData = []
            query = QtSql.QSqlQuery()
            email = str(email).strip()
            query.prepare("SELECT  *"
                          "    FROM Users"
                          "    WHERE Email = :Email")
            query.bindValue(":Email", email)

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        userData.append(query.value(i))
            return userData

        except Exception as error:
            print("(Connection.getUserInfo) An error ocurred while trying to get the user's info from the database: ", error)


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
                print("(Connection.insertUser) An error ocurred while trying to add the user to the database: ", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.insertUser) an error occurred while trying to add the user to the database: ", error)


    @staticmethod
    def updateUser(data):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE Users set "
                          "Name = :Name, Address = :Address,"
                          "Phone_number = :Phone_number, Email = :Email, User_Type = :User_Type "
                          "WHERE DNI = :DNI;")

            valuesOrder = [":DNI", ":Name", ":Address", ":Phone_number", ":Email", ":User_Type"]
            radialButtons = ["Employee", "Client"]

            for i in range(len(valuesOrder)):
                try:
                    if data[i] in radialButtons:
                        valueText = data[i]
                    else:
                        valueText = str(data[i].text())
                except AttributeError:
                    valueText = str(data[i].currentText())
                query.bindValue(valuesOrder[i], valueText)

            if not query.exec():
                print(query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.updateUser) An error occurred while trying to update the user's data in the database: ", error)


    @staticmethod
    def deleteUser(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM Users "
                          "    WHERE DNI = :DNI")
            query.bindValue(":DNI", dni)

            if not query.exec():
                print(query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.deleteUser) An error occurred while trying to delete the user from the database: ", error)


         #######################
    #### ##--## TASKS ##--## ####   ##########################################################################################
         #######################

    @staticmethod
    def getTasks():
        try:
            tasksList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  *"
                          "    FROM Tasks")

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    tasksList.append(row)

            return tasksList

        except Exception as error:
            print("(Connection.getTasks) An error occurred while trying to get the tasks from the database:", error)


    @staticmethod
    def insertTask(data):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO Tasks "
                          "(Employee, Client, Service, Price, Hours, Status)"
                          "VALUES "
                          "(:Employee, :Client, :Service, :Price, :Hours, :Status)")

            valuesOrder = [":Employee", ":Client", ":Service", ":Price", ":Hours", ":Status"]

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
                print("(Connection.insertTask) An error ocurred while trying to add the task to the database: ", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.insertTask) an error occurred while trying to add the user to the database: ", error)



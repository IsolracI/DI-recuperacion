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
        dbURL = "bbdd/bbdd.sqlite"

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
        """

        Obtiene los usuarios almacenados en la base de datos.

        :param type: Tipo de usuario que se desea obtener
        :type type: str
        :return: Lista con los datos de los usuarios encontrados
        :rtype: list

        """
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
    def getUsersOrderByName(type="All"):
        """

        Obtiene todos los usuarios ordenados alfabéticamente por nombre.

        :return: Lista con los usuarios ordenados por nombre
        :rtype: list

        """
        try:
            usersList = []
            query = QtSql.QSqlQuery()

            if type == "Client" or type == "Employee":
                query.prepare("SELECT  *"
                              "    FROM Users"
                              "    WHERE User_Type = :type"
                              "    ORDER BY Name")
                query.bindValue(":type", type)

            else:
                query.prepare("SELECT  *"
                              "    FROM Users"
                              "    ORDER BY Name")

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    usersList.append(row)

            return usersList

        except Exception as error:
            print("(Connection.getUsersOrderByName) an error occurred while trying to get the users from the database: ", error)


    @staticmethod
    def getUsersPage(limit, offset, userType="All"):
        try:
            usersList = []
            query = QtSql.QSqlQuery()

            if userType in ["Client", "Employee"]:
                query.prepare("SELECT  *"
                              "    FROM Users"
                              "    WHERE User_Type = :type"
                              "    LIMIT :limit OFFSET :offset")
                query.bindValue(":type", userType)

            else:
                query.prepare("SELECT  *"
                              "    FROM Users"
                              "    LIMIT :limit OFFSET :offset")

            query.bindValue(":limit", limit)
            query.bindValue(":offset", offset)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    usersList.append(row)

            return usersList

        except Exception as error:
            print("(Connection.getUsersPage) an error occurred while trying to get the users from the database: ", error)


    @staticmethod
    def getClientsName():
        """

        Obtiene los nombres de todos los usuarios registrados
        como clientes.

        :return: Lista con los nombres de los clientes
        :rtype: list

        """
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
        """

        Obtiene los nombres de todos los usuarios registrados
        como empleados.

        :return: Lista con los nombres de los empleados
        :rtype: list

        """
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
        """

        Obtiene toda la información de un usuario a partir de su
        correo electrónico.

        :param email: Correo electrónico del usuario
        :type email: str
        :return: Lista con la información del usuario
        :rtype: list

        """
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
        """

        Inserta un nuevo usuario en la base de datos utilizando
        los datos proporcionados desde la interfaz gráfica.

        :param data: Lista con los datos del usuario
        :type data: list
        :return: True si el usuario se insertó correctamente, False en caso contrario
        :rtype: bool

        """
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
        """

        Actualiza la información de un usuario existente utilizando
        los nuevos datos proporcionados desde la interfaz gráfica y
        el DNI como identificador principal.

        :param data: Lista con los nuevos datos del usuario
        :type data: list
        :return: True si la actualización fue correcta, False en caso contrario
        :rtype: bool

        """
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
                print("(Connection.updateUser) An error occurred while trying to update the user's data in the database: ", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.updateUser) An error occurred while trying to update the user's data in the database: ", error)


    @staticmethod
    def deleteUser(dni):
        """

        Elimina de la base de datos el usuario cuyo DNI sea
        igual al DNI proporcionado.

        :param dni: DNI del usuario que se desea eliminar
        :type dni: str
        :return: True si el usuario se eliminó correctamente, False en caso contrario
        :rtype: bool

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM Users "
                          "    WHERE DNI = :DNI")
            query.bindValue(":DNI", dni)

            if not query.exec():
                print("(Connection.deleteUser) An error occurred while trying to delete the user from the database: ", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.deleteUser) An error occurred while trying to delete the user from the database: ", error)


         #######################
    #### ##--## TASKS ##--## ####   ##########################################################################################
         #######################

    @staticmethod
    def getTasks():
        """

        Obtiene todas las tareas almacenadas en la base de datos.

        :return: Lista con todas las tareas registradas
        :rtype: list

        """
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
    def getEmployeeTasks(employee):
        """

        Obtiene las tareas asignadas a un empleado específico.

        :param employee: Nombre del empleado
        :type employee: str
        :return: Lista con las tareas del empleado
        :rtype: list

        """
        try:
            tasksList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  *"
                          "    FROM Tasks "
                          "    WHERE Employee = :Employee ")
            query.bindValue(":Employee", employee)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    tasksList.append(row)

            return tasksList

        except Exception as error:
            print("(Connection.getEmployeeTasks) An error occurred while trying to get the employee's tasks from the database:", error)


    @staticmethod
    def getClientTasks(client):
        """

        Obtiene las tareas asociadas a un cliente específico.

        :param client: Nombre del cliente
        :type client: str
        :return: Lista con las tareas del cliente
        :rtype: list

        """
        try:
            tasksList = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  *"
                          "    FROM Tasks "
                          "    WHERE Client = :Client ")
            query.bindValue(":Client", client)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    tasksList.append(row)

            return tasksList

        except Exception as error:
            print("(Connection.getClientTasks) An error occurred while trying to get the client's tasks from the database:", error)


    @staticmethod
    def getTaskInfo(taskId):
        """

        Obtiene toda la información de una tarea concreta.

        :param taskId: Identificador de la tarea
        :type taskId: int
        :return: Lista con la información de la tarea
        :rtype: list

        """
        try:
            taskInfo = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT  *"
                          "    FROM Tasks "
                          "    WHERE Task_ID = :TaskId")
            query.bindValue(":TaskId", taskId)

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        taskInfo.append(query.value(i))
            return taskInfo

        except Exception as error:
            print("(Connection.getTaskInfo) An error occurred while trying to get the task's info from the database:", error)


    @staticmethod
    def insertTask(data):
        """

        Inserta una nueva tarea en la base de datos utilizando
        los datos proporcionados desde la interfaz gráfica.

        :param data: Lista con los datos de la tarea
        :type data: list
        :return: True si la tarea se insertó correctamente, False en caso contrario
        :rtype: bool

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO Tasks "
                          "(Client, Employee, Service, Price, Hours, Status)"
                          "VALUES "
                          "(:Client, :Employee, :Service, :Price, :Hours, :Status)")

            valuesOrder = [":Client", ":Employee", ":Service", ":Price", ":Hours", ":Status"]

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


    @staticmethod
    def updateTask(data):
        """

        Actualiza la información de una tarea existente utilizando
        los nuevos datos proporcionados desde la interfaz gráfica y
        el ID de la tarea como identificador principal.

        :param data: Lista con los nuevos datos de la tarea
        :type data: list
        :return: True si la actualización fue correcta, False en caso contrario
        :rtype: bool

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE Tasks set "
                          "    Client = :Client, Employee = :Employee, Service = :Service, Price = :Price, Hours = :Hours, Status = :Status "
                          "WHERE Task_ID = :Task_ID")

            valuesOrder = [":Task_ID", ":Client", ":Employee", ":Service", ":Price", ":Hours", ":Status"]

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
                print("(Connection.updateTask) An error occurred while trying to update the task's data in the database:", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.updateTask) An error occurred while trying to update the task's data in the database:", error)


    @staticmethod
    def deleteTask(taskId):
        """

        Elimina de la base de datos la tarea cuyo ID sea
        igual al ID proporcionado.

        :param taskId: Identificador de la tarea que se desea eliminar
        :type taskId: int
        :return: True si la tarea se eliminó correctamente, False en caso contrario
        :rtype: bool

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM Tasks"
                          "    WHERE Task_ID = :TaskId")
            query.bindValue(":TaskId", taskId)

            if not query.exec():
                print("(Connection.deleteTask) An error occurred while trying to delete the task from the database:", query.lastError().text())
                return False
            return True

        except Exception as error:
            print("(Connection.deleteTask) An error occurred while trying to delete the task from the database:", error)


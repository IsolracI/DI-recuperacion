from PyQt6 import QtWidgets

class Events:

    @staticmethod
    def resizeTable(table):
        """

        Ajusta automáticamente el tamaño de las columnas y aplica formato
        en negrita a los encabezados de la tabla especificada.

        :param table: Tabla de la interfaz que se desea redimensionar
        :type table: QtWidgets.QTableWidget
        :return: None

        """
        try:
            header = table.horizontalHeader()

            for i in range(header.count()):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                headerItems = table.horizontalHeaderItem(i)
                # Cabezera en Negrilla
                font = headerItems.font()
                font.setBold(True)
                header.setFont(font)

        except Exception as error:
            print(f"(Events.resizeTable) There was an error while trying to resize the table {table}: ", error)
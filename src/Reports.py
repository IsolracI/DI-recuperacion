from reportlab.pdfgen import canvas
from src.Connection import *
from PIL import Image
import datetime
import os

class Reports:

    @staticmethod
    def reportHeader(reportCanvas, title):
        try:
            path_logo = "..\\assets\\amiyapog.png"
            logo = Image.open(path_logo)
            if isinstance(logo, Image.Image):
                reportCanvas.setFont('Helvetica-Bold', 10)
                reportCanvas.drawString(75, 775, "EMPRESA TEIS")
                reportCanvas.drawCentredString(300, 670, title)
                # Logo
                reportCanvas.drawImage(path_logo, 490, 745, width=64, height=78)
                # Company details
                reportCanvas.setFont('Helvetica', 9)
                reportCanvas.drawString(55, 757, "CIF: B12345678")
                reportCanvas.drawString(55, 742, "Dirección: Calle Galicia, 123")
                reportCanvas.drawString(55, 727, "Vigo 36215 - España")
                reportCanvas.drawString(55, 712, "Teléfono: +34 986 123 456")
                reportCanvas.drawString(55, 697, "Email: teis@mail.com")
                reportCanvas.rect(30, 690, 160, 80)
            else:
                print('No se pudo cargar el logo')

        except Exception as e:
            print("(Reports.header) an error occurred while trying to make the header", e)

    @staticmethod
    def reportFooter(reportCanvas, title):
        """

        Dibuja el pie de página del documento PDF.

        :param reportCanvas: Lienzo del PDF sobre el que se dibuja el contenido
        :type reportCanvas: reportlab.pdfgen.canvas.Canvas
        :param title: Título del informe o documento
        :type title: str
        :return: None

        """
        try:
            reportCanvas.line(35, 60, 525, 60)
            reportCanvas.line(35, 50, 380, 50)
            day = datetime.date.today()
            day = day.strftime("%d/%m/%Y %H:%M:%S")
            reportCanvas.setFont("Helvetica", 7)
            reportCanvas.drawString(35, 40, day)
            reportCanvas.drawString(35, 30, title)
            reportCanvas.drawString(440, 47, str("Página: " + str(reportCanvas.getPageNumber())))

        except Exception as error:
            print("(Reports.footer) an error occurred while trying to make the footer: ", error)


    @staticmethod
    def usersReport():
        """

        Genera un informe en PDF con la lista de usuarios.

        :return: None

        """
        try:
            rootPath = "..\\reports"
            data = datetime.datetime.now().strftime("%d_%m_%Y %H_%M_%S")
            usersReportName = data + "_reportUsers.pdf"
            pdfPath = os.path.join(rootPath, usersReportName)
            reportCanvas = canvas.Canvas(pdfPath)
            records = Connection.getUsersOrderByName()
            items = ["NAME", "PHONE", "EMAIL", "TYPE"]
            reportCanvas.setFont("Helvetica-Bold", 10)
            reportCanvas.drawCentredString(100, 650, str(items[0]))
            reportCanvas.drawCentredString(225, 650, str(items[1]))
            reportCanvas.drawCentredString(355, 650, str(items[2]))
            reportCanvas.drawCentredString(465, 650, str(items[3]))
            reportCanvas.line(35, 645, 525, 645)
            reportCanvas.line(35, 663, 525, 663)
            y = 630

            Reports.reportHeader(reportCanvas, "Listado de empleados")
            Reports.reportFooter(reportCanvas, "Listado de empleados")

            for record in records:
                if y <= 90:
                    reportCanvas.setFont("Helvetica-Oblique", 8)
                    reportCanvas.drawString(450, 75, "Página siguiente...")
                    reportCanvas.showPage() # crea una nueva página
                    reportCanvas.drawCentredString(100, 800, str(items[0]))
                    reportCanvas.drawCentredString(225, 800, str(items[1]))
                    reportCanvas.drawCentredString(355, 800, str(items[2]))
                    reportCanvas.drawCentredString(465, 800, str(items[3]))
                    reportCanvas.line(35, 645, 525, 645)
                    y = 780

                reportCanvas.setFont("Helvetica", 8)
                reportCanvas.drawCentredString(100, y, str(record[1]))
                reportCanvas.drawCentredString(225, y, str(record[3]))
                reportCanvas.drawCentredString(355, y, str(record[4]))
                reportCanvas.drawCentredString(465, y, str(record[5]))
                y -= 20

            reportCanvas.save()

            for file in os.listdir(rootPath):
                if file.endswith(usersReportName):
                    os.startfile(pdfPath)

        except Exception as error:
            print("(Reports.usersReport) an error occurred while trying to make the users reports: ", error)
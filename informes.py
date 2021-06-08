from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyQt5 import QtSql
from datetime import datetime, date
import os, var, random


class Informes:
    def cabecera(self):
        try:
            logo = '.\\img\icono.png'
            var.informe.drawImage(logo, 480, 760)
            var.titulo = 'LISTADO RUTAS'
            var.informe.drawString(230, 750, var.titulo)
            var.informe.line(60, 740, 545, 740)
            var.informe.line(60, 735, 545, 735)
            var.informe.setFont('Helvetica-Bold', size=16)
            var.informe.drawString(60, 790, 'TRANSPORTES TEIS')

        except Exception as error:
            print('Error cabecera informe: %s' % str(error))

    def informeRutas(self):
        try:
            informe = random.randint(1, 1000000)
            var.informe = canvas.Canvas('./reportes/' + str(informe) + '.pdf', pagesize=A4)
            Informes.cabecera(self) #preguntar por qué se hace sobre la clase
            Informes.pie(self)
            var.informe.setFont('Helvetica-Bold', size=10)
            var.informe.drawString(73, 720, 'Cod.')
            var.informe.drawString(112, 720, 'Fecha')
            var.informe.drawString(160, 720, 'Matrícula')
            var.informe.drawString(230, 720, 'Conductor')
            var.informe.drawString(345, 720, 'KmIni.')
            var.informe.drawString(390, 720, 'KmFin.')
            var.informe.drawString(435, 720, 'Tarifa')
            var.informe.drawString(495, 720, 'TOTAL')
            var.informe.line(60, 715, 545, 715)
            var.informe.line(60, 740, 60, 60)
            var.informe.line(545, 740, 545, 60)

            rootPath = '.\\reportes'
            cont = 0
            query = QtSql.QSqlQuery()
            query.prepare('select * from rutas')

            if query.exec_():
                i = 80
                j = 690 #altura desde la que empieza a listar
                total = 0.00
                while query.next():
                    if j<=80:
                        var.informe.drawString(440,70, 'Página siguiente...')
                    var.informe.setFont('Helvetica', size=10)
                    var.informe.drawString(i, j, str(query.value(0)))
                    var.informe.drawRightString(i + 70, j, str(query.value(1)))
                    var.informe.drawString(i + 80, j, str(query.value(2)))
                    var.informe.drawString(i + 150, j, str(query.value(3)))
                    var.informe.drawRightString(i + 290, j, str(query.value(4)))
                    var.informe.drawRightString(i + 340, j, str(query.value(5)))
                    var.informe.drawRightString(i + 380, j, str(query.value(6)))
                    kmt = int(query.value(5)) - int(query.value(6))
                    tarifatotal = float(kmt) * float(query.value(6))

                    var.informe.drawRightString(i + 450, j, str('{0:.2f}'.format(float(tarifatotal)) + ' €'))


                    #van el resto de los values
                    j = j-25
                    total = float(total) + float(tarifatotal)
                iva = float(total) * 0.21
                var.informe.setFont('Helvetica-Bold', size=10)
                var.informe.drawRightString(535, 95, 'IVA:   ' + ('{0:.2f}'.format(iva))+ ' €')
                var.informe.drawRightString(535, 75, 'TOTAL:   ' + ('{0:.2f}'.format(total)) + ' €')

                var.informe.setFont('Helvetica-Oblique', size=7)
                var.informe.drawAlignedString(115, 105, 'Observaciones')
            print(iva)
            print(total)
            var.informe.save()
            for file in os.listdir(rootPath):
                if file.endswith(str(informe) + '.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont += 1

        except Exception as error:
            print('Error cuerpo informe: %s' % str(error))

    def pie(self):
        try:
            var.informe.line(60, 60, 545, 60)
            var.informe.line(60, 120, 545, 120)
            var.informe.line(440, 120, 440, 60)
            dia = datetime.now().day
            mes = datetime.now().month
            ano = datetime.now().year
            var.informe.setFont('Helvetica-Oblique', size=8)
            var.informe.drawString(250, 50, var.titulo)
            var.informe.drawString(500, 50, str(dia) + '/' + str(mes) + '/' + str(ano))


        except Exception as error:
            print('Error pie informe: %s' % str(error))
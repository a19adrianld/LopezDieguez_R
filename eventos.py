import sys

from ventana import *
import var, conexion


class Eventos():
    '''
    Eventos del programa. Xestión Furgonetas.
    '''

    def matCapital():
        '''
        Pone en mayúsculas la matrícula
        :return:
        '''
        matricula = var.ui.txtMatricula.text()
        var.ui.txtMatricula.setText(matricula.upper())


    def cargaFurgo(self):
        try:
            var.newfurgo = []
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in furgo:
                var.newfurgo.append(i.text())
            conexion.Conexion.altaFurgo(var.newfurgo)
            conexion.Conexion.listarFurgo(self)

            conexion.Conexion.cargarCmbM(var.ui.cmbMat)

        except Exception as error:
            print('Error carga furgo: %s: ' % str(error))


#pasar datos arriba para modificarlos



    def limpiaFurgo(self):
        try:
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in range(len(furgo)):
                furgo[i].setText('')
        except Exception as error:
            print('Error limpiar furgoneta: %s: ' % str(error))

    def bajaFurgo(self):
        try:
            matricula = var.ui.txtMatricula.text()
            conexion.Conexion.deleteFurgo(matricula)
            conexion.Conexion.listarFurgo(self)

            conexion.Conexion.cargarCmbM(var.ui.cmbMat)

        except Exception as error:
            print('Error baja furgo: %s: ' % str(error))

    def modifFurgo(self):
        try:
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            furgomodif = []
            for i in furgo:
                furgomodif.append(i.text())
            conexion.Conexion.modifFurgo(furgomodif)
            conexion.Conexion.listarFurgo(self)

            conexion.Conexion.cargarCmbM(var.ui.cmbMat)

        except Exception as error:
            print('Error modificar furgo: %s: ' % str(error))

    def datosUnoFurgo(self):
        try:
            fila = var.ui.tabFurgo.selectedItems()
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            if fila:
                fila = [dato.text() for dato in fila]
                #carga los datos de la tabla en una lista furgo
                for i, dato in enumerate(furgo):
                    dato.setText(fila[i])
        except Exception as error:
            print('Error datos furgo: €s: ' % str(error))


    '''
    Eventos del programa. Xestión conductores.
    '''

    def altaCon(self):
        try:
            var.newcon = []
            con = [var.ui.txtDni, var.ui.txtNombre]
            for i in con:
                var.newcon.append(i.text())
            if Eventos.validoDni():
                conexion.Conexion.nuevoCon(var.newcon)
                conexion.Conexion.listarCon(self)

                conexion.Conexion.cargarCmbC(var.ui.cmbCon)

            else:
                QtWidgets.QMessageBox.critical(None, 'Datos no válidos.',
                                                  'Comprueba DNI')

        except Exception as error:
            print('Error carga furgo: %s: ' % str(error))



    def datosUnCon(self):
        try:
            fila = var.ui.tabConductor.selectedItems()
            con = [var.ui.txtDni, var.ui.txtNombre]
            if fila:
                fila = [dato.text() for dato in fila]
                #carga los datos de la tabla en una lista furgo


                for i, dato in enumerate(con):
                    dato.setText(fila[i])
            var.ui.lblValidar.setText('')
        except Exception as error:
            print('Error datos furgo: €s: ' % str(error))


    def bajaCon(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.deleteCon(dni)
            conexion.Conexion.listarCon(self) #actualizar la tabla

            conexion.Conexion.cargarCmbC(var.ui.cmbCon)

        except Exception as error:
            print('Error baja conductor: %s: ' % str(error))


    def dniCapital():
        '''
        Pone en mayúsculas la matrícula
        :return:
        '''
        dni = var.ui.txtDni.text()
        var.ui.txtDni.setText(dni.upper())


    def nomCapital():
        '''
        Pone en mayúsculas la matrícula
        :return:
        '''
        nombre = var.ui.txtNombre.text()
        var.ui.txtNombre.setText(nombre.title())


    def modifCon(self):
        try:
            print('hola')
            con = [var.ui.txtDni, var.ui.txtNombre]
            conmodif = []
            for i in con:
                conmodif.append(i.text())
            conexion.Conexion.modifCon(conmodif)
            conexion.Conexion.listarCon(self)

            conexion.Conexion.cargarCmbC(var.ui.cmbCon)

        except Exception as error:
            print('Error modificar conductor: %s: ' % str(error))
            

    def limpiaCon(self):
        try:
            con = [var.ui.txtDni, var.ui.txtNombre]
            for i in range(len(con)):
                con[i].setText('')
        except Exception as error:
            print('Error limpiar conductor: %s: ' % str(error))

    def validoDni():
        try:
            dni = var.ui.txtDni.text()
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control

        except Exception as error:
            print('Error módulo validar DNI %s' % str(error))
            return None


    #GESTION RUTAS

    def abrirCalendar(self):
        try:
            var.dlgCalendar.show()

        except Exception as error:
            print('Error abrir calendario' % str(error))
            return None


    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.dlgCalendar.hide()

        except Exception as error:
            print('Error abrir calendario' % str(error))
            return None


    def calculaDistancia():
        try:
            inicio = int(var.ui.txtKmi.text())
            final = int(var.ui.txtKmf.text())
            if final <= inicio:
                var.ui.lblKmtotal.setStyleSheet('QLabel {color:red;}')
                var.ui.lblKmtotal.setText('Comprueba los km')
            else:
                var.ui.lblKmtotal.setStyleSheet('QLabel {color:red;}')
                var.ui.lblKmtotal.setText(str(final-inicio))
        except Exception as error:
            print('Error calcular distancia' % str(error))
            return None


    def calculaTarifa(self):
        try:
            coste = []
            coste = conexion.Conexion.cargarTarifas(self) #aquí le pasamos el array de floats que cogimos de conexion cargarTarifas
            kmTot = int(var.ui.lblKmtotal.text())
            print(coste)
            if var.ui.rbtLocal.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[0]) + '€')) #ese coste[0] es el primer valor del array
            if var.ui.rbtProvincial.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[1]) + '€'))
            if var.ui.rbtRegional.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot) * coste[2]) + '€'))
            if var.ui.rbtNacional.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[3]) + '€'))

        except Exception as error:
            print('Error calcular tarifa ' % str(error))


    '''eventos tab rutas'''
    def altaRuta(self):
        try:
            var.newruta = []
            ruta = [var.ui.lblRuta, var.ui.txtFecha, var.ui.cmbMat, var.ui.cmbCon, var.ui.txtKmi, var.ui.txtKmf, var.ui.kmTot] #TODO CODE
            for i in furgo:
                var.newfurgo.append(i.text())
            conexion.Conexion.altaFurgo(var.newfurgo)
            conexion.Conexion.listarFurgo(self)

            conexion.Conexion.cargarCmbM(var.ui.cmbMat)

        except Exception as error:
            print('Error carga furgo: %s: ' % str(error))


    # '''ESTO ESTABA REPETIDO

    # eventos generales
    # '''
    # def Salir(self):
    #     try:
    #         ret = QtWidgets.QMessageBox.question(None, 'Salir',
    #                                        '¿Desea Salir del Programa?')
    #         if ret == QtWidgets.QMessageBox.Yes:
    #             sys.exit()
    #         else:
    #             QtWidgets.QMessageBox.hide
    #
    #
    #     except Exception as error:
    #         print('Error salir manu ' % str(error))



    def validarDni():
        try:
            if Eventos.validoDni():
                #dni = var.ui.txtDni.text()
                var.ui.lblValidar.setStyleSheet('QLabel {color:green;}')
                var.ui.lblValidar.setText('V')
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidar.setText('F')


        except Exception as error:
            print('Error módulo validar DNI %s' % str(error))
            return None


    #GESTION RUTAS

    def abrirCalendar(self):
        try:
            var.dlgCalendar.show()

        except Exception as error:
            print('Error abrir calendario' % str(error))
            return None


    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.dlgCalendar.hide()

        except Exception as error:
            print('Error abrir calendario' % str(error))
            return None


    def calculaDistancia():
        try:
            inicio = int(var.ui.txtKmi.text())
            final = int(var.ui.txtKmf.text())
            if final <= inicio:
                var.ui.lblKmtotal.setStyleSheet('QLabel {color:red;}')
                var.ui.lblKmtotal.setText('Comprueba los km')
            else:
                var.ui.lblKmtotal.setStyleSheet('QLabel {color:red;}')
                var.ui.lblKmtotal.setText(str(final-inicio))
        except Exception as error:
            print('Error calcular distancia' % str(error))
            return None


    def calculaTarifa(self):
        try:
            coste = [] #no hace falta
            coste = conexion.Conexion.cargarTarifas(self) #aquí le pasamos el array de floats que cogimos de conexion cargarTarifas
            kmTot = int(var.ui.lblKmtotal.text())
            print(coste)
            if var.ui.rbtLocal.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[0]))) #ese coste[0] es el primer valor del array
            if var.ui.rbtProvincial.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[1])))
            if var.ui.rbtRegional.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot) * coste[2])))
            if var.ui.rbtNacional.isChecked():
                var.ui.lblPrecio.setText(str('{0:.2f}'.format(float(kmTot)* coste[3])))

        except Exception as error:
            print('Error calcular tarifa ' % str(error))


    '''eventos tab rutas'''
    def altaRuta(self):
        try:
            var.newruta = []
            coste = conexion.Conexion.cargarTarifas(self)
            mitarifa = 0.00
            if var.ui.rbtLocal.isChecked():
                mitarifa = coste[0] #ese coste[0] es el primer valor del array
            if var.ui.rbtProvincial.isChecked():
                mitarifa = coste[1]
            if var.ui.rbtRegional.isChecked():
                mitarifa = coste[2]
            if var.ui.rbtNacional.isChecked():
                mitarifa = coste[3]

            # ruta = [var.ui.txtFecha, var.ui.cmbMat.currentData(var.ui.cmbMat.currentIndex()), var.ui.cmbCon.currentData(var.ui.cmbCon.currentIndex()), var.ui.txtKmi, var.ui.txtKmf, var.ui.lblKmtotal, var.ui.lblPrecio, mitarifa]
            # for i in ruta:
            #     var.newruta.append(i.text())

            ruta = [var.ui.txtFecha.text(), var.ui.cmbMat.currentText(), var.ui.cmbCon.currentText(), var.ui.txtKmi.text(), var.ui.txtKmf.text(),  mitarifa]
            for i in ruta:
                var.newruta.append(i)

            conexion.Conexion.altaRuta(var.newruta)
            conexion.Conexion.listarRuta(self)

        except Exception as error:
            print('Error carga ruta: %s: ' % str(error))


    # def datosUnaRuta(self):
    #     try:
    #         fila = var.ui.tabRutas.selectedItems()
    #         if fila:
    #             fila = [dato.text() for dato in fila]
    #             #carga los datos de la tabla en una lista furgo
    #         var.ui.lblRuta.setText(str(fila[0]))
    #         var.ui.txtFecha.setText(str(fila[1]))
    #         var.ui.cmbMat.setCurrentText(str(fila[2]))
    #         var.ui.cmbCon.setCurrentText(str(fila[3]))
    #         var.ui.lblKmtotal.setText(str(fila[4]))
    #         var.ui.lblPrecio.setText(str(fila[6]))
    #
    #     except Exception as error:
    #         print('Error datos furgo: €s: ' % str(error))

    def datosUnaRuta(self):
        try:
            fila = var.ui.tabRutas.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
                #carga los datos de la tabla en una lista furgo

            conexion.Conexion.listarUnaRuta(int(fila[0]))


        except Exception as error:
            print('Error datos furgo: €s: ' % str(error))


    def bajaRuta(self):
        try:
            numruta = int(var.ui.lblRuta.text())
            conexion.Conexion.deleteRuta(numruta)
            conexion.Conexion.listarRuta(self)


        except Exception as error:
            print('Error baja ruta: %s: ' % str(error))

    def limpiaRuta(self):
        try:
            ruta = [var.ui.lblRuta, var.ui.txtFecha, var.ui.txtKmi, var.ui.txtKmf, var.ui.lblKmtotal, var.ui.lblPrecio]
            for i in range(len(ruta)):
                ruta[i].setText('')
            var.ui.cmbMat.setCurrentIndex(0)
            var.ui.cmbCon.setCurrentIndex(0)

        except Exception as error:
            print('Error limpiar furgoneta: %s: ' % str(error))


    def modifRuta(self):
        try:
            coste = conexion.Conexion.cargarTarifas(self)
            mitarifa = 0.00
            if var.ui.rbtLocal.isChecked():
                mitarifa = coste[0] #ese coste[0] es el primer valor del array
            if var.ui.rbtProvincial.isChecked():
                mitarifa = coste[1]
            if var.ui.rbtRegional.isChecked():
                mitarifa = coste[2]
            if var.ui.rbtNacional.isChecked():
                mitarifa = coste[3]

            ruta = [var.ui.lblRuta.text(), var.ui.txtFecha.text(), var.ui.cmbMat.currentText(), var.ui.cmbCon.currentText(), var.ui.txtKmi.text(), var.ui.txtKmf.text(),  mitarifa]
            rutamodif = []
            for i in ruta:
                rutamodif.append(i)
            print(rutamodif)
            conexion.Conexion.modifRuta(rutamodif)
            conexion.Conexion.listarRuta(self)


        except Exception as error:
            print('Error modificar furgo: %s: ' % str(error))



    '''
    eventos generales
    '''
    def Salir(self):
        try:
            ret = QtWidgets.QMessageBox.question(None, 'Salir',
                                           '¿Desea Salir del Programa?')
            if ret == QtWidgets.QMessageBox.Yes:
                sys.exit()
            else:
                QtWidgets.QMessageBox.hide


        except Exception as error:
            print('Error salir manu ' % str(error))


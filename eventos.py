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

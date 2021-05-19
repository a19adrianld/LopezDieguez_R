from PyQt5 import QtWidgets, QtSql

import var


class Conexion():
    def db_connect(self):
        filename = 'logista.db'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de BBDD',
                                           'Imposible Conexión.\n' 'Haga Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            QtWidgets.QMessageBox.warning(None, 'Abierta Base de Datos',
                                          'Haga click para continuar')
            print('Conexión Establecida')

    '''
    Funciones xestión furgonetas
    '''
    def altaFurgo(newfurgo):
        query = QtSql.QSqlQuery()
        print(newfurgo)
        query.prepare('insert into furgoneta (matricula, marca, modelo)'
                      'VALUES (:matricula, :marca, :modelo)')
        query.bindValue(':matricula', str(newfurgo[0]))
        query.bindValue(':marca', str(newfurgo[1]))
        query.bindValue(':modelo', str(newfurgo[2]))
        if query.exec_():
            QtWidgets.QMessageBox.warning(None, 'Alta Furgoneta Correcta',
                                          'Haga click para continuar')
            print('Furgoneta dada de alta')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')



    '''
    que se vean en la ventana los datos
    '''
    def listarFurgo(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select matricula, marca, modelo from furgoneta')
        if query.exec_():
            while query.next():
                var.ui.tabFurgo.setRowCount(index+1)
                #creo la primera fila
                var.ui.tabFurgo.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabFurgo.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tabFurgo.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')


    def deleteFurgo(matricula):
        query = QtSql.QSqlQuery()
        query.prepare('delete from furgoneta where matricula = :matricula')
        query.bindValue(':matricula', str(matricula))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Eliminada',
                                              'Haga click para continuar')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')

    def modifFurgo(furgomodif):
        query = QtSql.QSqlQuery()
        query.prepare('update furgoneta set marca=:marca, modelo=:modelo '
                      'where matricula=:matricula')
        query.bindValue(':marca', str(furgomodif[1]))
        query.bindValue(':modelo', str(furgomodif[2]))
        query.bindValue(':matricula', str(furgomodif[0]))

        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Modificada',
                                          'Haga click para continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar la matricula. Haga click para continuar')



    '''
    Gestion conductores
    '''

    def nuevoCon(newcon):
        query = QtSql.QSqlQuery()
        print(newcon)
        query.prepare('insert into conductor (dni, nombre) '
                      'VALUES (:dni, :nombre)')
        query.bindValue(':dni', str(newcon[0]))
        query.bindValue(':nombre', str(newcon[1]))

        if query.exec_():
            QtWidgets.QMessageBox.warning(None, 'Alta Conductor Correcto',
                                          'Haga click para continuar')
            print('Conductor dado de alta')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')


    def listarCon(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, nombre from conductor')
        if query.exec_():
            while query.next():
                var.ui.tabConductor.setRowCount(index+1) #crea la fila
                #creo la primera fila
                var.ui.tabConductor.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabConductor.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')



    def deleteCon(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from conductor where dni = :dni')
        query.bindValue(':dni', str(dni))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Eliminado',
                                              'Haga click para continuar')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')



    def modifCon(conmodif):
        print(conmodif)
        query = QtSql.QSqlQuery()
        query.prepare('update conductor set nombre = :nombre '
                      ' where dni = :dni')
        query.bindValue(':nombre', str(conmodif[1]))
        query.bindValue(':dni', str(conmodif[0]))

        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Modificado',
                                          'Haga click para continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar el DNI. Haga click para continuar')


    def cargarCmbC(cmbCon):
        cmbCon.clear()
        cmbCon.addItem('')
        query = QtSql.QSqlQuery()   #ayuda aquí
        query.prepare('select nombre from conductor')
        if query.exec_():
            while query.next():
                cmbCon.addItem(str(query.value(0)))



    def cargarCmbM(cmbMat): #aqui cambié cmbCon por cmbMat
        cmbMat.clear()
        cmbMat.addItem('')
        query = QtSql.QSqlQuery()   #ayuda aquí // ya no me hace falta jeje, son las consultas sql... query = consulta lol
        query.prepare('select matricula from furgoneta')
        if query.exec_():
            while query.next():
                cmbMat.addItem(str(query.value(0)))


    '''
    tarifas
    '''
    def cargarTarifas(self):
        #try:
        tar = []
        query = QtSql.QSqlQuery()
        query.prepare('select * from tarifas')
        if query.exec_():
            while query.next():
                var.tarifas[0].setText(str(query.value(1)))
                tar.append(query.value(1)) #esto es para llenar tar y pasarlo a eventos calculaTarifa
                var.tarifas[1].setText(str(query.value(2)))
                tar.append(query.value(2))
                var.tarifas[2].setText(str(query.value(3)))
                tar.append(query.value(3))
                var.tarifas[3].setText(str(query.value(4)))
                tar.append(query.value(4))
            return tar
        #except Exception as error:
         #   print('Error mostrar ventana tarifas: %s' % str(error))

    def actualizarTarifas(self):
        try:
            nuevatarifa = []
            id = 1
            #CARGO LAS NUEVAS TARIFAS
            for i, dato in enumerate(var.tarifas):
                nuevatarifa.append('{0:.2f}'.format(float(dato.text())))
            #CARGO LAS NUEVAS TARIFAS EN LA BD
            print(nuevatarifa)
            query = QtSql.QSqlQuery()
            query.prepare('update tarifas set local=:local, provincial=:provincial, regional=:regional, nacional=:nacional where id =:id')
            query.bindValue(':id', int(id))
            query.bindValue(':local', (nuevatarifa[0]))
            query.bindValue(':provincial', (nuevatarifa[1]))
            query.bindValue(':regional', (nuevatarifa[2]))
            query.bindValue(':nacional', (nuevatarifa[3]))
            if query.exec_():
                QtWidgets.QMessageBox.information(None, 'Tarifas modificadas', 'Haga click para continuar')
            else:
                QtWidgets.QMessageBox.warning(None, query.lastError().text(), 'Recuerde que las tarifas son únicas, haga click para continuar')
        except Exception as error:
            print('Error actualizar tarifas: %s: ' % str(error))



    def altaRuta(nuevaruta):
        query = QtSql.QSqlQuery()
        print(nuevaruta)
        query.prepare('insert into rutas (fecha, matricula, conductor, kmIn, kmFin, kmtotal, tarifakm, tarifatotal)'
                      'VALUES (:fecha, :matricula, :conductor, :kmIn, :kmFin, :kmtotal, :tarifakm, :tarifatotal)')
        query.bindValue(':fecha', str(nuevaruta[0]))
        query.bindValue(':matricula', str(nuevaruta[1]))
        query.bindValue(':conductor', str(nuevaruta[2]))
        query.bindValue(':kmIn', str(nuevaruta[3]))
        query.bindValue(':kmFin', str(nuevaruta[4]))
        query.bindValue(':kmtotal', str(nuevaruta[5]))
        query.bindValue(':tarifakm', str(nuevaruta[6]))
        query.bindValue(':tarifatotal', str(nuevaruta[7]))

        if query.exec_():
            QtWidgets.QMessageBox.warning(None, 'Alta Ruta Correcta',
                                          'Haga click para continuar')
            print('Ruta dada de alta')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')


    def listarRuta(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from rutas')
        if query.exec_():
            while query.next():
                var.ui.tabRutas.setRowCount(index+1)
                #creo la primera fila
                var.ui.tabRutas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                var.ui.tabRutas.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tabRutas.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tabRutas.setItem(index, 3, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tabRutas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                var.ui.tabRutas.setItem(index, 5, QtWidgets.QTableWidgetItem(str(query.value(5))))
                var.ui.tabRutas.setItem(index, 6, QtWidgets.QTableWidgetItem(str(query.value(6))))
                var.ui.tabRutas.setItem(index, 7, QtWidgets.QTableWidgetItem(str(query.value(7))))
                var.ui.tabRutas.setItem(index, 8, QtWidgets.QTableWidgetItem(str(query.value(8))))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga click para continuar')









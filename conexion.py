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
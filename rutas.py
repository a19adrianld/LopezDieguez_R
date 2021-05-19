from PyQt5 import QtWidgets
from ventana import *
from tarifas import *
import sys, conexion, var, eventos, rutas

class Rutas():
    '''
    modulos de gestión rutas
    '''
    def mostrarTarifas(self):
        try:
            var.dlgTarifas.show()
            conexion.Conexion.cargarTarifas(self)  #esto solo va si no tiene parentesis o pones self

        except Exception as error:
            print('Error mostrar ventana tarifas: ' % str(error))
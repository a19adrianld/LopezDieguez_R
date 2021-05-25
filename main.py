from ventana import *
from calendar import *
from tarifas import *
from datetime import datetime
import sys, conexion, var, eventos, rutas
import locale


locale.setlocale(locale.LC_ALL, 'es-ES')



class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgCalendar = Ui_dlgCalendar()
        var.dlgCalendar.setupUi(self)
        dia = datetime.now().day   #marcar la fecha de hoy
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgCalendar.Calendar.setSelectedDate(QtCore.QDate(ano, mes, dia))
        var.dlgCalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)


class DialogTarifas(QtWidgets.QDialog):
    def __init__(self):
        super(DialogTarifas, self).__init__()
        var.dlgTarifas = Ui_dlgTarifas()
        var.dlgTarifas.setupUi(self)
        var.tarifas = [var.dlgTarifas.txtLoc, var.dlgTarifas.txtProv, var.dlgTarifas.txtReg, var.dlgTarifas.txtNac]
        var.dlgTarifas.btnActualizar.clicked.connect(conexion.Conexion.actualizarTarifas) #primero lo pusimos en conexion.Conexion (para saltarse un paso)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        Genera y conecta todos los eventos.
        '''
        super(Main,self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        '''Instanciar ventanas auxiliares'''
        var.dlgCalendar = DialogCalendar()
        var.dlgTarifas = DialogTarifas()

        '''
        Conexión a la base de datos.
        '''
        conexion.Conexion.db_connect(self)
        conexion.Conexion.listarFurgo(self)
        conexion.Conexion.listarCon(self)
        conexion.Conexion.listarRuta(self)
        conexion.Conexion.cargarCmbM(var.ui.cmbMat)
        conexion.Conexion.cargarCmbC(var.ui.cmbCon)

        '''
        llamadas a los eventos de los botones
        '''

        var.ui.btnGrabar.clicked.connect(eventos.Eventos.cargaFurgo)
        var.ui.btnReload.clicked.connect(eventos.Eventos.limpiaFurgo)
        var.ui.btnEliminar.clicked.connect(eventos.Eventos.bajaFurgo)
        var.ui.btnModificar.clicked.connect(eventos.Eventos.modifFurgo)
        var.ui.btnAltacon.clicked.connect(eventos.Eventos.altaCon)
        var.ui.btnEliminacon.clicked.connect(eventos.Eventos.bajaCon)
        var.ui.btnModifcon.clicked.connect(eventos.Eventos.modifCon)
        var.ui.btnReloadcon.clicked.connect(eventos.Eventos.limpiaCon)
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        var.ui.btnAltaruta.clicked.connect(eventos.Eventos.altaRuta)

        '''
        eventos cajas texto
        '''
        var.ui.txtMatricula.editingFinished.connect(eventos.Eventos.matCapital)  # las mayusculas
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.validarDni)
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.dniCapital)  # las mayusculas
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.nomCapital)  # mayusc
        var.ui.txtKmf.editingFinished.connect(eventos.Eventos.calculaDistancia) #calcula para los totales

        '''
        Eventos de las tablas
        '''
        var.ui.tabFurgo.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        # selecciona los datos de una fila
        var.ui.tabFurgo.clicked.connect(eventos.Eventos.datosUnoFurgo)
        # conecta al clickar en la fila

        var.ui.tabConductor.clicked.connect(eventos.Eventos.datosUnCon)
        var.ui.tabConductor.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        var.ui.tabFurgo.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        var.ui.tabConductor.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        var.ui.tabRutas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabRutas.clicked.connect(eventos.Eventos.datosUnaRuta)

        '''
        eventos tarifas
        '''
        var.ui.btnTiporuta.buttonClicked.connect(eventos.Eventos.calculaTarifa)

        '''
        eventos menuBar
        '''
        var.ui.menuBarSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.menuBarTarifas.triggered.connect(rutas.Rutas.mostrarTarifas) #podria ser eventos.Eventos, lo importamos arriba


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    #window.setFixedSize(1024,768)
    window.show()
    sys.exit(app.exec())


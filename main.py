from ventana import *
import sys, conexion, var, eventos

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        Genera y conecta todos los eventos.
        '''
        super(Main,self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Conexión a la base de datos.
        '''
        conexion.Conexion.db_connect(self)
        conexion.Conexion.listarFurgo(self)
        conexion.Conexion.listarCon(self)

        '''
        llamadas a los eventos de los botones
        '''

        var.ui.txtMatricula.editingFinished.connect(eventos.Eventos.matCapital) #las mayusculas
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.validarDni)
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.dniCapital) #las mayusculas
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.nomCapital) #mayusc
        var.ui.btnGrabar.clicked.connect(eventos.Eventos.cargaFurgo)
        var.ui.btnReload.clicked.connect(eventos.Eventos.limpiaFurgo)
        var.ui.btnEliminar.clicked.connect(eventos.Eventos.bajaFurgo)
        var.ui.btnModificar.clicked.connect(eventos.Eventos.modifFurgo)
        var.ui.btnAltacon.clicked.connect(eventos.Eventos.altaCon)
        var.ui.btnEliminacon.clicked.connect(eventos.Eventos.bajaCon)
        var.ui.btnModifcon.clicked.connect(eventos.Eventos.modifCon)
        var.ui.btnReloadcon.clicked.connect(eventos.Eventos.limpiaCon)



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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    #window.setFixedSize(1024,768)
    window.show()
    sys.exit(app.exec())


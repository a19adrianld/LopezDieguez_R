# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarifas.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgTarifas(object):
    def setupUi(self, dlgTarifas):
        dlgTarifas.setObjectName("dlgTarifas")
        dlgTarifas.setWindowModality(QtCore.Qt.ApplicationModal)
        dlgTarifas.resize(400, 300)
        dlgTarifas.setModal(True)
        self.label = QtWidgets.QLabel(dlgTarifas)
        self.label.setGeometry(QtCore.QRect(140, 20, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnActualizar = QtWidgets.QPushButton(dlgTarifas)
        self.btnActualizar.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        self.layoutWidget = QtWidgets.QWidget(dlgTarifas)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 60, 199, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblLoc = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLoc.setFont(font)
        self.lblLoc.setObjectName("lblLoc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblLoc)
        self.txtLoc = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtLoc.setObjectName("txtLoc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtLoc)
        self.lblProv = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblProv)
        self.txtProv = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtProv.setObjectName("txtProv")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtProv)
        self.lblReg = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblReg.setFont(font)
        self.lblReg.setObjectName("lblReg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblReg)
        self.txtReg = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtReg.setObjectName("txtReg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtReg)
        self.lblNac = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNac.setFont(font)
        self.lblNac.setObjectName("lblNac")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblNac)
        self.txtNac = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNac.setObjectName("txtNac")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtNac)

        self.retranslateUi(dlgTarifas)
        QtCore.QMetaObject.connectSlotsByName(dlgTarifas)

    def retranslateUi(self, dlgTarifas):
        _translate = QtCore.QCoreApplication.translate
        dlgTarifas.setWindowTitle(_translate("dlgTarifas", "Dialog"))
        self.label.setText(_translate("dlgTarifas", "XESTOR TARIFAS"))
        self.btnActualizar.setText(_translate("dlgTarifas", "Actualizar"))
        self.lblLoc.setText(_translate("dlgTarifas", "Local:"))
        self.lblProv.setText(_translate("dlgTarifas", "Provincial:"))
        self.lblReg.setText(_translate("dlgTarifas", "Regional:"))
        self.lblNac.setText(_translate("dlgTarifas", "Nacional:"))

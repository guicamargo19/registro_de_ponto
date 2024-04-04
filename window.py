# -*- coding: utf-8 -*-

##############################################################################
# Form generated from reading UI file 'window.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
##############################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QPushButton,
                               QVBoxLayout, QWidget)

from styles import LOGO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainGridLayout = QGridLayout()
        self.mainGridLayout.setObjectName(u"mainGridLayout")
        self.mainGridLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logoGridLayout = QGridLayout()
        self.logoGridLayout.setObjectName(u"logoGridLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(180, 180))
        self.logoLabel.setPixmap(QPixmap(LOGO))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setWordWrap(False)
        self.logoLabel.setOpenExternalLinks(False)

        self.logoGridLayout.addWidget(self.logoLabel, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.logoGridLayout.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.logoGridLayout)

        self.reportLabel0 = QLabel(self.centralwidget)
        self.reportLabel0.setObjectName(u"reportLabel")
        self.reportLabel0.setMinimumSize(QSize(0, 0))
        self.reportLabel0.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Gill Sans"])
        font1.setPointSize(18)
        font2 = QFont()
        font2.setFamilies([u"Gill Sans"])
        font2.setPointSize(15)
        self.reportLabel0.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel0)

        self.reportLabel1 = QLabel(self.centralwidget)
        self.reportLabel1.setObjectName(u"reportLabel2")
        self.reportLabel1.setText("-")
        self.reportLabel1.setMaximumSize(QSize(16777215, 20))
        self.reportLabel1.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel1)

        self.reportLabel2 = QLabel(self.centralwidget)
        self.reportLabel2.setObjectName(u"reportLabel3")

        self.reportLabel2.setMaximumSize(QSize(16777215, 20))
        self.reportLabel2.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel2)

        self.reportLabel3 = QLabel(self.centralwidget)
        self.reportLabel3.setObjectName(u"reportLabel4")
        self.reportLabel3.setMaximumSize(QSize(16777215, 20))
        self.reportLabel3.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel3)

        self.reportLabel4 = QLabel(self.centralwidget)
        self.reportLabel4.setObjectName(u"reportLabel5")
        self.reportLabel4.setMaximumSize(QSize(16777215, 20))
        self.reportLabel4.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel4)

        self.reportLabel5 = QLabel(self.centralwidget)
        self.reportLabel5.setObjectName(u"reportLabel6")
        self.reportLabel5.setMaximumSize(QSize(16777215, 20))
        self.reportLabel5.setFont(font2)

        self.verticalLayout_3.addWidget(self.reportLabel5)

        self.resultadoGrid = QGridLayout()
        self.resultadoGrid.setObjectName(u"resultadoGrid")
        self.infoLabel = QLabel(self.centralwidget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setFont(font1)

        self.resultadoGrid.addWidget(self.infoLabel, 0, 0, 1, 1)

        self.totalLabel = QLabel(self.centralwidget)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setFont(font1)

        self.resultadoGrid.addWidget(self.totalLabel, 0, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.resultadoGrid)

        self.mainGridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.dataAtualGrid = QGridLayout()
        self.dataAtualGrid.setObjectName(u"dataAtualGrid")
        self.dataAtualLabel = QLabel(self.centralwidget)
        self.dataAtualLabel.setFont(font1)
        self.dataAtualLabel.setObjectName(u"dataAtualLabel")
        self.dataAtualLabel.setMaximumSize(QSize(16777215, 20))
        self.dataAtualLabel.setMargin(-2)
        self.dataAtualLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.dataAtualGrid.addWidget(self.dataAtualLabel, 0, 0, 1, 1)

        helpFont = QFont()
        helpFont.setFamilies([u"Arial"])
        helpFont.setPointSize(20)

        self.helpButton = QPushButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(30, 30))
        self.helpButton.setMaximumSize(QSize(30, 30))
        self.helpButton.setProperty('cssClass', 'specialButton')
        self.helpButton.setFont(helpFont)
        self.dataAtualGrid.addWidget(self.helpButton, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.entradaButton = QPushButton(self.centralwidget)
        self.entradaButton.setObjectName(u"entradaButton")
        self.entradaButton.setMinimumSize(QSize(16777215, 75))
        self.entradaButton.setSizeIncrement(QSize(0, 0))
        self.entradaButton.setBaseSize(QSize(0, 0))
        self.entradaButton.setProperty('cssClass', 'specialButton')

        font = QFont()
        font.setFamilies([u"Gill Sans"])
        font.setPointSize(35)

        self.verticalLayout.addWidget(self.entradaButton)

        self.entradaButton.setFont(font)
        self.entradaButton.setIconSize(QSize(16, 16))

        self.saidaButton = QPushButton(self.centralwidget)
        self.saidaButton.setObjectName(u"saidaButton")
        self.saidaButton.setMinimumSize(QSize(16777215, 75))
        self.saidaButton.setFont(font)
        self.saidaButton.setMouseTracking(False)
        self.saidaButton.setTabletTracking(False)
        self.saidaButton.setAutoDefault(False)
        self.saidaButton.setFlat(False)
        self.saidaButton.setProperty('cssClass', 'specialButton')

        self.verticalLayout.addWidget(self.saidaButton)

        self.relatorioButton = QPushButton(self.centralwidget)
        self.relatorioButton.setObjectName(u"relatorioButton")
        self.relatorioButton.setMinimumSize(QSize(16777215, 75))
        self.relatorioButton.setFont(font)
        self.relatorioButton.setProperty('cssClass', 'specialButton')

        self.verticalLayout.addWidget(self.relatorioButton)

        self.fecharButton = QPushButton(self.centralwidget)
        self.fecharButton.setObjectName(u"fecharButton")
        self.fecharButton.setMinimumSize(QSize(16777215, 75))
        self.fecharButton.setFont(font)
        self.fecharButton.setProperty('cssClass', 'specialButton')

        self.verticalLayout.addWidget(self.fecharButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.dataAtualGrid)

        self.mainGridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout.addLayout(self.mainGridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(accessibility)
        self.logoLabel.setAccessibleName(
            QCoreApplication.translate("MainWindow", "0", None))
# endif // QT_CONFIG(accessibility)
        self.logoLabel.setText("")
        self.entradaButton.setText(
            QCoreApplication.translate("MainWindow", "Entrada", None))
        self.reportLabel0.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.reportLabel1.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.reportLabel2.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.reportLabel3.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.reportLabel4.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.reportLabel5.setText(
            QCoreApplication.translate("MainWindow", "-", None))
        self.infoLabel.setText(QCoreApplication.translate(
            "MainWindow", "Total de Horas:", None))
        self.totalLabel.setText(
            QCoreApplication.translate("MainWindow", "", None))
        self.dataAtualLabel.setText(QCoreApplication.translate(
            "MainWindow", "", None))
        self.saidaButton.setText(QCoreApplication.translate(
            "MainWindow", u"Sa\u00edda", None))
        self.relatorioButton.setText(QCoreApplication.translate(
            "MainWindow", u"Relat\u00f3rio", None))
        self.fecharButton.setText(
            QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.helpButton.setText(
            QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

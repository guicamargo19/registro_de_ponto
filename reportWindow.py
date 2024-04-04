# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'reportWindow.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

# from main import RelatorioWindow
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QListWidget,
                               QPushButton, QWidget)


class Ui_reportWindow(object):
    def setupUi(self, reportWindow):
        if not reportWindow.objectName():
            reportWindow.setObjectName(u"reportWindow")
        reportWindow.setFixedSize(QSize(400, 400))
        self.centralwidget = QWidget(reportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.reportsTitleLabel = QLabel(self.centralwidget)
        self.reportsTitleLabel.setObjectName(u"reportsTitleLabel")
        font = QFont()
        font.setFamilies([u"Gill Sans"])
        font.setPointSize(20)
        self.reportsTitleLabel.setFont(font)

        helpFont = QFont()
        helpFont.setFamilies([u"Arial"])
        helpFont.setPointSize(20)

        self.helpButton = QPushButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(30, 30))
        self.helpButton.setMaximumSize(QSize(30, 30))
        self.helpButton.setProperty('cssClass', 'specialButton')
        self.helpButton.setFont(helpFont)
        self.gridLayout.addWidget(self.helpButton, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.reportsTitleLabel, 0, 0, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setFixedSize(QSize(377, 75))
        font1 = QFont()
        font1.setFamilies([u"Gill Sans"])
        font1.setPointSize(35)
        self.backButton.setFont(font1)
        self.backButton.setProperty('cssClass', 'specialButton')

        self.gridLayout.addWidget(
            self.backButton, 3, 0, 1, 1,
            alignment=Qt.AlignmentFlag.AlignVCenter)

        self.listReport = QListWidget(self.centralwidget)
        self.listReport.setObjectName(u"listReport")
        self.listReport.setFixedSize(QSize(377, 250))

        self.gridLayout.addWidget(
            self.listReport, 1, 0, 1, 1,
            alignment=Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addLayout(self.gridLayout)

        reportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(reportWindow)

        QMetaObject.connectSlotsByName(reportWindow)
    # setupUi

    def retranslateUi(self, reportWindow):
        reportWindow.setWindowTitle(QCoreApplication.translate(
            "reportWindow", u"MainWindow", None))
        self.reportsTitleLabel.setText(QCoreApplication.translate(
            "reportWindow", u"Relat\u00f3rio de horas trabalhadas:", None))
        self.backButton.setText(QCoreApplication.translate(
            "reportWindow", u"Voltar", None))
        self.helpButton.setText(QCoreApplication.translate(
            "reportWindow", u"?", None))
    # retranslateUi

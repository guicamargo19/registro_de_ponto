from datetime import date, datetime, timedelta
from time import gmtime, strftime

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QMainWindow,
                               QMessageBox, QVBoxLayout)

from backup import clearJson, dumpJson, loadJson
from dbtiny import Register, dbRegister, getValorFromDb
from reportWindow import Ui_reportWindow
from window import Ui_MainWindow

# Report window class


class WindowReport(QMainWindow, Ui_reportWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.backButton.clicked.connect(self.backToMainWindow)

        self.helpButton.clicked.connect(self.helpFunction)

    # Back button function

    def backToMainWindow(self):
        self.close()

    # Help button function

    def helpFunction(self):
        dialog = HelpDialog(
            """
        Últimos 30 registros de dias trabalhados.

        Após 30 registros existentes, o mais
        antigo é removido, mantendo assim
        sempre 30 registros na base de dados.
        """
        )
        dialog.exec()


# Help Dialog window class


class HelpDialog(QDialog):
    def __init__(self, _message) -> None:
        super().__init__()
        self.message = _message
        self.setWindowTitle('Ajuda')
        Qbtn = QDialogButtonBox.Ok  # type: ignore
        self.button = QDialogButtonBox(Qbtn)
        self.button2 = self.button.addButton(Qbtn)
        self.button2.setProperty("cssClass", "specialButton")
        self.button2.setMinimumSize(60, 45)
        self.button2.clicked.connect(self.accept)
        self.myLayout = QVBoxLayout()
        message = QLabel(_message)
        message.setContentsMargins(0, 0, 30, 0)
        message.setStyleSheet("font-size:15px;")
        self.myLayout.addWidget(
            message, alignment=Qt.AlignmentFlag.AlignVCenter)
        self.myLayout.addWidget(
            self.button2, alignment=Qt.AlignmentFlag.AlignBottom)

        self.setLayout(self.myLayout)


# Main Window class


class MainWindow(QMainWindow, Ui_MainWindow):
    timeOut = None
    timeIn = None
    fmt = "%H:%M:%S"
    totalHours = 0.0
    index1 = 1
    newRegister = None
    dayRegister = None
    listBackup: list = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.saveStateApplication()

        self.telaReport = WindowReport()

        # Signals
        self.relatorioButton.clicked.connect(self.reportFunction)

        self.dataAtualLabel.setText(self.actualDate())

        self.entradaButton.clicked.connect(self.enterRegister)

        self.saidaButton.clicked.connect(self.exitRegister)

        self.fecharButton.clicked.connect(self.exitFunction)

        self.helpButton.clicked.connect(self.helpText)

    # Backup data entry label

    def entryBackupFunction(self, i, listObject, fmt, reportLabel):
        formatedDate = datetime.strptime(
            listObject[i], '%d/%m/%Y %H:%M:%S')
        stringDate = formatedDate.strftime(fmt)
        text = f"Entrada: {stringDate}"
        reportLabel.setText(text)
        self.listBackup.append(stringDate)
        dumpJson(self.listBackup)
        self.timeIn = formatedDate
        return self.timeIn

    # Backup data exit label

    def exitBackupFunction(self, i, listObject, fmt, reportLabel):
        formatedDate = datetime.strptime(
            listObject[i], '%d/%m/%Y %H:%M:%S')
        stringDate = formatedDate.strftime(fmt)
        text = f"Saída: {stringDate}"
        reportLabel.setText(text)
        self.listBackup.append(stringDate)
        dumpJson(self.listBackup)
        self.timeOut = formatedDate
        return self.timeOut

    # totalLabel insert data from Backup restore

    def textInsertLabel(self, timeOut, timeIn):
        text = self.countHours(timeOut, timeIn)
        self.totalLabel.setText(text)

    # Save application state function

    def saveStateApplication(self):
        listObject = loadJson()
        fmt = '%d/%m/%Y %H:%M:%S'
        if listObject != []:
            sizeListObject = len(listObject)
            if sizeListObject == 1:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

            elif sizeListObject == 2:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

                self.timeOut = self.exitBackupFunction(
                    1, listObject, fmt, self.reportLabel1)

                self.textInsertLabel(self.timeOut, self.timeIn)

            elif sizeListObject == 3:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

                self.timeOut = self.exitBackupFunction(
                    1, listObject, fmt, self.reportLabel1)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    2, listObject, fmt, self.reportLabel2)

            elif sizeListObject == 4:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

                self.timeOut = self.exitBackupFunction(
                    1, listObject, fmt, self.reportLabel1)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    2, listObject, fmt, self.reportLabel2)

                self.timeOut = self.exitBackupFunction(
                    3, listObject, fmt, self.reportLabel3)

                self.textInsertLabel(self.timeOut, self.timeIn)

            elif sizeListObject == 5:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

                self.timeOut = self.exitBackupFunction(
                    1, listObject, fmt, self.reportLabel1)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    2, listObject, fmt, self.reportLabel2)

                self.timeOut = self.exitBackupFunction(
                    3, listObject, fmt, self.reportLabel3)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    4, listObject, fmt, self.reportLabel4)

            elif sizeListObject == 6:
                self.timeIn = self.entryBackupFunction(
                    0, listObject, fmt, self.reportLabel0)

                self.timeOut = self.exitBackupFunction(
                    1, listObject, fmt, self.reportLabel1)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    2, listObject, fmt, self.reportLabel2)

                self.timeOut = self.exitBackupFunction(
                    3, listObject, fmt, self.reportLabel3)

                self.textInsertLabel(self.timeOut, self.timeIn)

                self.timeIn = self.entryBackupFunction(
                    4, listObject, fmt, self.reportLabel4)

                self.timeOut = self.exitBackupFunction(
                    5, listObject, fmt, self.reportLabel5)

                self.textInsertLabel(self.timeOut, self.timeIn)

    # Count total hours of work function

    def countHours(self, timeOut: datetime, timeIn: datetime):
        dateResult = timeOut - timeIn
        dateResultSeconds = dateResult.total_seconds()
        self.totalHours += dateResultSeconds
        return self.secondsToDatetime(self.totalHours)

    # convert datetime to string to insert into the label

    def secondsToDatetime(self, seconds: float, format='%H:%M:%S'):
        td = timedelta(seconds=seconds)
        timeObj = gmtime(td.total_seconds())
        return strftime(format, timeObj)

    # Applies de actual date plus the day name at the label

    def actualDate(self):
        completeDate = str(date.today())
        format = '%Y-%m-%d'
        newDate = datetime.strptime(completeDate, format)
        dateBrazil = (newDate.strftime('%d/%m/%Y'))
        data = str(date.today().weekday())
        if data == '0':
            return f'{dateBrazil} - Segunda-Feira'
        elif data == '1':
            return f'{dateBrazil} - Terça-Feira'
        elif data == '2':
            return f'{dateBrazil} - Quarta-Feira'
        elif data == '3':
            return f'{dateBrazil} - Quinta-Feira'
        elif data == '4':
            return f'{dateBrazil} - Sexta-Feira'
        elif data == '5':
            return f'{dateBrazil} - Sábado'
        elif data == '6':
            return f'{dateBrazil} - Domingo'
        else:
            return dateBrazil

    # Enter register

    @Slot()
    def enterRegister(self):
        data = datetime.now()
        self.timeIn = data
        formatedDate = data.strftime('%d/%m/%Y %H:%M:%S')
        text = f"Entrada: {formatedDate}"

        if self.reportLabel0.text() == "-":
            self.reportLabel0.setText(text)
            self.listBackup.append(formatedDate)
            dumpJson(self.listBackup)

        elif self.reportLabel2.text() == "-" and \
                self.reportLabel1.text() != "-":
            self.reportLabel2.setText(text)
            self.listBackup.append(formatedDate)
            dumpJson(self.listBackup)

        elif self.reportLabel4.text() == "-" and \
                self.reportLabel3.text() != "-":
            self.reportLabel4.setText(text)
            self.listBackup.append(formatedDate)
            dumpJson(self.listBackup)

    # Exit register

    @Slot()
    def exitRegister(self):
        if self.timeIn is not None:
            data = datetime.now()
            self.timeOut = data
            formatedDate = data.strftime('%d/%m/%Y %H:%M:%S')
            text = f"Saída: {formatedDate}"

            if self.reportLabel1.text() == "-" and \
                    self.reportLabel0.text() != "-":
                self.reportLabel1.setText(text)
                self.listBackup.append(formatedDate)
                dumpJson(self.listBackup)
                self.textInsertLabel(self.timeOut, self.timeIn)

            elif self.reportLabel3.text() == "-" and \
                    self.reportLabel2.text() != "-":
                self.reportLabel3.setText(text)
                self.listBackup.append(formatedDate)
                dumpJson(self.listBackup)
                self.textInsertLabel(self.timeOut, self.timeIn)

            elif self.reportLabel5.text() and \
                    self.reportLabel4.text() != "-":
                self.reportLabel5.setText(text)
                self.listBackup.append(formatedDate)
                dumpJson(self.listBackup)
                self.textInsertLabel(self.timeOut, self.timeIn)

    # Close the application

    @Slot()
    def exitFunction(self):
        self.close()

    # Close event function

    def closeEvent(self, event):

        string = """
                Por favor, informe um registro de SAÍDA para encerrar a
                aplicação!
                """

        if self.reportLabel0.text() != '-' and self.reportLabel1.text() == '-':
            message = HelpDialog(string)
            message.exec()
            event.ignore()

        elif self.reportLabel2.text() != '-' and \
                self.reportLabel3.text() == '-':
            message = HelpDialog(string)
            message.exec()
            event.ignore()

        elif self.reportLabel4.text() != '-' and \
                self.reportLabel5.text() == '-':
            message = HelpDialog(string)
            message.exec()
            event.ignore()

        else:
            answer = QMessageBox.question(
                self, "Fechar aplicação", "Você tem certeza que deseja sair?",
                buttons=QMessageBox.Yes | QMessageBox.No,   # type: ignore
                defaultButton=QMessageBox.No,  # type: ignore
            )

            if answer == QMessageBox.Yes:  # type: ignore
                self.newRegister = self.dataForReport()

                if self.newRegister == '-':
                    event.accept()
                    clearJson()

                else:
                    self.checkDuplicity()
                    event.accept()
                    clearJson()

            else:
                event.ignore()

    # Report window show function

    @Slot()
    def reportFunction(self):
        self.telaReport.listReport.clear()
        self.telaReport.setWindowTitle("Relatório de horas por dia")
        dbList = getValorFromDb(self.index1)

        if isinstance(dbList, list):
            qtde = len(dbList)
            i = 0
            while i < qtde:
                if dbList is not None:
                    for itens in dbList:
                        i += 1
                        self.telaReport.listReport.addItem(itens)
        else:
            self.telaReport.listReport.addItem('NENHUM REGISTRO')

        self.telaReport.show()

    # Function that somates the time worked at the same day

    def sumHours(self, dateRegister: datetime, newRegister):
        hours, minutes, seconds = map(int, newRegister.split(':'))
        # String to timedelta
        newRegister = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        total = dateRegister + newRegister
        return total.strftime('%H:%M:%S')

    # Function that check duplicity of registers in the same day

    def checkDuplicity(self):
        completeDate = str(date.today())
        format = '%Y-%m-%d'
        newDate = datetime.strptime(completeDate, format)
        dateBrazil = (newDate.strftime('%d/%m/%Y'))
        dbList = getValorFromDb(self.index1)

        if dbList is not None:
            if isinstance(dbList, list):
                if dateBrazil in dbList[-1]:
                    stringRegister = ""
                    for item in dbList[-1]:

                        if item in "/:":
                            stringRegister = f'{stringRegister}{item}'

                        elif item in \
                                " .-abcdefghijlmnopqrstuvxzçáSDFTQ":
                            continue

                        elif item not in "/:":
                            try:
                                intString = int(item)
                                if isinstance(intString, int):
                                    stringRegister = \
                                        f'{stringRegister}{intString}'
                                    qtde = len(stringRegister)
                                    if qtde == 10:
                                        stringRegister = \
                                            f'{stringRegister}{" "}'
                                    if qtde == 19:
                                        break
                            except TypeError:
                                continue

                    fmtComplete = '%d/%m/%Y %H:%M:%S'
                    fmtHours = '%H:%M:%S'
                    dateRegister = datetime.strptime(
                        stringRegister, fmtComplete)
                    dateStringRegister = dateRegister.strftime(fmtHours)
                    dateRegister = datetime.strptime(
                        dateStringRegister, fmtHours)

                    newRegister = self.totalLabel.text()
                    sumHours = self.sumHours(dateRegister, newRegister)
                    self.newRegister = self.dataForReportBackup(sumHours)

                    self.dayRegister = Register([self.newRegister])
                    dbRegister(self.index1, self.newRegister,
                               self.dayRegister, check=True)
                else:
                    self.dayRegister = Register([self.newRegister])
                    dbRegister(self.index1, self.newRegister,
                               self.dayRegister)
        else:
            self.dayRegister = Register([self.newRegister])
            dbRegister(self.index1, self.newRegister,
                       self.dayRegister)

    # String data pattern for database insert

    def dataForReport(self):
        actualDate = self.dataAtualLabel.text()
        totalHours = self.totalLabel.text()
        if totalHours != '':
            register = f'{actualDate} - {totalHours} horas trabalhadas.'
            print(register)
            return register
        else:
            return '-'

    # String data pattern for the database

    def dataForReportBackup(self, sumHours):
        actualDate = self.dataAtualLabel.text()
        totalHours = sumHours
        if totalHours != '':
            register = f'{actualDate} - {totalHours} horas trabalhadas.'
            print(register)
            return register

    # Help message for the main window
    @Slot()
    def helpText(self):
        dialog = HelpDialog(
            """
        Clicando no botão 'Entrada', é iniciada a contagem de
        tempo trabalhado.

        Clicando no botão 'Saída', o intervalo trabalhado é
        registrado e armazenado, aguardando a continuação da
        contagem clicando no botão 'Entrada' novamente.

        Ao final do expediente, o último registro deve ser uma
        Saída, assim o registro deste dia será inserido
        na base de dados e ficará disponível para relatório.

        O botão 'Relatório' abre a janela contendo os últimos 30
        registros de horas trabalhadas por dia.

        O botão 'Fechar' encerra a aplicação.
            """
        )
        dialog.exec()

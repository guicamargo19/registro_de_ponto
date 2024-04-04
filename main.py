import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from styles import ICON, setupTheme
from windowMain import MainWindow

if __name__ == '__main__':

    # Create the application
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Set the application icon
    icon = QIcon(str(ICON))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Set the application main window title
    window.setWindowTitle('Registro de Ponto')

    # Start the application
    window.setFixedSize(650, 400)
    window.show()
    sys.exit(app.exec())

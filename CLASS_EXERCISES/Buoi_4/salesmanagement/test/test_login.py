from PyQt6.QtWidgets import QApplication, QMainWindow

from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.LoginMainWindow import LoginMainWindowExt

app = QApplication([])
mainWindow = QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainWindow)
myui.showwindow()
app.exec()
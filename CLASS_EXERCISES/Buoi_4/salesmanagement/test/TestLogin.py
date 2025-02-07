import PyQt6.QtWidgets

from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.LoginMainWindowExt import LoginMainWindowExt

app=PyQt6.QtWidgets.QApplication([])
mainwindow=PyQt6.QtWidgets.QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
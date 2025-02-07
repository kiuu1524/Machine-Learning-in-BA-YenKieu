from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.MainProgramMainWindow import Ui_MainWindow


class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.MainProgramWindow import Ui_Dialog


class MainProgramWindowExt(Ui_Dialog):
    def setupUi(self, Dialog):

        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
            self.MainWindow.show()

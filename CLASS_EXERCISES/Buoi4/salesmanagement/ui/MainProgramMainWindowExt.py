import sys

from PyQt6.QtWidgets import QMainWindow

from salesmanagement.ui.MainProgramMainWindow import Ui_MainWindow
from salesmanagement.ui.ProductMainWindowExt import ProductMainWindowExt


class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
        self.actionQuanlySanphamDanhMuc.triggered.connect(self.xuly_momanhinh_qlspdm)
    def xuly_thoat(self):
        sys.exit(0)
    def xuly_momanhinh_qlspdm(self):
        self.mainwindow = QMainWindow()
        self.myui = ProductMainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
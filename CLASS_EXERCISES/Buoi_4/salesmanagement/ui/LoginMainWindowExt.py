from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from CLASS_EXERCISES.Buoi_4.salesmanagement.libs.nhanvienconnector import NhanVienConnector
from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.LoginMainWindow import Ui_MainWindow

#from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.MainProgramMainWindow import Ui_MainWindow
from CLASS_EXERCISES.Buoi_4.salesmanagement.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    #def __init__(self):
     #   self.nvconnector=NhanVienConnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonDangNhap.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.lineEditUserName.text()
        password=self.lineEditPassword.text()
        #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
        #gọi kết nối cơ sở dữ liệu MySQL
        self.nvconnector.connect()
        ##self.nvlogin=self.nvconnector.dang_nhap(username,password)
        #if self.nvlogin!=None:
        if username=="admin" and password=="123":
            self.MainWindow.hide()
            self.mainwindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()
        def setupSignalAndSlot(self):
            self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
        def xuly_thoat(self):
            self.exit(0)

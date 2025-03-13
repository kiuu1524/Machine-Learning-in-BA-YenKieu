from PyQt6.QtWidgets import QApplication, QMainWindow

from HousingPricePrediction.coding_pyqt6.HousingPricePredictionMainWindowExt import HousingPricePredictionMainWindowExt

app = QApplication([])
mainwindow = QMainWindow()
myui = HousingPricePredictionMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()


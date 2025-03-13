
from PyQt6.QtWidgets import QTableWidgetItem, QPushButton,QApplication, QWidget, QMessageBox
from Connectors.Connector import Connector
import pandas as pd
import mysql.connector

from UI.MainWindow import Ui_MainWindow
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class MainWindowEx(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.connector = Connector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # self.pushButtonCustomer.clicked.connect(self.loadCustomerIntoQTableWidget)
        self.pushButton2a.clicked.connect(self.load2aIntoQTableWidget)
        self.pushButton2b.clicked.connect(self.load2bIntoQTableWidget)
        self.pushButton2c.clicked.connect(self.load2cIntoQTableWidget)
        self.pushButton2d.clicked.connect(self.load2dIntoQTableWidget)
        self.pushButton2e.clicked.connect(self.load2eIntoQTableWidget)

        self.pushButton3a.clicked.connect(self.load3aIntoQTableWidget)
        self.pushButton3b.clicked.connect(self.load3bIntoQTableWidget)
        self.pushButton4.clicked.connect(self.load4IntoQTableWidget)


    def connectDatabase (self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "babaecommerce"
        self.connector.username ="root"
        self.connector.password = "Yk12345678"
        self.connector.connect()

    def showDataIntoTableWidget(self, table, df):

        table.setRowCount(0)
        table.setColumnCount(len(df.columns))

        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            table.insertRow(row)
            j = 0

            for data in arr:
                table.setItem(row, j, QTableWidgetItem(str(data)))
                j = j + 1
            row=row + 1

    def load2aIntoQTableWidget(self):

        self.connectDatabase()

        sql = "SELECT YEAR(order_purchase_timestamp) AS purchase_year, COUNT(DISTINCT customer_id) AS purchased_customers FROM orders GROUP BY purchase_year ORDER BY purchase_year "
        df = self.connector.queryDataset(sql)

        self.showDataIntoTableWidget(self.tableWidgetData, df)

    def load2bIntoQTableWidget(self):

        self.connectDatabase()
        sql="SELECT   purchase_year, purchased_customers,  (purchased_customers - LAG(purchased_customers, 1, 0) OVER (ORDER BY purchase_year)) / LAG(purchased_customers, 1, 0) OVER (ORDER BY purchase_year) AS growth_rate "\
                "FROM ( SELECT  YEAR(order_purchase_timestamp) AS purchase_year,  COUNT(DISTINCT customer_id) AS purchased_customers  "\
                "FROM orders  GROUP BY purchase_year) AS yearly_purchases ORDER BY purchase_year"
        df = self.connector.queryDataset(sql)

        self.showDataIntoTableWidget(self.tableWidgetData, df)
    def load2cIntoQTableWidget(self):

        self.connectDatabase()

        sql = "SELECT YEAR(order_purchase_timestamp) AS purchase_year, sum(oi.price) AS total_revenue FROM orders o "\
                "JOIN order_items oi ON o.order_id = oi.order_id GROUP BY purchase_year ORDER BY purchase_year; "
        df = self.connector.queryDataset(sql)

        self.showDataIntoTableWidget(self.tableWidgetData, df)

    def load2dIntoQTableWidget(self):

        self.connectDatabase()

        sql= "SELECT  YEAR(o.order_purchase_timestamp) AS purchase_year,  p.product_category_name,  SUM(oi.price) AS total_revenue "\
                "FROM orders o JOIN order_items oi ON o.order_id = oi.order_id "\
                "JOIN products p ON oi.product_id = p.product_id  "\
                "GROUP BY purchase_year, p.product_category_name ORDER BY purchase_year, total_revenue DESC;"

        df = self.connector.queryDataset(sql)

        self.showDataIntoTableWidget(self.tableWidgetData, df)

    def load2eIntoQTableWidget(self):

        self.connectDatabase()

        sql= "SELECT YEAR(o.order_purchase_timestamp) AS purchase_year, p.product_category_name, SUM(CASE WHEN o.order_status = 'canceled' THEN 1 ELSE 0 END) AS canceled_orders "\
                "FROM orders o JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id GROUP BY purchase_year, p.product_category_name ORDER BY purchase_year, canceled_orders DESC;"

        df = self.connector.queryDataset(sql)

        self.showDataIntoTableWidget(self.tableWidgetData, df)

    def load3aIntoQTableWidget(self):
        try:
            self.connectDatabase()

            seller_state = self.lineEditSeller.text()
            sql= f" SELECT  seller_id as 'List of employees'  FROM sellers WHERE seller_state like '{seller_state}' "
            df = self.connector.queryDataset(sql)

            self.showDataIntoTableWidget(self.tableWidgetData, df)
        # except Exception as e:
        #     print("Error:", e)
        #

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("ERROR")
            msgBox.setWindowTitle("KHÔNG CÓ MÃ KHÁCH HÀNG NÀY")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()

    def load3bIntoQTableWidget(self):
        try:
            self.connectDatabase()

            customer_id = self.lineEditCustomerID.text()

            sql = f"SELECT  customer_id,order_id,  order_purchase_timestamp,  order_status FROM orders where customer_id like '{customer_id}'"

            df = self.connector.queryDataset(sql)

            self.showDataIntoTableWidget(self.tableWidgetData, df)

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("ERROR")
            msgBox.setWindowTitle("KHOONG TÌM THẤY THÔNG TIN")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()


    def load4IntoQTableWidget(self):


        self.connectDatabase()
        sql= "SELECT  c.customer_zip_code_prefix as zip, oi.price as price,oi.freight_value as freight_value1 FROM  orders o  JOIN  order_items oi ON o.order_id = oi.order_id JOIN  customers c ON o.customer_id = c.customer_id; "
        df = self.connector.queryDataset(sql)

        X = df.drop(columns=['freight_value1'])
        y = df['freight_value1']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        self.labelmse.setText(str(mse))

    def show(self):
        self.MainWindow.show()

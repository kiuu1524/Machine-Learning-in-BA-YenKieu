from salesmanagement.libs.connector import MySQLConnector
from salesmanagement.models.danhmuc import DanhMuc


class DanhMucConnector(MySQLConnector):
    def LayToanBoDanhMuc(self):
        cursor = self.conn.cursor()
        sql="select * from Danhmuc"
        cursor.execute(sql)
        dataset = cursor.fetchall()
        dsdm=[]
        for item in dataset:
            dsdm.append(DanhMuc(item[0],item[1],item[2]))
        cursor.close()
        return dsdm


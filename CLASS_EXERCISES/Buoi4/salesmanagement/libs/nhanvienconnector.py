from salesmanagement.libs.connector import MySQLConnector
from salesmanagement.models.nhanvien import NhanVien


class NhanVienConnector(MySQLConnector):
    def dang_nhap(self,username,password):
        cursor=self.conn.cursor()
        sql="select * from nhanvien where username=%s and password=%s"
        val = (username,password)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        nv=None# giả sử không tìm thấy nhân viên đúng theo USERname +password
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdeleted = dataset
            #vào được đây tức là có nhân viên
            nv=NhanVien(id,manhanvien,tennhanvien,username,password,isdeleted)
        cursor.close()
        return nv



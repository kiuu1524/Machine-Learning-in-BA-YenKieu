from salesmanagement.libs.sanphamconnector import SanPhamConnector

spc=SanPhamConnector()
spc.connect()
dssp=spc.LaySanPhamTheoMaDanhMuc(1)
print("Danh sách sản phẩm có mã danh mục =1:")
for p in dssp:
    print(p)
#test chi tiết sản phẩm:
id=2
spc.connect()
sp=spc.Lay_ChiTiet(id)
if sp!=None:
    print("*"*20)
    print(sp)

id_remove=13
spc.connect()
result=spc.Xoa_SanPham(id_remove)
if result>0:
    print("Xóa sản phẩm có mã =",id_remove," thành công")
else:
    print("Xóa sản phẩm có mã =", id_remove, " THẤT BẠI")

from file_factory import FileFactory
from ontap_oop import Product
ff=FileFactory()
dataset=ff.readData('mydataset.json',Product)
print('Danh sach san pham: ')
for product in dataset:
    print(product)

def loc_san_pham_theo_gia(san_pham, gia_min, gia_max):

    ket_qua = [sp for sp in san_pham if gia_min <= sp.price <= gia_max]
    return ket_qua


# Nhập khoảng giá từ người dùng
gia_min = float(input("Nhập giá thấp nhất (a): "))
gia_max = float(input("Nhập giá cao nhất (b): "))

if gia_min > gia_max:
    print("Giá thấp nhất phải nhỏ hơn giá cao nhất!")
else:
    ket_qua_loc = loc_san_pham_theo_gia(dataset, gia_min, gia_max)
    print("Sản phẩm trong khoảng giá {} - {}:".format(gia_min, gia_max))
    for sp in ket_qua_loc:
        print(f"id:{sp.id}, name: {sp.name}, Price: {sp.price}")


def xoa_san_pham_gia_nho_hon(san_pham, gia_min):
    return [sp for sp in san_pham if sp.price >= gia_min]

gia_min = float(input("Nhập giá tối thiểu (x): "))
danh_sach = xoa_san_pham_gia_nho_hon(dataset, gia_min)

print("Danh sách sản phẩm còn lại:")
if not danh_sach:
    print("Không còn sản phẩm nào.")
else:
    for sp in danh_sach:
        print(f"id:{sp.id}, name: {sp.name}, Price: {sp.price}")
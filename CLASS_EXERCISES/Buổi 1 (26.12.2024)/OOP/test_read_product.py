from file_factory import FileFactory
from ontap_oop import Product
ff=FileFactory()
dataset=ff.readData('mydataset.json',Product)
print('Danh sach san pham: ')
for product in dataset:
    print(product)


#Lọc ra các sản phẩm có giá trong khoảng từ min_price đến max_price.
    
def filter_products_by_price(products, min_price, max_price):
    """
    Lọc ra các sản phẩm có giá trong khoảng từ min_price đến max_price.
    
    :param products: Danh sách các đối tượng Product
    :param min_price: Giá tối thiểu (A)
    :param max_price: Giá tối đa (B)
    :return: Danh sách các sản phẩm thỏa mãn điều kiện
    """
    return [product for product in products if min_price <= product.price <= max_price]

def get_price_range():
    """
    Hàm nhập giá trị min và max từ người dùng.
    :return: Bộ giá trị (min_price, max_price)
    """
    while True:
        try:
            min_price = float(input("Nhập giá trị tối thiểu (min): "))
            max_price = float(input("Nhập giá trị tối đa (max): "))
            if min_price > max_price:
                print("Giá trị tối thiểu không được lớn hơn giá trị tối đa. Vui lòng nhập lại.")
            else:
                return min_price, max_price
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

# Nhập giá trị min và max
min_price, max_price = get_price_range()

# Lọc các sản phẩm theo khoảng giá
filtered_products = filter_products_by_price(dataset, min_price, max_price)  # Sửa Product thành dataset

# In các sản phẩm thỏa mãn
print("Danh sách sản phẩm trong khoảng giá từ", min_price, "đến", max_price, ":")
for product in filtered_products:
    print(product)






def remove_products_below_price(products, threshold):
    """
    Xóa tất cả các sản phẩm có giá < threshold.
    
    :param products: Danh sách các đối tượng Product
    :param threshold: Giá trị ngưỡng
    :return: Danh sách sản phẩm sau khi xóa
    """
    return [product for product in products if product.price >= threshold]

# Nhập giá trị x (ngưỡng)
try:
    threshold_price = float(input("Nhập giá trị ngưỡng x để xóa các sản phẩm có giá < x: "))
except ValueError:
    print("Giá trị không hợp lệ. Vui lòng nhập số hợp lệ.")
    exit()

# Xóa các sản phẩm có giá < x
dataset = remove_products_below_price(dataset, threshold_price)

# In danh sách sản phẩm sau khi xóa
print("\nDanh sách sản phẩm sau khi xóa các sản phẩm có giá <", threshold_price, ":")
for product in dataset:
    print(product)
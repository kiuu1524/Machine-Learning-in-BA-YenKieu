from ontap_oop import Product
from file_factory import FileFactory

p1=Product(1,"Coca",100)
print(p1)

dataset=[]
dataset.append(p1)
dataset.append(Product(2,'Pepsi',20))
dataset.append(Product(3,'Sting',80))
dataset.append(Product(4,'Aqua',70))
dataset.append(Product(5,'Redbull',81))
print('Danh sach san pham')
for product in dataset:
    print(product)

#Gọi chức năng chụp ảnh đối tượng xuống ổ cứng
#chụp thành định dạng Json
ff=FileFactory()
ff.writeData('mydataset.json',dataset)

while True:
    id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    
    dataset.append(Product(id, name, price))
    
    choice = input("Do you want to continue? (Y/N)")
    if choice.lower() == "n":
        break
    
print("Updated Dataset:")
for product in dataset:
    print(product)


ff = FileFactory()
ff.writeData(f"mydataset.json", dataset)

def firstDegree(a,b):
    """

    :param a: Hệ số a
    :param b: Hệ số b
    :return: Trả về 3 trường hợp kết quả
    """
    if a==0 and b==0:
        print("Phuong trinh vo so nghiem")
    elif a==0 and b!=0:
        print('Phuong trinh vo nghiem')
    else:
        x=-b/a
        print('Nghiem cua phuong trinh x=',x)

print('Phuong trinh bac 1')
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
firstDegree(a,b)



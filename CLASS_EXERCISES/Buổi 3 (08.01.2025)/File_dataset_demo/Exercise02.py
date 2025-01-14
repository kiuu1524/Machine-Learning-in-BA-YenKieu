import pandas as pd

def filter_and_sort_orders(df, minValue, maxValue, sortType):
    """
    Lọc danh sách các hóa đơn có tổng giá trị nằm trong khoảng [minValue, maxValue]
    và sắp xếp danh sách theo tổng giá trị.

    Args:
        df (pd.DataFrame): Dữ liệu đơn hàng với các cột ['OrderID', 'UnitPrice', 'Quantity', 'Discount'].
        minValue (float): Giá trị tổng tối thiểu để lọc.
        maxValue (float): Giá trị tổng tối đa để lọc.
        sortType (bool): True nếu muốn sắp xếp tăng dần, False nếu sắp xếp giảm dần.

    Returns:
        pd.DataFrame: DataFrame chứa các mã hóa đơn và tổng giá trị, đã lọc và sắp xếp.
    """
    # Tính tổng giá trị từng hóa đơn
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='TotalValue')

    # Lọc các hóa đơn nằm trong khoảng [minValue, maxValue]
    filtered_orders = order_totals[(order_totals['TotalValue'] >= minValue) & (order_totals['TotalValue'] <= maxValue)]

    # Sắp xếp danh sách hóa đơn theo sortType
    sorted_orders = filtered_orders.sort_values(by='TotalValue', ascending=sortType)

    return sorted_orders

# Ví dụ sử dụng
if __name__ == "__main__":
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv('../../dataset/SalesTransactions.csv')

    # Nhập giá trị min, max và kiểu sắp xếp
    minValue = float(input("Nhập giá trị min: "))
    maxValue = float(input("Nhập giá trị max: "))
    sortType = input("Nhập kiểu sắp xếp (tăng dần: True, giảm dần: False): ").strip().lower() == 'true'

    # Gọi hàm
    result = filter_and_sort_orders(df, minValue, maxValue, sortType)

    # In kết quả
    print("Danh sách các hóa đơn:")
    print(result)

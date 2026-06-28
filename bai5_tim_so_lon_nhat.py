a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
lon_nhat = a
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c

print(f"Số lớn nhất trong ba số {a}, {b}, {c} là: {lon_nhat}")

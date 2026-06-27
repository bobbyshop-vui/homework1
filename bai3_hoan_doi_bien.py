a = input("Nhập giá trị biến a: ")
b = input("Nhập giá trị biến b: ")

print(f"Trước khi hoán đổi: a = {a}, b = {b}")

a, b = b, a

print(f"Sau khi hoán đổi:  a = {a}, b = {b}")

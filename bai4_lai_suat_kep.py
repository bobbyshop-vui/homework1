P = float(input("Nhập số tiền gốc (P): "))
r = float(input("Nhập lãi suất hàng năm (r, ví dụ 0.05 cho 5%): "))
n = float(input("Nhập số lần tính lãi trong năm (n): "))
t = float(input("Nhập số năm (t): "))

A = P * (1 + r / n) ** (n * t)

print(f"\nSố tiền gốc (P):            {P:,.2f}")
print(f"Lãi suất (r):               {r * 100:.2f}%")
print(f"Số lần tính lãi/năm (n):    {n:.0f}")
print(f"Số năm (t):                 {t:.0f}")
print(f"Số tiền cuối cùng (A):      {A:,.2f}")

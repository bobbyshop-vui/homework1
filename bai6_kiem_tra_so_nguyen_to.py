so = int(input("Nhập một số nguyên dương: "))

if so < 2:
    print(f"Số {so} không phải là số nguyên tố.")
else:
    la_nguyen_to = True
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print(f"Số {so} là số nguyên tố.")
    else:
        print(f"Số {so} không phải là số nguyên tố.")

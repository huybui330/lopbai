def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

# Nhập số từ người dùng
n = int(input("Nhập số nguyên dương: "))

if n < 0:
    print("Không tồn tại giai thừa cho số âm")
else:
    print(f"Giai thừa của {n} là: {giai_thua(n)}")
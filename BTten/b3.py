def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)
    d = int (input("Nhap so nguyen duong:"))
    if n < 0:
        print("Không tồn tại giai thừa cho số âm")
    else:
        print(f"giai thừa của {d} là:{giai_thua(d)}") 
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.0001)
y = x**2
z = x**0.5

plt.figure(figsize=(5.5, 2))
plt.subplot(1, 2, 1)  # 1 hàng, 2 cột, biểu đồ đầu tiên
plt.plot(x, y, 'b')  # Biểu đồ màu xanh
plt.title("Đồ thị hàm số y = x^2")
plt.subplot(1, 2, 2)  # 1 hàng, 2 cột, biểu đồ thứ hai
plt.plot(x, z, 'r') 
plt.title("Đồ thị hàm số y=sqrt(x)")
plt.show()
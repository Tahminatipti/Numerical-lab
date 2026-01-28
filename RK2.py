import matplotlib.pyplot as plt

def f(x, y):
    return  x+y

x0 = 0
y0 = 1
h = 0.1
xn = 1

x = x0
y = y0

x_values = []
y_values = []

print("x\t y\t\tk1\t\tk2")

while x <= xn:
    x_values.append(x)
    y_values.append(y)
    k1 = h * f(x, y)
    k2 = h * f(x + h, y + k1)
    y = y + (k1 + k2) / 2
    x = x + h

    print(f"{x:.2f}\t{y:.5f}\t\t{k1:.5f}\t\t{k2:.5f}")

print(f"y({xn}) = {y:.5f}")

plt.plot(x_values, y_values, marker='o', label="RK2 Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Runge-Kutta 2nd Order Method")
plt.grid(True)
plt.legend()
plt.show()

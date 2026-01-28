import matplotlib.pyplot as plt

# Given data points
x = [1, 2, 4, 7]
y = [1, 4, 16, 49]

n = len(x)

# Lagrange Interpolation Function
def lagrange(x_val):
    result = 0

    print("i\t Li(x)")
    print("-" * 20)

    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x_val - x[j]) / (x[i] - x[j])

        print(f"{i}\t {Li:.6f}")
        result += Li * y[i]

    return result

# Interpolation point
x_interp = 3
y_interp = lagrange(x_interp)

print("\nInterpolated value at x =", x_interp, "is y =", y_interp)

# Plotting
plt.plot(x, y, 'o-', label="Given Data")
plt.scatter(x_interp, y_interp, color='red', label="Interpolated Point")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Function to integrate
def f(x):
    return x**2 + 1

# Trapezoidal Rule
def trapezoidal(a, b, n):
    h = (b - a) / n

    print("i\t x_i\t\t f(x_i)")
    print("-" * 30)

    total = f(a) + f(b)

    for i in range(n + 1):
        x = a + i * h
        fx = f(x)
        print(f"{i}\t {x:.4f}\t {fx:.6f}")

        if i != 0 and i != n:
            total += 2 * fx

    integral = (h / 2) * total
    return integral

# Limits and intervals
a = 0
b = 2
n = 4

# Compute integral
result = trapezoidal(a, b, n)
print("\nApproximate Integral =", result)

# Plotting
x_vals = [a + i*(b-a)/100 for i in range(101)]
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x)")

# Plot trapezoids
h = (b - a) / n
for i in range(n):
    x0 = a + i*h
    x1 = x0 + h
    plt.plot([x0, x1], [f(x0), f(x1)], 'r')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Trapezoidal Rule")
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - x - 2

# Bisection Method
def bisection(a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    print("-" * 60)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        print(f"{i}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

# Initial guesses
a = 1
b = 2

# Find root
root = bisection(a, b)

print("\nApproximate Root:", root)

# Plotting
x_vals = [x / 10 for x in range(0, 30)]
y_vals = [f(x) for x in x_vals]

plt.axhline(0)        # x-axis
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(root, f(root))  # root point
plt.text(root, f(root), f"  Root ≈ {root:.4f}")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method Root Finding")
plt.legend()
plt.show()

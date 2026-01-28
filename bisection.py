import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return 3*x**2 - 4*x - 2

# Bisection Method
def bisection(a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("No root guaranteed in the interval")
        return None

    print("Iteration\ta\t\tb\t\tc\t\tf(c)")
    print("-" * 70)

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i+1}\t\t{a:.6f}\t{b:.6f}\t{c:.6f}\t\t{fc:.6f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\n✅ Root ≈ {c:.6f}")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nDid not converge")
    return None

# Run the bisection method
root = bisection(1, 2)

# --- Plotting ---
if root is not None:
    # Create range for plotting
    x = np.linspace(0, 3, 400)
    y = f(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = 3x² - 4x - 2")
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root:.4f}")
    plt.scatter(root, f(root), color='red', s=60, zorder=5)

    plt.title("Bisection Method Root Finding")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
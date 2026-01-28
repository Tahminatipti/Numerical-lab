import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return 3*x**2 - 4*x - 2

# False Position (Regula Falsi) Method
def False_Position(a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("False Position method fails: no guaranteed root in this interval.")
        return None

    print("Iteration\ta\t\tb\t\tc\t\tf(c)")
    print("-" * 70)

    for i in range(max_iter):
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
        fc = f(c)
        print(f"{i+1}\t\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.6f}")

        # Check for convergence
        if abs(fc) < tol or abs(b - a) < tol:
            print(f"\n✅ Root ≈ {c:.6f}")
            return c

        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\n❌ Did not converge within max iterations.")
    return None

# Run the method
root = False_Position(1, 2)

# --- Plotting the function and root ---
if root is not None:
    x = np.linspace(0, 3, 400)
    y = f(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = 3x² - 4x - 2", color="blue")
    plt.axhline(0, color="black", linewidth=1)  # x-axis
    plt.axvline(root, color="red", linestyle="--", label=f"Root ≈ {root:.4f}")
    plt.scatter(root, f(root), color="red", s=60, zorder=5)

    plt.title("False Position (Regula Falsi) Method")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

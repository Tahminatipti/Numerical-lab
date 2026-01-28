import matplotlib.pyplot as plt
import math

# Given data
x = [0, 1, 2, 3, 4]
y = [1, 2, 4, 7, 11]

n = len(y)

# Create backward difference table
diff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    diff[i][0] = y[i]

for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

# Print backward difference table
print("Backward Difference Table:")
for i in range(n):
    for j in range(i + 1):
        print(f"{diff[i][j]:8.4f}", end=" ")
    print()

# Newton Backward Interpolation
def newton_backward(x_val):
    h = x[1] - x[0]
    p = (x_val - x[-1]) / h
    result = diff[-1][0]

    p_term = 1
    for i in range(1, n):
        p_term *= (p + (i - 1))
        result += (p_term * diff[-1][i]) / math.factorial(i)

    return result

# Interpolation point
x_interp = 3.5
y_interp = newton_backward(x_interp)

print("\nInterpolated value at x =", x_interp, "is y =", y_interp)

# Plotting
plt.plot(x, y, 'o-', label="Given Data")
plt.scatter(x_interp, y_interp, color='red', label="Interpolated Point")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton Backward Interpolation")
plt.legend()
plt.grid(True)
plt.show()

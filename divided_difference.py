import matplotlib.pyplot as plt

# Given data (unequal spacing allowed)
x = [1, 2, 4, 7]
y = [1, 4, 16, 49]

n = len(x)

# Create divided difference table
div_diff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    div_diff[i][0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        div_diff[i][j] = (div_diff[i+1][j-1] - div_diff[i][j-1]) / (x[i+j] - x[i])

# Print divided difference table
print("Divided Difference Table:")
for i in range(n):
    for j in range(n - i):
        print(f"{div_diff[i][j]:10.4f}", end=" ")
    print()

# Newton Divided Difference interpolation
def newton_divided(x_val):
    result = div_diff[0][0]
    product = 1

    for i in range(1, n):
        product *= (x_val - x[i-1])
        result += product * div_diff[0][i]

    return result

# Interpolation point
x_interp = 3
y_interp = newton_divided(x_interp)

print("\nInterpolated value at x =", x_interp, "is y =", y_interp)

# Plotting
plt.plot(x, y, 'o-', label="Given Data")
plt.scatter(x_interp, y_interp, color='red', label="Interpolated Point")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton Divided Difference Interpolation")
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
def f(x,y):
  return 3*x**2-2*y
x0=0
y0=1
h=0.1
xn=0.5
x=x0
y=y0
x_values=[]
y_values=[]
print("x\ty\t\tk1\t\tk2\t\tk3\t\tk4")
while x<xn:
  x_values.append(x)
  y_values.append(y)
  k1=h*f(x,y)
  k2=h*f(x+h/2,y+k1/2)
  k3=h*f(x+h/2,y+k2/2)
  k4=h*f(x+h,y+k3)
  y=y+(k1+2*k2+2*k3+k4)/6
  x=x+h
  
  print(f"{x:.2f}\t{y:.5f}\t\t{k1:.5f}\t{k2:.5f}\t{k3:.5f}\t{k4:.5f}")
print(f"Root={y:.5f}")
plt.plot(x_values,y_values,marker='o',label="RK4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("RK4")
plt.grid(True)
plt.legend()
plt.show()
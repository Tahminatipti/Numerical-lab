import numpy as np
import math
import matplotlib.pyplot as plt

# Define the differential equation y' = x + y
def f(t, y):
    return t + y
def y_exact(t):
    return 2*np.exp(t)-t-1

# Exact solution (for comparison)
def eulars(f,a,b,alpha,N):
    h=(b-a)/N
    t=a
    w=alpha
    t_values=[t]
    w_values=[w]
    print("t\t\tw\t\texact\t\terror")
     
    for i in range(1,N+1):
        w=w+h*f(t,w)
        t=a+i*h
        exact=y_exact(t)
        error=abs(exact-w)
        print(f"{t:.6f}\t{w:.6f}\t{exact:.6f}\t{error:.6f}")
        t_values.append(t)
        w_values.append(w)
    return np.array(t_values),np.array(w_values)
t,w=eulars(f,0,1,1,10)
y_true=y_exact(t)
plt.figure(figsize=(8,6))
plt.plot(t,w,'bo-',label="eulars aprroximation")
plt.plot(t,y_true,'r--',label='exact solution')
plt.title("Eulars method")
plt.xlabel('t')
plt.ylabel('w')
plt.legend()
plt.grid(True)
plt.show()


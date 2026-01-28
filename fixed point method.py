
import matplotlib.pyplot as plt
import numpy as np
def g(x):
    return (x**2+5)/6
def fixed_point(x0,tol=1e-4,max_iter=100):
    print("Iteration\tx1")
    for i in range(max_iter):
        x1=g(x0)
        print(f"{i+1}\t\t{x1:.6f}")
        if abs(x1-x0)<tol:
            print(f"root is:{x1:.6f}")
            return x1
        x0=x1
    print("Did not converge")
    return None
fixed_point(2.0)
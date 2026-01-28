import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return 3*x**2-4*x-2
def df(x):
 return 6*x-4
def newtonraphson(x0,tol=1e-4,max_iter=100):
  print("iteration\tx\t\tf(x)\t\tdf(x)")
  print('-'*60)
  for i in range(max_iter):
    fx=f(x0)
    dfx=df(x0)
    if dfx==0:
      print("Method is failed")
      return None
    x1=x0-(fx/dfx)
    print(f"{i+1}\t\t{x1:.6f}\t{f(x1):.6f}\t{df(x1):.6f}")
    if abs(x1-x0)<tol:
      print(f"root={x1:.6f}")
      return x1
    x0=x1
  print("did not converge")
  return None
root=newtonraphson(2.0)
if root is not None:
  x=np.linspace(0,3,400)
  y=f(x)
  plt.figure(figsize=(8,6))
  plt.plot(x,y,label='f(x)=3*x**2-4*x-2',color='blue')
  plt.axhline(0,color='red',linewidth=1)
  plt.axvline(root,color='black',linestyle="--",label=f"root={root:.6f}")
  plt.scatter(root,f(root),color='green',s=60,zorder=5)
  plt.title('Newton raphson method')
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.legend()
  plt.grid(True)
  plt.show()


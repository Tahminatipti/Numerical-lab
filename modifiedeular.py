def f(x,y):
  return x+y

x0=0
y0=1
h=0.1
xn=0.5

x=x0
y=y0

print("x\ty")

while x<=xn:
  print(f"{x:.1f}\t{y:.4f}")

  y_pred=y+h*f(x,y)
  y=y+(h/2)*(f(x,y)+f(x+h,y_pred))
  x=x+h

def f(x,y):
  return x+y
def f2(x,y):
  return 1+x+y
def taylor(x0,y0,h,xn):
   
  x=x0
  y=y0
  print("x\ty")

  while x<=xn:
    print(f"{x:.1f}\t{y:.5f}")
    y=y+h*f(x,y)+(h**2/2)*f2(x,y)
    x=x+h
  return
  
x0=0
y0=1
h=0.1
xn=0.5
root=taylor(x0,y0,h,xn)
 


def trapizoidal(f,a,b,n):
 h=(b-a)/n
 s=f(a)+f(b)

 for i in range(1,n):
  x=a+i*h
  s+=2*f(x)

 return (h/2)*s
import math
f=lambda x:x**2

a=0
b=2
n=4

print("Aprroximate intregral:",trapizoidal(f,a,b,n))

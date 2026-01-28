def simpson13(f,a,b,n):
  if n%2!=0:
      print("n must be even")
      return None
  
  h=(b-a)/n
  s=f(a)+f(b)

  for i in range(1,n):
     x=a+i*h
     if i%2==0:
        s+=2*f(x)
     else:
        s+=4*f(x)
  return (h/3)*s

import math
f=lambda x:x**2

a=0
b=2
n=4

root=simpson13(f,a,b,n)
print(f"Aproximate integral:{root:.5f}")
    
    
 

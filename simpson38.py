def simpson38(f,a,b,n):
  if n%3!=0:
    print("N must be multiple of 3")
    return None
  
  h=(b-a)/n
  s=f(a)+f(b)

  for i in range(1,n):
    x=a+i*h
    if i%3==0:
      s+=2*f(x)
    else:
      s+=3*f(x)

  return(3*h/8)*s

import math
f=lambda x:x**2

a=0
b=2
n=6

root=simpson38(f,a,b,n)
print(f"Aproximate intregral:{root:.5f}")

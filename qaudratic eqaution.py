#program to solve qaudratic equation
#G.Niharika
import cmath
print("enter the value")
a=int(input())
b=int(input())
c=int(input())
discriminant=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(discriminant))/(2*a)
root2=(-b+cmath.sqrt(discriminant))/(2*a)
print("the root1 is:",root1)
print("the root2 is:",root2)

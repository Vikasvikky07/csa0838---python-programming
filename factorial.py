     #program to find factorial of given number
#G.Niharika
print("enter the value")
n=int(input())
factorial=1
if(n<0):
   print("factorial does not exist")
elif(n==0):
   print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
print("factorial of",n,"is",factorial)  

x=int(input("X="))
n=int(input("N="))
print("1 for addition\n2 for substraction\n3 for division\n4 for multiplication\n5 for power")
option=int(input("option:"))
if option==1:
    result=x+n
    print("sum:",result)
elif option==2:
    result=x-n
    print("sub:",result)
elif option==3:
    result=x/n
    print("div:",result)
elif option==4:
    result=x*n
    print("mul:",result)
elif option==5:
    result=x**n
    print("pow:",result)
else:
    print("invalid input")
            
                
 
 


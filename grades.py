#program to find grade and average marks of a student
#G.Niharika
print("enter the marks")
sub1=int(input())
sub2=int(input())
sub3=int(input())
total=sub1+sub2+sub3
avg=total/3
if(avg>91):
  print("Grade is S")
elif(avg>81):
  print("Grade is A")
elif(avg>71):
  print("Grade is B")
elif(avg>61):
  print("Grade is C")
elif(avg>51):
  print("Grade is D")
elif(avg<50):
    print("FAIL")
else:
  print("invalid input")
print("average=",avg)

n=1
even=0
odd=0
while (n<=4):
    a=int(input("enter a number"))
    if (a%2==0):
        even=even+a
    else:
        odd=odd+a
    n=n+1
print("total of even numbers is ",even)
print("random something "+str(odd)+"   is the total of odd numbers")
print("%d is the total of %s numbers and %d"  %(even,"even",odd))

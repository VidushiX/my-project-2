
#A shop has 3 products and their product number and prices are as follows (1-pizza-1200, 2-buns-60 ,3-rolls-80), write a python program to print a bill for
#this shop by taking the product number and the quantity. (you need to think of a way to end the program when the cashier wants to stop entering products)
#this bill should only display the total

p=[1200,60,80]
total=0
pno=int(input("enter product number: "))

while(pno>0):
    pq=int(input("enter product quantity: "))
    total= (p[pno-1]*pq)+total
    pno=int(input("enter product number: "))


print("Total is",total)

#git test

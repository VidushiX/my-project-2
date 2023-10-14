f=open("marks.txt","r+")
f2=open("results.txt","w")
for i in f:
    data=i.strip().split("-")
    tot=int(data[1])+int(data[2])+int(data[3])
    avg=tot/3
    f2.write("the total is"+str(tot)+"\n")
    f2.write("the average is"+str(avg)+"\n")
f.close()
f2.close()

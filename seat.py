name= input("enter your name:")
print("hello",name)
num= int (input("enter your age:"))
if num<26:
    print(name,"your at last")
elif num<=51:
    print(name,"you are at middle")
elif num >=50:
    print( name,"your are at front")
 
opp={1:18,2:17,3:16,4:15,5:14,6:13,7:12,8:11,9:10,10:9,11:8,12:7,13:6,14:5,15:4,16:3,17:2,0:1}
T=int(input("what is the no of the person: "))
for i in range(T):
    n=int(input("which seat do you want: "))
    compartment=(n-1)//18
    position=n%18
    oppseat=opp[position]
    seat=(compartment*18)+oppseat
    print(seat, end=" ")
    if position in [0,1,3,5,7,9,12,14,16]:
      print("WS")
    if position in [2,4,6,8,10,11,13,15,17]:
      print("AS")

myname="Lola"
print(myname)
myage=14
print(myage)
friends=["Emma", "Kat", "Branda"]
#friends[2]
#this is a loop
for friend in friends:
    print(friend)
#print(friends[2])
pocketmoney=int(input("Enter the pocket money of every month:"))
if(pocketmoney>500):
    print("you are a rich kid")
elif(pocketmoney>100):
    print("you have a good life")
else:
    print("i know how you feel")   
     
count=5
while(count>=0):
    print(count)
    count=count-1
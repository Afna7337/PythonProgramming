Startyear=int(input("enter the Start year:"))
Endyear=int(input("enter the End year:"))
print("the leap year between  these years:")
for i in range(Startyear,Endyear):
    if(i % 4 == 0 and i % 100 != 0 or i % 400 == 0):
        print (i)
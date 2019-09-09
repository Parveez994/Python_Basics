
c=int(input("Enter the number:"))
sum=0

for i in range(1,c):
    if(c%i==0):
        sum=sum+i

if(sum==c):
    print("It is a perfect number",c)
else:
    print("It is naot a perfect number",c)

if c>1:
    for a in range(2,c):
        if (c%a)==0:
            print("Not a prime no.")
            print(a,"times",c//a,"is",c)
            break
        else:
            print(c,"is a prime no.")

else:
    print(c,"is not a prime no.")


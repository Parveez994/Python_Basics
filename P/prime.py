c=int(input("Enter any number:"))

if c>1:
    for a in range(2,c):
        if (c%a==0):
            print("Not a prime no.")
            print(a,"times",c//a,"is",c)
            break
        else:
            print(c,'is a prime no.')

else:
    print(c,'is not a prime no.')

b=int(input("Enter a number:"))
s=0
temp=b

while temp>0:
    d=temp%10
    s+=d**3
    temp//=10

    if(b==s):
        print('Armstrong number')
    else:
        print('Not an armstrong number')

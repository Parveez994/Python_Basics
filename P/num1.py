a=int(input())
t=0

while(a>0):
    d=a%10
    t=t+d
    a=a//10

    print("Sum of numbers",t)

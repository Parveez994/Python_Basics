a=123
r=0
while(a>0):
    d=a%10
    r=r*10+d
    a=a//10
    print('reverse the digits',r)

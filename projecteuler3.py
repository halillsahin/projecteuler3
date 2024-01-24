a=int(600851475143**0.5+1)
b=[]
c=[]
for i in range(2,a):
    if 600851475143%i==0:
        b.append(i)
for i in b :
    for x in range(2,i):
        if i%x==0:
            break
    else:
        c.append(i)    
    

print(max(c))            



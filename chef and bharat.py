from collections import defaultdict

def chefora(inp):
    n = inp
    palin = inp
    n = n//10
    while n > 0:
        palin = palin*10+(n%10)
        n = n//10
    return palin
    

    
    return n*int(size)+int(reverse_1)
divisor=10**9+7
sums=0
de=[]
sum=[]
for i in range(1,10):
    de.append(i)
    sums=sums+i
    sum.append(sums)

for i in range(10,100001):
    k=chefora(i)
    de.append(k)
    sums=sums+k
    sum.append(sums)

dic=defaultdict(list)
test=int(input().strip())
while test:
    lr=[]
    lr=list(map(int,input().strip().split()))
    # flag=0
    # if lr[1] in dic.keys:
    #     product=dic[lr[1]]
    #     flag=1
    # elif:
    #     for i in dic.keys:
    #         if i>j  
    product=1

   

    
    
    new_sum=sum[lr[1]-1]-sum[lr[0]-1]
    
    

    


    product=pow(de[lr[0]-1],new_sum,divisor)
            
        

            

    print(product)
    test-=1




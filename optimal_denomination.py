import random
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x



test=120000
while test:
    n=int(random.randint(1,100000))
    print(n)
    salary=[]
    for i in range(0,n):
        salary.append(int(random.randint(1,10**9)))
    left=[0 for i in range(0,n)]
    right=[0 for i in range(0,n)]
    hcf=salary[0]
    left[1]=hcf
    for i in range(2,n):
        hcf=gcd(hcf,salary[i-1])
        left[i]=hcf
    hcf=salary[n-1]
    right[n-2]=hcf
    i=n-3

    while i>=0:
        hcf=gcd(hcf,salary[i+1])
        right[i]=hcf
        i-=1

    mid=[]
    for i in range(0,n):
        k=gcd(left[i],right[i])
        mid.append(k)
    #code to decide which element to chose
    sum=0

    for i in salary:
        sum=sum+i
    temp=float('inf')
    for i in range(0,len(salary)):
        k=((sum-salary[i])+mid[i])/mid[i]
        if k<temp:
            temp=k
    print(int(temp))


    

        


    



   
    
   


    test-=1
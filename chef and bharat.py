def chefora(n):
    nu=str(n)
    size=len(nu)-1
    size='1'+size*'0'
    reverse=nu[0:len(nu)-1]
    reverse_1=reverse[::-1]

    
    return n*int(size)+int(reverse_1)


for i in range(10,100):
    print(chefora(i))



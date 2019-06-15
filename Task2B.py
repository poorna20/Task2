
def add(a,s):
    for i in range(s[0]-1,s[1]):
        a[i]+=s[2]
    return a

n=int(input("Enter number of elements: "))
a=[i for i in range(1,n+1)]
q=int(input("Enter number of queries: "))
for i in range(0,q):
    s=[int(s) for s in input("Enter indices and value to add: ").split()]
    a=add(a,s)

print ("Max element: ",max(a))
    
    
    

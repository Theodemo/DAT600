def linear_search(A,n,x):
    for i in range(0,n):
        if A[i]==x:
            return i
        
    return -1

A=[1,2,3,4,5,6,7,8,9,10]
n=len(A)    
x=11
print(linear_search(A,n,x)) 

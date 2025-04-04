
def insertion_sort_decreasing(A,n):

    for i in range(1,n):
        key=A[i]
        j=i-1
        while j>0 and A[j]<key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
    return A
        
        
A=[5,2,4,6,1,3]
n=len(A)
A=insertion_sort_decreasing(A,n)
print(A)
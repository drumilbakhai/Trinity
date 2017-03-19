def selectSort(A):
    for slot in range(len(A)-1,0,-1):
        maxPosition = 0
        for position in range(1,slot+1):
            if A[position] > A[maxPosition]:
                maxPosition = position
            temp = A[slot]
            A[slot]= A[maxPosition]
            A[maxPosition]= temp

A = [54,26,93,17,77,31,44,55,20]
selectSort(A)
print A
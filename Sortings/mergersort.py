def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        print "Left Sorting Done ", left
        mergeSort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] =  left[i]
                i = i+1
            elif right[j] < left [i]:
                A[k] = right[j]
                j = j+1
            k= k+1

        ## Append elements which are not compared

        while i< len(left):
            A[k] = left[i]
            k= k+1
            i=i+1

        while j < len(right):
            A[k]= right[j]
            k=k+1
            j=j+1
        print "Hey Sorted Part is ", A
A = [200,100,90,80]
mergeSort(A)
print A
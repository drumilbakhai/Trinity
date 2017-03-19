import math

def maximum(A,left,right):
    if right-left == 0:
        return A[right]

    mid = int(math.floor((left+right/2)))
    print mid
    leftMax = maximum(A,left,mid)
    rightMax = maximum(A,mid+1,right)
    print rightMax,leftMax
    if rightMax < leftMax:
        return leftMax
    else:
        return rightMax


A = [1,2,3,4,5]
maximum(A,0,4)
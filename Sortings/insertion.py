def insertion(A):
    for unsortedIndex in range(1,len(A)):
        insertVal = A[unsortedIndex]
        free_hole = unsortedIndex
        print "Here the Element ", insertVal, "will be shifted and blanked out"
        while free_hole > 0 and A[free_hole-1] > insertVal:
            # Shift Elements to one position to right
            print "Element ",insertVal, "will be moved because ",A[free_hole-1], "is greater than ",insertVal
            A[free_hole] = A[free_hole-1]
            free_hole = free_hole -1

        # Updating the value of Element Present in Hole
        A[free_hole] = insertVal
        if unsortedIndex == len(A)-1:
            print "Final List Is ", A


A = [54,26,93,17,77,31,44,55,20]
insertion(A)
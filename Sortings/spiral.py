def spiral(matrix,rows,cols):
    #Direction 0 is for Left->Right Parsing
    #Direction 1 is for Top-> Bottom Parsing
    #Direction 2 is for Right->Left Parsing
    #Direction 3 is for Bottom->Up Parsing
    direction = 0

    Top = 0
    Bottom = rows
    print "Bottom is ",Bottom
    left = 0
    right = cols

    while left<=right and Top<=Bottom:

        if direction == 0:
            print "LEFT TO RIGHT"
            for x in xrange(left,right):
                print A[Top][x]
            Top = Top + 1
            direction =1

        elif direction ==1:
            print "TOP TO BOTTOM"
            for x in xrange(Top,Bottom):
                print A[x][right-1]
            right = right - 1
            #print "Right value is ",right
            direction = 2

        elif direction ==2:
            print "RIGHT TO LEFT "
            for x in xrange(right,left,-1):
                print A[Bottom-1][x-1]
            Bottom = Bottom -1
            direction = 3

        elif direction == 3:
            print "BOTTOM TO TOP"
            for x in xrange(Bottom,Top,-1):
                print A[x-1][left]
            left = left +1
            direction = 0


A = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
rows = len(A)
columns = len(A[0])
print "hi",rows,columns
spiral(A,rows,columns)


#for row in xrange(len(A)):
    #for col in xrange(len(A[row])):
       # print "o"

def isPlaindrome(stringer):
    if len(stringer) < 2:
        print "Maja"
        return True
    elif stringer[0] != stringer[-1]:
        #print "NO PALIdrome"
        return False
    isPlaindrome(stringer[1:-1])

mystring = "kay"

isPlaindrome(mystring)
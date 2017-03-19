from deque import Deque

def palindrom(stringer):
    d = Deque()

    for character in stringer:
        d.addRear(character)

    flag = True
    while len(d.items) > 1 and flag:
        frontChar = d.delFront()
        rearChar = d.delRear()
        if rearChar!= frontChar:
            flag = False

    return flag

myString = raw_input("Enter String")
if(palindrom(myString)):
    print "It is palindrome"
else:
    print "Sorry Broo"

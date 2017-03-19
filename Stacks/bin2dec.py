from stacks import Stacks

def conversion(dec):
    s = Stacks()
    binary = ""
    while dec > 0:
        #print dec
        rem = dec % 2
        s.push(rem)
        #print "Element Added", rem
        dec = dec // 2
    #s.printStack()

    while not s.isEmpty():
        binary = binary + str(s.pop())

    return binary

stringer = raw_input("Enter decimal number")
num = int(stringer)

print "Binary Equivalent is ", conversion(num)
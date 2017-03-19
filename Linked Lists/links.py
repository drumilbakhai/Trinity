class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        # type: () -> object
        return self.data

    def getNext(self):
        return self.next


    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1

            current = current.getNext()

        return count

    def printer(self):
        current = self.head
        while current != None:

            print current.getData()
            current = current.getNext()



    def search(self,item):
        current = self.head
        flag = False
        while current != None and not flag:
            if current.getData() == item:
                flag= True
            else:
                current = current.getNext()
        return flag

    def lastNode(self):
        last = None
        current = self.head
        while current:
            last= current
            current=current.getNext()

        return last

    def lastAdd(self, item):
        last = self.lastNode()
        newNode = Node(item)
        current = self.head
        last.setNext(newNode)
        newNode.setNext(None)
        last.getData()
    

l = LinkedList()
#n = Node()
l.add(40)
l.add(50)
l.add(60)

print(l.size())

l.printer()
print (l.lastAdd(30))

l.printer()

print(l.search(5000))
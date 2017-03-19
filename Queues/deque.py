class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self,item):
        self.items.append(item)

    def delRear(self):
        return self.items.pop(0)

    def delFront(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def printStack(self):
        print self.items
        #print ''.join(self.items)

    def size(self):
        return len(self.items)


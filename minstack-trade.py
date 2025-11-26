from collections import defaultdict

class DoublyLiskedList:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Trade:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cache: dict[list[DoublyLiskedList]] = defaultdict(list)
        self.minstack: list = []

    def addTrade(self, val):
        node = DoublyLiskedList(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        self.cache[val].append(node)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def executeTrade(self):
        if not self.tail:
            return
         
        node = self.tail
        if node.prev:
            node.prev.next = None
            self.tail = node.prev
        val = node.val
        self.cache[val].pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def getMin(self):
        return self.minstack[-1]
    
    def cancelTrade(self, val):
        node = self.cache[val].pop()
        node_prev, node_next = node.prev, node.next
        if node_prev:
            node_prev.next = node_next
        else:
            self.head = node_next
        if node_next:
            node_next.prev = node_prev
        else:
            self.tail = node_prev
        if self.minstack and node.val == self.minstack[-1]:
            self.minstack.pop()


tr = Trade()

tr.addTrade(3)
tr.addTrade(5)
tr.addTrade(2)
tr.addTrade(5)
tr.addTrade(1)
print(tr.getMin())      # expected 1
tr.cancelTrade(5)       # removes the MOST RECENT 5
print(tr.getMin())      # expected 1
tr.cancelTrade(1)
print(tr.getMin())      # expected 2
tr.cancelTrade(3)
print(tr.getMin())      # expected 2



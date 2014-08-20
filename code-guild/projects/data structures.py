__author__ = 'grant'

"""
Nodes are the simplest way to store data.
They store data in an "item" variable,
and they store a pointer to the next node
called a "neighbor"
"""

class Node(object):
    def __init__(self, item, neighbor=None):
        self.item = item
        self.neighbor = neighbor

    def getItem(self):
        return self.item

    def getNeighbor(self):
        return self.neighbor

    def setItem(self):
        self.item = item

    def setNeighbor(self):
        self.neighbor = neighbor

"""A linked list is a sequentially searched list of nodes.
One node is the head node, and one node at the end of the
linked list is the tail node.  You can think of a metal
chain as an analogy.  Each link of the chain is linked to
another link, and you can't change that easily.  To add new
links and make the chain longer, you add new links to the
end of the existing chain.  Each time a node is added to a
linked list, it becomes the newest tail node.  Even though
a chain is a good visualization for a linked list, it isn't
perfect.  The nodes are not necessarily stored in physically
contiguous memory space.  The nodes keep track of each other
by storing a reference to their next neighbor instead."""

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, item):
        __doc__ = "Creates new nodes as tail nodes." \
                  "Checks to see if the appended node" \
                  "is the head node, and if not, it" \
                  "follows the getNeighbor method until" \
                  "it finds the existing tail node."
        newNode = Node(item)
        if self.head:
            node = self.head
            while node.getNeighbor():
                node = node.getNeighbor()
            node.setNeighbor(newNode)
        else:
            self.head = newNode

    def getItem(self, idx):
        __doc__ = "Finds a node by following the chain of" \
                  "getNeighbor methods through the range of idx."
        node = self.head
        for i in range(idx):
            node = node.getNeighbor()
        return node.getItem()

    def setItem(self, idx, item):
        __doc__ = "Updates a node by following the chain of" \
                  "getNeighbor methods through the range of idx."
        node = self.head
        for i in range(idx):
            node = node.getNeighbor()
        node.setItem(item)

"""
Array lists are a way of storing data that is more flexible
than a linked list.  Linked lists are great if you are
sequentially accessing nodes, but for non-sequential access,
or when the linked list becomes very large, it takes a long
time to follow the getNeighbor chain to the appropriate node.

Array lists allow for direct access at any given index without
following a chain of getNeighbor methods.  We are also able
to create or modify existing nodes at any given index.  The
array list must always be larger than the number of nodes it
contains.

Arrays in C are fixed in size, and they must be
"re-dimensionalized" to resize them to accommodate more nodes,
or shrink them to save memory.  In Python however, all lists
are implemented as array lists.
"""

class ArrayList(object):
    def __init__(self):
        init_size = 10
        self.array = [None] * init_size
        self.listLength = 0
        self.arrayLength = init_size

    def append(self, item):
        __doc__ = "Creates new nodes by first checking" \
                  "the size of the array list to make sure" \
                  "there is space to accommodate the new node," \
                  "then creates the node at the end of the" \
                  "array list."
        if self.listLength == self.arrayLength:
            self.array += [None] * self.arrayLength
            self.arrayLength *= 2
        self.array[self.listLength] = item
        self.listLength += 1

    def getItem(self, idx):
        __doc__ = "Returns the node at any given index"
        if idx >= self.listLength:
            raise Exception('index out of bounds')
        return self.array[idx]

    def setItem(self, idx, item):
        __doc__ = "Creates or updates an existing node" \
                  "at any given index."
        if idx >= self.listLength:
            raise Exception('index out of bounds')
        self.array[idx] = item

"""
Stacks and queues are also common structures you'll hear about.
To imagine a stack, think of a stack of papers.  You can only
add to the top of the stack, and similarly, you can only take
the top paper off the stack.  This is called "last in last out"
or LILO.  Another way of thinking about it is to imagine you
sell music records.  You want to put the most recent releases
right out in front.  They came in last, or most recently, and they
are going to be displayed front and center.

Imagining a queue isn't difficult.  Think of a line of people.
In the UK actually, people call a lineup a queue.  The last person
in line is the start of the queue, and they don't get to leave the
queue until they are the first in line.  Think of the grocery store
line.  This is called "first in first out" or FIFO.  Making a store
analogy, you sell milk.  Obviously you want to sell the oldest milk
before you sell the newest milk you just received so that none goes
bad in the cooler.
"""


class NodeStack(object):
    def __init__(self):
        self.top = None

    def push(self, item):
        __doc__ = "Creates a new node at the top of the stack."
        self.top = Node(item, self.top)

    def pop(self):
        __doc__ = "Checks if there is a node at the top" \
                  "then removes the top node."
        if self.top:
            item = self.top.getItem()
            self.top = self.top.getNeighbor()
            return item
        else:
            raise Exception('stack is empty')


class NodeQueue(object):
    def __init__(self):
        self.start = None

    def push(self, item):
        __doc__ = "Creates a new node at the start of the queue."
        self.start = Node(item, self.start)

    def pop(self):
        __doc__ = "While there is a node in the queue, it checks" \
                  "if it can access neighboring nodes, and when" \
                  "it reaches a node without a neighbor, it removes" \
                  "it from the start of the queue"
        while self.start.getNeighbor():
            nextItem = self.start.getNeighbor()
            return nextItem
        else:
            raise Exception('queue is empty')


class Hashtable(object):
    def __init__(self, size):
        self.size = size
        self.idx = [[] for x in range(size)]

    def setItem(self, item):
        hashKey = ord(item[0]) % (self.size + 1)
        self.idx[hashKey].append([hashKey, item])

    def getItem(self, key):
        return self.idx[key]

    def pop(self, key):
        self.idx.pop(key)






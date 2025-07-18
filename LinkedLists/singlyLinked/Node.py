class Node: #instantiate a random node, a node is basically an object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:#manage linked list
    def __init__(self):
        self.head = None #list has nothing yet
    def instertAtBeginning(self, new_data):  #reassignment of pointers : initialize node's field
        new_node = Node(new_data) #immediately creating a node: reference to user's element
        new_node.next = self.head   # reference to next node

        self.head = new_node
    def instertAtEnd(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            return
        last = self.head
        while last.next: #hold until we get to the last node in our linked list
            last = last.next
        last.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return "empty"
        self.head = self.head.next


    def deleteFromEnd(self):
        if self.head is None:
            return "list is empty"
        if self.head.next is None:  #if we have only one element
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None



    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    lList = LinkedList()
    lList.instertAtBeginning("fox")
    lList.instertAtBeginning("brown")
    lList.instertAtBeginning("quick")
    lList.instertAtBeginning("the")
    lList.instertAtBeginning("yooh")



    lList.instertAtEnd("brown")
    lList.instertAtEnd("jumps")
    lList.instertAtEnd("fast")

    lList.printLinkedList()
    lList.printLinkedList()

    lList.deleteFromBeginning()
    lList.deleteFromEnd()
    lList.printLinkedList()


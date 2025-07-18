#creation of singly linked list
from operator import truediv
from symtable import Class

class SinglyLinkedList: #Lightweight, nonpublic class for storing a singly linked node
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

snode1 = SinglyLinkedList("1")
snode2 = SinglyLinkedList("2")
snode3 = SinglyLinkedList("3")
snode4 = SinglyLinkedList("4")

snode1.nextNode = snode2
snode2.nextNode = snode3

currentNode = snode1
while True:
    print(currentNode.value, ">>>", end=' ')

    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode
k = 2
class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data
 
def reverseKNodes(h, k):
    temp = h
    count = 1
    while (count < k):
        temp = temp.next
        count = count + 1
        
    jp = temp.next
    temp.next = None
 
    prev = None
    current = h
    next = None
    while (current != None):
        next = current.next
        current.next = prev
        prev = current
        current = next
     
    h = prev
    current = h
    while (current.next != None):
        current = current.next
    current.next = jp
    return h
 
def push(h, new_data) :
    new_node = Node()
    new_node.data = new_data
    new_node.next = (h)
    (h) = new_node
    return h
 
def printList( head) :
    temp = head
    while (temp != None):
        print(temp.data, end = " ")
        temp = temp.next

head = None
head = push(head, input('Enter num1: '))
head = push(head, input('Enter num1: '))
head = push(head, input('Enter num1: '))
head = push(head, input('Enter num1: '))
head = push(head, input('Enter num1: '))
  
print("list: ")
printList(head)
print('-')
head = reverseKNodes(head, k)

print("list after reversing: ")
printList(head)

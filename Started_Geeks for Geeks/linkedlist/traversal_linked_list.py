class Node:
    def __init__(self,key):
        self.key = key 
        self.next = None 

def printlist(head):
    curr = head
    while curr !=None:
        print(f"{curr.key}->",end="")
        curr = curr.next


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3
head = temp1 
printlist(head)
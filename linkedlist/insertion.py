# AtBeginning => 
#create a temporary node
#set the next value of the tempnode to current headnode
#current headnode is tempnode
# AtEnd =>
#create a tempnode, inititate lastel which is current headnode iterating element 
#iterate through the linkedlist until find lastel.nxtnode as none
#set lastel.next as tempnode 
  
class Node:
    def __init__(self,datavalue) -> None:
        self.datavalue=datavalue
        self.nextvalue=None
class sLinkedList:
    def __init__(self) -> None:
        self.headvalue=None
    def printList(self):
        current=self.headvalue
        while(current is not None):
            print(current.datavalue)
            current=current.nextvalue
    def AtBeginning(self, newvalue):
        tempNode=Node(newvalue)
        tempNode.nextvalue=self.headvalue
        self.headvalue=tempNode
    def AtEnd(self, newvalue):
        tempNode=Node(newvalue)
        lastel=self.headvalue
        while(lastel.nextvalue):
            lastel=lastel.nextvalue
        lastel.nextvalue=tempNode





head=sLinkedList()
head.headvalue=Node("mon")
body1=Node("tue")
body2=Node("wed")
body3=Node("thu")
head.headvalue.nextvalue=body1
body1.nextvalue=body2
body2.nextvalue=body3
body3.nextvalue=None
head.printList()
head.AtBeginning("sun")
print("after insertion at beginning")
head.printList()
head.AtEnd("friday")
print("after insertion at the end")
head.printList()
print("again printing it")
head.printList()
# head.printList()
# print("let us now enter new value at the beginning")
# newval="sun"
# head.AtBeginning(newval)
# head.printList()

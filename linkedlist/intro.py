# Description 
# two classes Node and sLinkedList
# Node has two values datavalue and nextvalue
# sLinkedList has one value headvalue
# initially this headvalue is one of the node and has a datavalue
# create other nodes 
# link this nodes => headvalue.nextvalue is the next node and likewise
## printList function inside sLinkedList => iterates through linkedlist datavalue and switches to nextvalue after printing


class Node:
    def __init__(self,datavalue) -> None:
        self.datavalue=datavalue
        self.nextvalue=None
class sLinkedList:
    def __init__(self) -> None:
        self.headvalue=None

    def printList(self):
        while(self.headvalue is not None):
            print(self.headvalue.datavalue)
            self.headvalue=self.headvalue.nextvalue


head=sLinkedList()
head.headvalue=Node("Mon")
body1=Node("Tue")
body2=Node("Wed")
head.headvalue.nextvalue=body1
body1.nextvalue=body2
body2.nextvalue=None 

head.printList()

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
       




head=sLinkedList()
head.headvalue=Node("mon")
body1=Node("tue")
body2=Node("wed")
body3=Node("thu")
head.headvalue.nextvalue=body1
body1.nextvalue=body2
body2.nextvalue=body3
body3.nextvalue=None
print(head.headvalue.datavalue)
head.printList()
print(head.headvalue.datavalue)
# head.AtBeginning("sun")
# head.printList()
# print("let us now enter new value at the beginning")
# newval="sun"
# head.AtBeginning(newval)
# head.printList()

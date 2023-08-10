# stack is generally last in first out whereas queue is first in first out 

class StackUsingQueue:
    # main list is queue1 
    # supporting list is queue2 
    def __init__(self):
        self.queue1=list()
        self.queue2=list()
    # add a new element to queue1
    def push(self,x):
        self.queue1.append(x)
    # removing element from queue1 using queue
    # first append all the elements in queue1 to queue2 excpet last element
    # then pop(0) to last_el => return last_el in the end 
    # now swap queue1 and queue2 as queue1 is the main list 
    def pop(self):
        if not self.queue1: return None 
        while(len(self.queue1)>1):
            self.queue2.append(self.queue1.pop(0))
        last_el=self.queue1.pop(0)
        self.queue1,self.queue2=self.queue2,self.queue1
        print(self.queue1)
        print(self.queue2)
        return last_el

output=StackUsingQueue()
output.queue1=[1,2,3,4]
output.queue1.append(5)
result=output.pop()
print(result)
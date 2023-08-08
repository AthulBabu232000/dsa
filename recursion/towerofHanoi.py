# tower of Hanoi is a recursive problem 
# there are three towers 
# source,helper,destination => source tower has n disks
# task: move all disk to destination find number of times disks are moved
# you can move one disk at a time
# smaller disks can only be placed over larger disks not viceversa 


n:int=int(input("enter the number of disks to be transferred: "))
def hanoi_tower(n,source,helper,destination):
    if n==1:
        print(f"disc {n} is transferred from {source} to {destination}")
        return
    hanoi_tower(n-1,source,destination,helper)
    print(f"disc {n} is transferred from {source} to {destination}")
    hanoi_tower(n-1,helper,source,destination)
hanoi_tower(n,"S","H","D")

# consider a stack to three disc disc1 disc2 disc3 
# disc 1 on top
# disc 2 on middle
# disc 3 on bottom 


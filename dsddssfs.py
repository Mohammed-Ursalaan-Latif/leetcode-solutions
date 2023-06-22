##stacks##
##top=0
##
##def pop(listname):
##     if len(listname)>1:
##          del listname[-1]
##          top=listname[-1]
##          print (listname)
##     elif len(listname)==1:
##          del listname[-1]
##          print("empty")
##     else:
##          print("cant empty an empty list")
##    
##def add(listname,x):
##     listname.append(x)
##   
##nums=[1,2,4,5,7,2]
##pop(nums)
##pop(nums)
##pop(nums)
##pop(nums)
##pop(nums)
##pop(nums)
##add(nums,4)
##print(nums)
##pop(nums)    
##pop(nums)

##queue##

#adds to back using enque
#removes from front using deque

#queue implementation start
##nums=[1,2,4,5,7,2]
##
##def deque(listname):
##     #check if empty
##     if not listname:
##          print("queue is empty")
##     #remove front item from queue
##     else:
##          listname.pop()
##     #test out code
##     print(listname)
##
##def enque(listname,item):
##     #insert item at back of queue i.e. index 0
##     listname.insert(0,item)
##     #test out code
##     print(listname)
##
##enque(nums,3)
##deque(nums)
##enque(nums,22)
##enque(nums,19)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)
##deque(nums)

#linked list
class node(object):

     def __init__(self,data,nextnode=None):
          self.data=data
          self.nextnode=nextnode
     def getnextnode(self):
          return self.nextnode
     def setnextnode(self,value):
          self.nextnode=value
     def getdata(self):
          return self.data
     def setdata(self,value):
          self.data=value

class Linkedlist():
     root=None
     size=0
     def __init__(self,root,size=None):
          self.root=root
          self.size=size
     ##add
          def add(x):
               newnode=node(x,root)
               self.root=newnode
               self.size+=1
     ##remove
     ##find
         

###Deletion...........

class Node:
    def __init__(self,key):
        
        
        self.key =key
        self.left=None
        self.right= None
def insert(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->",end='')
        inorder(root,right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key< node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left = deleteNode(root.left,key)
    elif(key > root.key):
        root.left = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root
root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
print("inorder traversal:",end='')
inorder(root)
print("\nDelete 4")
root = deleteNode(root,6)
prit("inorder traversal:",end='')
inorder(root)

#even odd queue....................

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front> self.__rear):
            return True
        return False
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])
    def odd_element(self):
        for index in range(q1.__front,q1.__rear+1):
            if(q1.__element[index]%2!=0):
                self.enqueue(q1.__element[index])
    def even_element(self):
        for index in range(q1.__front,q1.__rear+1):
            if(q1.__element[index]%2==0):
                self.enqueue(q1.__element[index])
    
q1=Queue(8)
q1.enqueue(2)
q1.enqueue(7)
q1.enqueue(9)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(5)
q1.enqueue(10)
q1.display()
odd=Queue(8)
odd.odd_element()
print("odd queue")
odd.display()
even=Queue(8)
even.even_element()
print("even queue")
even.display()
'''

#merges the two linked lists................

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
def merge_lists(list1,list2,n):
    curr_node = list1
    for i in range(n-1):
        curr_node = curr_node.next
    next_node = curr_node.next
    curr_node.next = list2

    while list2.next:
        list2 = list2.node
    list2.next = next_node

    return list1
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(5)
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)
merged_list=merge_lists(list1,list2,2)
while merged_list:
    print(merged_list.data, end='->')
    merged_list = merged_list.next'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_lists(list1, list2, n):
    curr_node = list1
    for i in range(n-1):
        curr_node = curr_node.next
        
    next_node = curr_node.next
    curr_node.next = list2
    
    while list2.next:
        list2 = list2.next
    list2.next = next_node
    
    return list1
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(5)
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)
merged_list = merge_lists(list1, list2, 2)
while merged_list:
    print(merged_list.data, end="->")
    merged_list = merged_list.next

###replace maximum element by given element-----------
#Old List
#12 -> 95 -> 140 -> 110 -> 40 ->  n=3
#New List
#12 -> 95 -> 3 -> 110 -> 40 -> 

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class Slinkedlist():
    def __init__(self):
        self.head=None
    def replace(self,n):
        start=self.head
        large=0
        while(start is not None):
            if(start.data>large):
                large=start.data
                add=start
            start=start.next
        
        add.data=n
    def display(self):
        start=self.head
        while(start is not None):
            print(start.data,"->",end=" ")
            start=start.next
        
list1=Slinkedlist()
list1.head=Node(12)
e2=Node(95)
e3=Node(140)
e4=Node(110)
e5=Node(40)
#linking the node
list1.head.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
n=int(input())
print("Old List")
list1.display()
print("\nNew List")
list1.replace(n)
list1.display()

#print detail by choice of gender.................

class Node:
    def __init__(self,name,age,gender):
        self.next=None
        self.name=name
        self.age=age
        self.gender=gender
class Slinkedlist():
    def __init__(self):
        self.head=None
    def display(self,ch):
        start=self.head
        while(start is not None):
            if(start.gender == ch):
                print(start.name," " ,start.age," ",start.gender)
            start=start.next
list1=Slinkedlist()
list1.head=Node("Sibanilaal",21,"Female")
e2=Node("Annalaal",20,"Female")
e3=Node("Sarthaklaali",21,"Male")
e4=Node("Shrutilaal",21,"Female")
e5=Node("Tanaylaali",20,"Male")
#linking the node
list1.head.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
ch=input("Enter the gender to be searched")
list1.display(ch)

#.................triangle number................
#7 -> 28 -> 8 -> 35 -> 3 -> 6 -> 5 -> 15 -> 2 -> 5 -> 
#The triangle numbers are
#15
#6
#28
'''
class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__element[self.__top]=data
            
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index-=1
        
class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size #[None,None,None,None]
        self.rear=-1
        self.front=0
    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.rear+=1
            self.element[self.rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data=self.element[self.front]
            self.front+=1
            return data
    def is_full(self):
        if(self.rear==self.max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.front> self.rear):
            return True
        return False
    def second_check(self):
        first=self.dequeue()
        second=self.dequeue()
        sum1=0
        while(self.front<self.rear):
            for i in range(1,first+1):
                sum1+=i
            if(sum1== second):
                s1.push(second)
            first=self.dequeue()
            second=self.dequeue()
            sum1=0
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index],"->",end=" ")       
        
q1=Queue(10)
q1.enqueue(7)
q1.enqueue(28)
q1.enqueue(8)
q1.enqueue(35)
q1.enqueue(3)
q1.enqueue(6)
q1.enqueue(5)
q1.enqueue(15)
q1.enqueue(2)
q1.enqueue(5)
q1.display()
s1=stack(10)
q1.second_check()
print()
print("The triangle numbers are")
s1.display()


    



            

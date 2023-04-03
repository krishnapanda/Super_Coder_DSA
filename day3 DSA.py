#Doubly Link List
#Operation : insert , delete , length , isempty

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self):
        prev = None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head = prev
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
list = LinkedList()
list.push(20)
list.push(4)
list.push(15)
list.push(85)
print("given linked list")
list.printList()
list.reverse()
print("\nReversed linked list")
list.printList()'''

'''#DoublyLinkedList
class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
    def printLinkedList(self):
         temp=self.head
         while temp is not None:
             print(temp.data,sep=",")
             temp = temp.next
    def insertAtEnd(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
    def insertAtPosition(self,value,position):
        temp = self.head
        count = 1
        while temp is not None:
            if count == position - 1:
                break
            count +=1
            temp = temp.next
            if position == 1:
                self.insertAtBeginning(value)
            elif temp is None:
                print("there are less than {}-1 elements in linked List.Cannot insert at {}position".format(position,position))
            elif temp.next is None:
                self.insertAtEnd(value)
            else:
                new_node=Node(value)
                new_node.next=temp.next
                new_node.previous=temp
                temp.next.previous=new_node
                temp.next=new_node
    def deleteFromBegining(self):
            if self.isEmpty():
                print("Linked List is empty is empty.Cannot delete elements")
            elif self.head.next is None:
                self.head=None
            else:
                self.head=self.head.next
                self.head.previous=None
       # def deleteFromLast(self):




    def deleteFromPosition(self,position):
            if self.isEmpty():
                print("linked list is empty.Connot delete elements.")
            elif position == 1:
                self.deleteFromBegining()
            else:
                temp = self.head
                count = 1
                while temp is not None:
                    if count == position:
                        break
                    temp= temp.next
                    count=count+1
                if temp is None:
                    print("there are less than{} elements in linked List.Cannot insert")
                elif temp is None:
                    self.deleteFromLast()
                temp.previous.next=temp.next
                temp.next.previous=temp.previous
                temp.next=None
                temp.previous=None
                
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("delete data at 2nd position")
x.deleteFromPosition(2)
x.printLinkedList()

##Deleting duplicacy from the doubly linked list...............

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dlinkedlist:
    def __init__(self):
        self.head=None
        
    def listprint(self):
        start=self.head
        while(start is not None):
            print(start.data)
            start=start.next
    def delete_end(self):
        end=self.head
        while(end.next.next is not None):
            end=end.next
        end.next=None
        return
    def remove_duplicate(self):
        start=self.head
        while(start is not None):
            dup=start.next
            while(dup is not None):
                if(dup.data == start.data):
                    if(dup.next is not None):
                        start.next=dup.next
                        dup.next.prev=start
                        dup=dup.next
                        continue
                    else:
                        self.delete_end()
                        break
                dup=dup.next
            start=start.next
            
list1=Dlinkedlist()
list1.head=Node(11)
n2=Node(10)
n3=Node(3)
n4=Node(7)
n5=Node(7)
n6=Node(10)
#linking the nodes
list1.head.next=n2
n2.prev=list1.head
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
n5.next=n6
n6.prev=n5
print("The list is")
list1.listprint()
print("After removing duplicacy")
list1.remove_duplicate()
list1.listprint()


#Postfix Evaluation..........
class Evaluate:
    def __init__(self,capacity):
        self.array=[]
        self.top=-1
        self.capacity=capacity
    def isempty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def pop(self):
        if(not self.isempty()):
            self.top-=1
            return self.array.pop()
        else:
            return ("$")
    def push(self,op):
        self.top+=1
        self.array.append(op)
    
    def postfixevaluation(self,exp):
        for i in exp:
            if(i.isdigit()):
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())
if __name__=="__main__":
    exp="231*+9-"
    obj=Evaluate(len(exp))
    print(obj.postfixevaluation(exp))

##smaller number is in bottom and greater number is in the top............

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__top=-1
        self.__array=[]
    def isempty(self):
        if(self.__top==-1):
            return True
        else:
            return False
    def pop(self):
        n=self.__element[self.__top]
        self.__top-=1
        return n
    def push(self,op):
        self.__top+=1
        self.__element[self.__top]=op
            
    def get_max_size(self):
        return self.__max_size
    
    def arrange(self):
        index=self.__top
        while(index>=0):
            n=self.pop()
            self.__array.append(n)
            index-=1
        self.__array.sort()
        for i in self.__array:
            self.push(i)
    def display(self):
        index=self.__top
        while(index >=0):
            print(self.__element[index])
            index-=1
        return
s1=Stack(5)
s1.push(5)
s1.push(66)
s1.push(5)
s1.push(8)
s1.push(7)
print("The stack is ")
s1.display()
print("The sorted stack is")
s1.arrange()
s1.display()






           

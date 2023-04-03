# Operation in stack :#isempty
                      #isfull
                      #top
                      #push
                      #pop
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if (self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("the stack is full!!")
        else:
            self.__top+=1
            self.__elements[self._top]=data
    def pop(self):
        if(self.is_empty()):
            print("the stack is empty!!")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(seld.is_empty()):
            print("the stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size
    ball_stack=Stack(4)
    print("Is it empty",ball_stack.is_empty())
    ball_stack.push(5)
    print("is it empty",ball_stack.is_empty())
    ball_stack.push(6)
    ball_stack.push(7)
    ball_stack.push(8)
    ball_stack.display()
    print("size of the stack",ball_stack.get_max_size())
    print("the element deleted",ball_stack.pop())
    print("after deleting the element")
    ball_stack.display()
    print("size o fthe stack",ball_stack.get_max_size())

  #####ENQUE(add data in the rear)
 #dequeue(remove data from the front)

class Queue:
    
    def __init__(self,max_size):
        
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_siz-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rare+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
queue1=Queue(4)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()

queue1.enqueue(500)
queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()

#write a python program to return a new queue which contains .....
class Queue:
    
    def init(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below str() to print the elements of the DS object while debugging
    def str(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def check_numbers(number_queue):
    #write your logic here  
    size=number_queue.get_max_size()
    solution_queue1=Queue(size)
    while size>0:
        element=number_queue.dequeue()
        if all(element%i==0 for i in range(1,11)):
            solution_queue1.enqueue(element)
        size-=1 
    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)

#problem 3...........

l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
l3=l2[::-1]
str1=""
for i in range(0,len(l1)):
    if(l1[i]!=None and l3[i]!=None):
        str1+=l1[i]
        str1+=l3[i]
        str1+=" "
    elif(l1[i]==None):
        str1+=l3[i]
        str1+=" "
    else:
        str1+=l1[i]
        str1+=" "
print(str1)

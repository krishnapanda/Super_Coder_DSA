'''# Selection sort
def selectionSort(array,size):
    for step in range(size):
        min_idx = step
        
        for i in range(step + 1,size):
            if array[i] < array[min_idx]:
                min_idx = i
            
        (array[step],array[min_idx]) = (array[min_idx], array[step])
        
data = [20,12,10,15,2]
size = len(data)
selectionSort(data,size)
print("Sorted array in ascending order:")
print(data)

#Fruit Farms  (Class Diagram)

class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name)]
        else:
            return -1


class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity, is_wholesale):
        self.__purchase_id = "P" + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__is_wholesale = is_wholesale

    def calculate_price(self):
        price = FruitInfo.get_fruit_price(self.__fruit_name)
        if price == -1:
            return -1
        else:
            total_price = price * self.__quantity
            max_price_fruit = max(FruitInfo.fruit_price_list)
            min_price_fruit = min(FruitInfo.fruit_price_list)
            if price == max_price_fruit and self.__quantity > 1:
                total_price *= 0.98
            elif price == min_price_fruit and self.__quantity >= 5:
                total_price *= 0.95
            if self.__is_wholesale:
                total_price *= 0.9
            return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

    def get_is_wholesale(self):
        return self.__is_wholesale


class Customer:
    def __init__(self, customer_name, phone_number):
        self.__customer_name = customer_name
        self.__phone_number = phone_number

    def get_customer_name(self):
        return self.__customer_name

    def get_phone_number(self):
        return self.__phone_number
customer = Customer("John", "9876543210")
purchase = Purchase(customer, "Grape", 6, True)
final_price = purchase.calculate_price()
print("Purchase ID:", purchase.get_purchase_id())
print("Customer Name:", purchase.get_customer().get_customer_name())
print("Customer Phone Number:", purchase.get_customer().get_phone_number())
print("Fruit Name:", purchase.get_fruit_name())
print("Quantity:", purchase.get_quantity())
print("Is Wholesale:", purchase.get_is_wholesale())
print("Final Price:",final_price)

#the owner of a blke house wants to keep to keep track of the table.......................

class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        if not self.occupied_table_list: 
            self.occupied_table_list.append(1) 
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list) - 1: 
                    self.occupied_table_list.append(self.occupied_table_list[i] + 1) 
                elif self.occupied_table_list[i+1] != self.occupied_table_list[i] + 1: 
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i] + 1) 
                    break

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print_list() 
my_list.reverse()
my_list.print_list()'''


#Softeams Ltd is a private firm that provides software solution.................

class Employee:
    def __init__(self, emp_id, emp_name, basic_salary, qualification):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.qualification = qualification
    
    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False
    
    def validate_qualification(self):
        if self.qualification.lower() == "bachelors" or self.qualification.lower() == "masters":
            return True
        else:
            return False

class Graduate(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, cgpa):
        super().init(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa
    
    def validate_job_band(self):
        if self.job_band.upper() in ["A", "B", "C"]:
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band.upper() == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band.upper() == "C":
                incentive = 0.1 * self.basic_salary
            
            if self.cgpa >= 4 and self.cgpa <= 4.25:
                tpi = 1000
            elif self.cgpa > 4.25 and self.cgpa <= 4.5:
                tpi = 1700
            elif self.cgpa > 4.5 and self.cgpa <= 4.75:
                tpi = 3200
            elif self.cgpa > 4.75 and self.cgpa <= 5:
                tpi = 5000
                
            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

class Lateral(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, skill_set):
        super().init(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set
    
    def validate_job_band(self):
        if self.job_band.upper() in ["D", "E", "F"]:
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band.upper() == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band.upper() == "F":
                incentive = 0.2 * self.basic_salary
            
            sme_bonus = 0
            if self.skill_set.lower() == "agp":
                sme_bonus = 6500
            elif self.skill_set.lower() == "agpt":
                sme_bonus = 8200
            elif self.skill_set.lower() == "agdev":
                sme_bonus = 11500
                
    calculate_gross_salary


#CHildrenCAMP

class ChildrenCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received

    def calculate_total_chocolates(self):
        return sum(self.chocolates_received)

    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            return "Extra chocolates is less than 1"
        if child_id_rewarded not in self.child_id:
            return "Child id is invalid"
        index = self.child_id.index(child_id_rewarded)
        self.chocolates_received[index] += extra_chocolates
        return self.chocolates_received

child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChildrenCamp(child_id, chocolates_received)
print(camp.calculate_total_chocolates()) 

print(camp.reward_child(30, 2)) 
print(camp.calculate_total_chocolates()) 

print(camp.reward_child(60, 2)) 

print(camp.reward_child(40,0))


#Anagram.................
def check_anagram(str1,str2):
    l1=list(str1)
    l2=list(str2)
    if len(l1)==len(l2):
        for i in l1:
            if i in l2:
                if str1!=str:
                    return True
    return False
print(check_anagram('anagram','ramnaga'))      

#bubble sort
'''def bubblesort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
arr=[5,3,7,6,2]
n=len(arr)
bubblesort(arr,n)
print(arr)'''
def bubblesort(arr,n):
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[5,3,7,6,2]
n=len(arr)
bubblesort(arr,n)
print(arr)                
            

##Quicksort..................
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
        
arr=[7,8,4,2,9,6,1]
low=0
high=len(arr)-1
quicksort(arr,low,high)
print(arr)        

##Selection sort..............
def selectionsort(arr,s):
    for step in range(s):
        min_ind=step
        for i in range(step+1,s):
            if arr[i]<arr[min_ind]:
                min_ind=i
        (arr[step],arr[min_ind])=(arr[min_ind],arr[step])
data=[1,2,3,4,5,6,0]
s=len(data)
selectionsort(data,s)
print(data)




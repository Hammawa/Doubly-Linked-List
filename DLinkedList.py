#----------------------------------------------------
# Lab 7, Exercise 2: Doubly Linked Lists
# TO DO: complete mandatory methods in DLinkedList class
# TO DO (optional): complete optional methods in DLinkedList class
# to get better understanding of manipulating linked lists
#
# Author: 
# Collaborators/references: Abdullah Hammawa, 1619949
#   - CMPUT 175 provided complete DLinkedListNode
#   - CMPUT 175 provided init, search, index methods for DLinkedList
#   - CMPUT 175 provided tests for DLinkedList
#----------------------------------------------------


class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
        
    def insert(self, pos, item):
        # TODO: mandatory
        # inserts the item at pos
        # pos should be a positive number (or zero) of type int
        # TO DO: write assert statement that tests if pos is int
        assert type(pos) == int, "The position must be given as an integer value."
        # TO DO: write assert statement that tests that pos is not negative
        assert pos >= 0, "The position must be given as a positive integer value."
        # TO DO: delete pass and COMPLETE THE METHOD 
        if pos == 0:
            self.add(item)
        elif pos == self.__size:#and pos != 1:
            self.append(item)   
        else:
            #traverse the list starting from the head until I get the node that will serve as the initNext for the node I'm inserting
            #keep track of the node which will becom the previous node so that I can use the setNext() method to attach said node to my new inserted node
            current = self.__head
            i = 0
            while (i+1) < pos:
                current = current.getNext()
                previous_node = current
                i += 1        
            new_next = previous_node.getNext()
            inserted_node = DLinkedListNode(item, new_next, previous_node)
            new_next.setPrevious(inserted_node)
            previous_node.setNext(inserted_node) 
            self.__size += 1        

    def searchLarger(self, item):
        # TODO: mandatory
        is_number = (type(item) == int or type(item) == float)
        assert is_number == True, "The argument for the searchLarger method must be a number"
        current = self.__head
        is_bigger = False
        traversed_list = (current.getNext() == None)
        while is_bigger == False and traversed_list == False:
            #get data of each node and check if its bigger than the argument
            data = current.getData()
            is_bigger = (data > item)
            current = current.getNext()
            traversed_list = (current.getNext()==None)
        if is_bigger == True and traversed_list == False:
            index = self.index(data)
        elif traversed_list == True:
            data = current.getData()
            is_bigger =  (data > item)
            if is_bigger:
                index = self.index(data)
            else:
                index = -1
        return index        
    
    def getSize(self):
        # TODO: mandatory   
        return self.__size
    
    def getItem(self, pos):
        # TODO: mandatory 
        is_in_list = (pos <= self.__size and pos >= -self.__size)
        assert is_in_list == True, "The given position is outside of the list"
        is_empty = (self.__size == 0)
        assert is_empty == False, "There are no items in this list"
        if pos == 0:
            item = self.__head.getData()
        elif pos > 0:
            i = 0
            current = self.__head
            while i < pos:
                current = current.getNext()
                i += 1
                item = current.getData()
        elif pos < 0:
            i = 0
            current = self.__head
            while i < self.__size + pos:
                current = current.getNext()
                i += 1
                item = current.getData()
        return item        
        
    def __str__(self):
        # TODO: mandatory  
        # returns a string representation of the list
        current = self.__head
        first = True
        if first == True:
            string = str(current.getData())
            current = current.getNext()
            first = False
        while first == False and current != None:
            string = string + ' ' + str(current.getData())
            current = current.getNext()    
        return string        



    def add(self, item):
        # optional exercise
        # adds an item at the start of the list
        new_node = DLinkedListNode(item,None,None)
        new_node.setNext(self.__head)
        if self.__size == 0:   
            self.__head = new_node
        else:
            self.__head.setPrevious(new_node)
            new_node.setNext(self.__head)
            self.__head = new_node
        self.__size = self.__size + 1        
        
    def remove(self, item):
        # optional exercise
        pass
        
    def append(self, item):
        # optional exercise
        # adds an item at the end of the list
        new_node = DLinkedListNode(item,None,None)
        current = self.__head # Start the traversal
        if self.__size == 0: # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            new_node.setPrevious(current)
            current.setNext(new_node)
           #new_node.setPrevious(current)
            self.__tail = new_node
            self.__size = self.__size + 1        
        
        
    def pop1(self):
        # optional exercise
        pass
    
    def pop(self, pos=None):
        # optional exercise
        # Hint - incorporate pop1 when no pos argument is given
        pass
        
    

def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.insert(0, "Hello")
    linked_list.insert(1, "World")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    '''
    OPTIONAL TESTS FOR OPTIONAL EXERCISE - do not need to demo
    '''
    '''
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
    '''
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(9, -1, -1):
        int_list.insert(0,i)      
            
    is_pass = (int_list.getSize() == 10)
    assert is_pass == True, "fail the test"            
            
    is_pass = (int_list.searchLarger(8) == 9)
    assert is_pass == True, int_list.searchLarger(8)
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
                  
    is_pass = (int_list.getItem(-1) == 9)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 801)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
                
if __name__ == '__main__':
    test()

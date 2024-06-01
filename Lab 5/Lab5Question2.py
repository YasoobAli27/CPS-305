#Syed Yasoob Ali
#500953533

#Lab 5, Question 2
#Assistance recieved from GeeksforGeeks website


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class PLinkedList:
    def __init__(self):
        self.head = None
  
  

def InsertAtEnd(self, newdata):
    NewNode = Node(newdata)
    if self.head is None:
        self.head = NewNode
        return
    temp = self.head
    while(temp.next):
        temp = temp.next
        temp.next=NewNode
  
#a
def Listsearch(self, val):
    temp = self.head
    count=0
    while temp != None:
        count=count+1
        if temp.data == val:
            print('Found at position:',count)
            return True 
  
    temp = temp.next
    return False 

#b
def Reverselist(self):
    prev = None
    temp = self.head
    while(temp is not None):
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
        self.head = prev
  

def Listdisplay(self):
    temp = self.head
    while (temp):
        print(temp.data)
        temp = temp.next

Plist = PLinkedList()
Plist.InsertAtEnd(9)
Plist.InsertAtEnd(12)
Plist.InsertAtEnd(4)
Plist.Listdisplay()
if Plist.Listsearch(5)==False:
    print('Not Found')
Plist.Reverselist()
print('List after reverse')
Plist.Listdisplay()

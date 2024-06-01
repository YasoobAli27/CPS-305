#Syed Yasoob Ali
#500953533

#Lab 5, Question 1
#Used GeeksforGeeks website for assistance


class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None


class PLinkedList:
    def __init__(self):
        self.head = None

        #a
        def DeleteFirst(self):
            if (self.head is None):
                print("No Node")
            else:
                temp = self.head.next
                temp = None
                print("Deleted")

        #b
        def InsertEnd(self, newdata):
            NewNode = Node(newdata)
            if self.head is None:
                self.head = newNode
                return
            temp = self.head
            while(temp.next):
                temp = temp.next
                temp.next = NewNode

        #c
        def DeleteNodePos(self,pos):
            temp = self.head
            count = 0
            if(self.head is not None and pos ==1):
                self.head = self.head.next
                temp = None
                print("Deleted")
                return
            prev = self.head
            flag = 0
            while(temp is not None):
                count += 1
                if count == pos:
                    prev.next = temp.next
                    temp = None
                    print("Deleted")
                    flag = 1
                    break
                prev = temp
                temp = temp.next
                if flag == 0:
                    print("No node exists at this position")

        #Output
        def Listdisplay(self):
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

Plist = PLinkedList()
Plist.InsertEnd(4)
Plist.InsertEnd(5)
Plist.InsertEnd(7)
Plist.Listdisplay()
Plist.DeleteFirst()
Plist.Listdisplay()
Plist.DeleteNodePos(2)
Plist.Listdisplay()
Plist.DeleteNodePos(2)


                
                
            
                
                
        

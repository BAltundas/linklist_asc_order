# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:34:58 2021

@author: Bilgin Altundas
"""
# function to insert a Node at required position
def insertPos(root, position, data): 
    cur_node = root.head
     
    # This condition to check whether the
    # position given is valid or not.
    if (position < 1):        
        print("Invalid position!")
     
    # if position == 1:
    #print(head.next.nval,data)
    if cur_node.next.nval > data:
        print('here')
        newNode = Node(data)
        newNode.next = cur_node
        cur_node.next = newNode    
        print(cur_node.next.nval)
    else:
       
        # Keep looping until the position is zero
        while (position != 0):           
            position -= 1
  
            if (position == 1):
  
               # adding Node at required position
               newNode = Node(data)
 
               # Making the new Node to point to
               # the old Node at the same position
               newNode.next = cur_node.next
 
               # Replacing headNode with new Node
               # to the old Node to point to the new Node
               cur_node.next = newNode
               break
             
            cur_node = cur_node.next
            if cur_node == None:
                break           
        if position != 1:
              print("position out of range")        
    return cur_node

############## Create a Node and List in Ascending order    
class Node:
    def __init__(self,data=None):
        self.next =None
        self.nval =data
    
class CreateListASC:
    def __init__(self):
        self.head = Node()    
    
    def display(self):
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            print(cur_node.nval,end=' ')
         
    def insertInASC(self, new_data): 
        last_node = self.head
        
        if last_node is None:
            return Node(new_data)
        
        if last_node is None: 
            print("The given previous node must inLinkedList.")
            return      
        new_node = Node(new_data)        
        while last_node.next!=None:
            prev_node = last_node
            last_node = last_node.next
            if last_node.nval>new_data:
                prev_node.next = new_node
                new_node.next = last_node
                return 
            else:
                continue      
        last_node.next = new_node
        return 
            
mylist = CreateListASC()
mylist.insertInASC(15)
mylist.insertInASC(5)
mylist.insertInASC(25)
mylist.insertInASC(1)
mylist.display()


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_beg(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head= new_node

    def print_list(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    def remove_item(self):
        pass

    def reverse_list(self):
        prev=None
        curr=self.head
        while(curr !=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev


list = LinkedList()
list.insert_node_at_beg(23)
list.insert_node_at_beg(24)
list.insert_node_at_beg(25)
list.insert_node_at_beg(26)
list.print_list()
print("#####")
list.reverse_list()
list.print_list()

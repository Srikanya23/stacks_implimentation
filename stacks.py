class node :
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self) :
        self.top=None

    def is_empty(self):
        return (self.top==None)
    def push(self,value):
        new_node=node(value)
        new_node.next =self.top
        self.top=new_node
    def display(self):
        current=self.top
        while current!= None:
            print(current.data)
            current=current.next
    def pop(self):
        if self.is_empty():
            return 'Empty Stack'
        current=self.top
        self.top=current.next
        return current.data
    def peek(self):
        if self.is_empty():
            return 'Empty Stack'
        else :
            return self.top.data
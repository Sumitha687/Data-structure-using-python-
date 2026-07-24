class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newNode=Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
        else:
            self.rear.next=newNode
            self.next=newNode
        print(data,"enqueued successfully")
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp=self.front
        print(temp.data,"dequeueed successfully")
        self.front=self.front.next
        if self.front is None:
            self.rear=None
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp=self.front
        print("queue elements:")
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("Null")
q=Queue()
while True:
    print("\n--QUEUE USING LINKED LIST--")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=input("Enter car number:")
        q.enqueue(value)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.display()
    elif choice==4:
        print("Program ended")
        break
    else:
        print("Invalid choice")
    

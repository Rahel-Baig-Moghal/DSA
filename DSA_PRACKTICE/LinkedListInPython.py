class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.head
        lstr = ''

        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)      
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count+=1
            itr=itr.next
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count+=1
            itr=itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if data_after == itr.data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr=itr.next
    
    def remove_by_value(self, data):
        count=0
        itr = self.head
        while itr:
            if data == itr.data:
                itr.next = itr.next.next
                break
            count+=1
            itr=itr.next





if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['mango', 'grapes', 'melon', 'lemon'])
    ll.print()
    ll.insert_after_value("lemon","apple") 
    ll.print()
    ll.remove_by_value("melon")
    ll.print()

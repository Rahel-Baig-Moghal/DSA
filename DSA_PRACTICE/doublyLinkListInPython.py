class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node 

    def print_forward(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.head
        lstr = ''

        while itr:
            lstr +=  str(itr.data) + '-->'
            itr = itr.next
        print(lstr+'None')

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)      
    
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

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr=last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr=itr.prev

        print(llstr+'None')



if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(['mango', 'grapes', 'melon', 'lemon'])
    ll.print_forward()
    ll.print_backward()
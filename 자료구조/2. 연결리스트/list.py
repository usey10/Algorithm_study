# 연결리스트를 구현하고, 연결리스트의 기능을 테스트하세요!
# 아래 제공된 기본 틀을 이용하여 구현하세요.

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# solution
# 구현 진행시 고려해야 할 사항
# 1. 일반적인 경우에 잘 동작 하는지?
# 2. edge 케이스 확인 필요

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
        # edge case : 처음 연결 리스트가 비어있을 때 동작 하는지? -> O

    def append(self, value):
        curr = self.head

        # edge case : 처음 연결 리스트가 비어있을 때 잘 동작하는지? 
        if curr is None:
            self.head = Node(value,None)
            return
        
        while curr.next is not None:
            curr = curr.next
        node = Node(value, None)
        curr.next = node


    def set_head(self, index):
        curr = self.head
        for _ in range(index):
            # edge case : index > N
            if curr is None:
                return
            curr = curr.next
        # edge case : index == N
        if curr is None:
            return
        self.head = curr
            
    def access(self, index):
        curr = self.head
        for _ in range(index):
            # edge case : index > N
            if curr is None:
                return None
            curr = curr.next
        # edge case : index == N
        if curr is None:
            return None
        return curr.value

    def insert(self, index, value):
        # edge case : index == 0
        if index == 0:
            self.prepend(value)
            return
        
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return
            prev = curr
            curr = curr.next
        node = Node(value, curr)
        prev.next = node
        # edge case : index > N 동작 O


    def remove(self, index):
        # edge case : index = 0
        # my answer
        if index == 0:
            self.set_head(1)
            return
        
        # solution
        # # edge case : 이미 연결리스트가 비어있을 때
        # if self.head is None:
        #     return
        # # edge case : index = 0
        # if index == 0:
        #     self.head = self.head.next
        
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return
            prev = curr
            curr = curr.next

        # edge case : index == N
        if curr is None:
            return
        
        prev.next = curr.next


    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end=' ')
            curr = curr.next
        print()


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.print()

    for i in range(10):
        my_list.append(i + 1)

    my_list.print()

    for i in range(10):
        my_list.prepend(i + 1)

    my_list.print()

    value = my_list.access(3)
    print('my_list.access(3) = ' + str(value))

    my_list.insert(8, 128)
    my_list.print()

    my_list.remove(0)
    my_list.print()

    my_list.set_head(10)
    my_list.print()
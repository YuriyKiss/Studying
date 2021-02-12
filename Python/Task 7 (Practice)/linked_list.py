class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.__count = 0

    def __str__(self):
        text = "["
        temp = self.head
        while temp:
            if text != "[":
                text += ", "
            text += str(temp.data)
            temp = temp.next
        text += "]"
        return text

    def __len__(self):
        if self.head is None:
            self.__count = 0
        return self.__count

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def peek(self):
        if self.head is not None:
            return self.head.data

    def insert(self, index, data):
        if index == 0:
            self.__count += 1
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        i = 0
        n = self.head
        while i < index - 1 and n is not None:
            n = n.next
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            self.__count += 1
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def append(self, data):
        self.__count += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def remove(self, pos):
        if self.head is None:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            self.__count -= 1
            return

        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        for_next = temp.next.next
        temp.next = None
        temp.next = for_next

        self.__count -= 1

    def change(self, key, new):
        curr = self.head

        while curr is not None:
            if curr.data == key:
                curr.data = new

            curr = curr.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

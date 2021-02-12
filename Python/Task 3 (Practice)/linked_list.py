class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.__count = 0

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                index += len(self)

            i, temp = 0, self.head
            while temp is not None:
                if i == index:
                    return temp.data
                temp = temp.next
                i += 1
            raise IndexError(f'{type(self).__name__} index {index} out of range(0, {len(self)})')
        else:
            raise ValueError(f'Linked list cannot be indexed with values of type {type(index)}')

    def __setitem__(self, index, new_data):
        if isinstance(index, int):
            if index < 0:
                index += len(self)

            i, temp = 0, self.head
            while temp is not None:
                if i == index:
                    temp.data = new_data
                    return
                temp = temp.next
                i += 1
            raise IndexError(f'{type(self).__name__} index {index} out of range(0, {len(self)})')
        else:
            raise ValueError(f'Linked list cannot be indexed with values of type {type(index)}')

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

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print(self):
        text = "["
        temp = self.head
        while temp:
            if text != "[":
                text += ", "
            text += str(temp.data)
            temp = temp.next
        text += "]"
        print(text)

    def pop(self):
        if self.is_empty():
            return None

        else:
            element = self.head
            self.head = self.head.next
            element.next = None
            return element.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def clear(self):
        for i in range(len(self)):
            self.pop()

    def __len__(self):
        return self.__count

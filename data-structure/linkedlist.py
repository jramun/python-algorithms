class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value

    def set_value(self, value):
        self.value = value


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, value):
        new = Node(value)
        new.set_next(self.head)
        self.head = new
        self.size += 1

    def get(self, value):
        item = self.head
        while item is not None:
            if item.get_value() == value:
                return item
            else:
                item = item.get_next()
        return None

    def delete(self, index):
        if index > self.size:
            return
        if self.head is None:
            return
        else:
            counter = 0
            node = self.head
            while counter < index - 1:
                node = node.get_next()
                counter += 1
            node.set_next(node.get_next().get_next())
            self.size -= 1

    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.get_value())
            temp = temp.get_next()

    def get_size(self):
        return self.size


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert(1)
    linkedList.insert(10)
    linkedList.insert(5)
    linkedList.insert(6)
    linkedList.insert(8)
    linkedList.insert(55)
    linkedList.show()

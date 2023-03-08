from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    value: T = None
    next: Node[T] = None
    previous: Node[T] = None

    def __init__(self, value: T, next: Node[T], previous: Node[T]) -> None:
        super().__init__()
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList(Generic[T]):
    __head: Node[T] = None
    __end: Node[T] = None
    __size: int = 0

    def insert_front(self, item: T) -> None:
        new_head = Node[T](
            value=item, next=self.__head, previous=None
        )
        if self.__head is not None:
            self.__head.previous = new_head
        self.__head = new_head

        if self.__end is None:
            self.__end = self.__head
        self.__size += 1

    def insert_back(self, item: T) -> None:
        new_end = Node[T](
            value=item, next=None, previous=self.__end
        )
        if self.__end is not None:
            self.__end.next = new_end
        self.__end = new_end

        if self.__head is None:
            self.__head = self.__end
        self.__size += 1

    def get(self, index: int) -> T:
        return self.__get(index).value

    def __get(self, index: int) -> Node[T]:
        self.__assert_index(index)
        if index > self.__size // 2:
            return self.__get_from_end(index)
        else:
            return self.__get_from_head(index)

    def __get_from_head(self, index: int) -> Node[T]:
        current_node = self.__head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __get_from_end(self, index: int) -> Node[T]:
        current_node = self.__end
        for i in range(self.__size - index - 1):
            current_node = current_node.previous
        return current_node

    def remove(self, index: int) -> None:
        self.__assert_index(index)
        if index == 0:
            self.remove_front()
        elif index == self.__size - 1:
            self.remove_back()
        else:
            for_remove = self.__get(index)
            for_remove.previous.next = for_remove.next
            for_remove.next.previous = for_remove.previous
            self.__size -= 1

    def remove_front(self) -> None:
        if self.__size == 1:
            self.clear()
            return
        if self.__head.next is not None:
            self.__head.next.previous = None
        self.__head = self.__head.next
        self.__size -= 1

    def remove_back(self) -> None:
        if self.__size == 1:
            self.clear()
            return
        if self.__end.previous is not None:
            self.__end.previous.next = None
        self.__end = self.__end.previous
        self.__size -= 1

    def back(self) -> T:
        if self.__end is None:
            raise IndexError('Out of bounds')
        return self.__end.value

    def front(self) -> T:
        if self.__head is None:
            raise IndexError('Out of bounds')
        return self.__head.value

    def clear(self) -> None:
        self.__head = None
        self.__end = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def __assert_index(self, index: int) -> None:
        if not (0 <= index < self.__size):
            raise IndexError('Out of bounds')


class Dequeue(Generic[T]):
    __linked_list = DoublyLinkedList[int]()

    def push_back(self, item: T) -> None:
        self.__linked_list.insert_back(item)

    def push_front(self, item: T) -> None:
        self.__linked_list.insert_front(item)

    def pop_back(self) -> T:
        back = self.back()
        self.__linked_list.remove_back()
        return back

    def pop_front(self) -> T:
        front = self.front()
        self.__linked_list.remove_front()
        return front

    def back(self) -> T:
        return self.__linked_list.back()

    def front(self) -> T:
        return self.__linked_list.front()

    def size(self) -> int:
        return self.__linked_list.size()

    def clear(self) -> None:
        self.__linked_list.clear()


dequeue = Dequeue[int]()
while True:
    command = input()
    if command.startswith('push_front'):
        item = int(command.split()[1])
        dequeue.push_front(item)
        print('ok')

    elif command.startswith('push_back'):
        item = int(command.split()[1])
        dequeue.push_back(item)
        print('ok')

    elif command == 'pop_front':
        try:
            print(dequeue.pop_front())
        except IndexError:
            print('error')

    elif command == 'pop_back':
        try:
            print(dequeue.pop_back())
        except IndexError:
            print('error')

    elif command == 'front':
        try:
            print(dequeue.front())
        except IndexError:
            print('error')

    elif command == 'back':
        try:
            print(dequeue.back())
        except IndexError:
            print('error')

    elif command == 'size':
        print(dequeue.size())

    elif command == 'clear':
        dequeue.clear()
        print('ok')

    elif command == 'exit':
        print('bye')
        break

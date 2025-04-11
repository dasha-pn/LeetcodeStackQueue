"""Exercise 1"""

class Node:
    """
    A node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node.
    """
    def __init__(self, data, next):
        """
        Initialize a node with data and a pointer to the next node.

        >>> node = Node(5, None)
        >>> node.data
        5
        >>> node.next is None
        True
        """
        self.data = data
        self.next = next


class Stack:
    """
    A stack implemented using a singly linked list.
    """
    def __init__(self):
        """
        Create an empty stack.

        >>> s = Stack()
        >>> s.is_empty()
        True
        """
        self._items = None

    def is_empty(self):
        """
        Check if the stack is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push(10)
        >>> s.is_empty()
        False
        """
        return self._items is None

    def push(self, value):
        """
        Push a value onto the top of the stack.

        >>> s = Stack()
        >>> s.push(1)
        >>> s.peek
        1
        """
        self._items = Node(value, self._items)

    def pop(self):
        """
        Pop and return the value from the top of the stack.

        >>> s = Stack()
        >>> s.push(5)
        >>> s.push(10)
        >>> s.pop()
        10
        >>> s.pop()
        5
        >>> s.pop()
        Traceback (most recent call last):
            ...
        ValueError: Stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty.")
        temp = self._items.data
        self._items = self._items.next
        return temp

    @property
    def peek(self):
        """
        Return the value at the top of the stack without removing it.

        >>> s = Stack()
        >>> s.push(7)
        >>> s.peek
        7
        >>> s.pop()
        7
        >>> s.peek
        Traceback (most recent call last):
            ...
        ValueError: Stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty.")
        return self._items.data


class MyQueue:
    """
    A queue implemented using two stacks.
    """
    def __init__(self):
        """
        Create an empty queue.

        >>> q = MyQueue()
        >>> q.empty()
        True
        """
        self.out = Stack()
        self.inn = Stack()

    def push(self, el):
        """
        Push an element to the end of the queue.

        >>> q = MyQueue()
        >>> q.push(1)
        >>> q.push(2)
        >>> q.peek()
        1
        """
        self.inn.push(el)

    def pop(self):
        """
        Remove and return the element from the front of the queue.

        >>> q = MyQueue()
        >>> q.push(1)
        >>> q.push(2)
        >>> q.pop()
        1
        >>> q.pop()
        2
        """
        if self.empty():
            raise ValueError("Queue is empty.")
        if self.out.is_empty():
            while not self.inn.is_empty():
                self.out.push(self.inn.pop())
        return self.out.pop()

    def peek(self):
        """
        Return the element at the front of the queue without removing it.

        >>> q = MyQueue()
        >>> q.push(3)
        >>> q.push(4)
        >>> q.peek()
        3
        >>> q.pop()
        3
        >>> q.peek()
        4
        """
        if self.empty():
            raise ValueError("Queue is empty.")
        if self.out.is_empty():
            while not self.inn.is_empty():
                self.out.push(self.inn.pop())
        return self.out.peek

    def empty(self):
        """
        Check if the queue is empty.

        >>> q = MyQueue()
        >>> q.empty()
        True
        >>> q.push(1)
        >>> q.empty()
        False
        """
        return self.inn.is_empty() and self.out.is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

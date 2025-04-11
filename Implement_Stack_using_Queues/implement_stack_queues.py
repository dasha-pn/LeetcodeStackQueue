"""Exercise 2"""

class Queue:
    """
    A simple queue implementation using a Python list.

    Methods:
        enqueue(x): Adds an element to the back of the queue.
        dequeue(): Removes and returns the element from the front.
        front(): Returns the front element without removing it.
        is_empty(): Returns True if the queue is empty.
        size(): Returns the number of elements in the queue.
    """

    def __init__(self):
        """
        Initialize an empty queue.

        >>> q = Queue()
        >>> q.is_empty()
        True
        """

        self.data = []

    def is_empty(self):
        """
        Check whether the queue is empty.

        >>> q = Queue()
        >>> q.is_empty()
        True
        """

        if self.data:
            return False
        return True

    def add(self, value):
        """
        Add an element to the back of the queue.

        >>> q = Queue()
        >>> q.add(10)
        >>> q.peek()
        10
        """

        self.data.append(value)

    def peek(self):
        """
        Return the front element without removing it.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.peek()
        5
        >>> q.pop()
        5
        """

        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self.data[0]

    def pop(self):
        """
        Remove and return the element from the front of the queue.

        >>> q = Queue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.pop()
        1
        >>> q.pop()
        2
        """

        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self.data.pop(0)

class MyStack:
    """
    Stack implemented using two queues.

    Methods:
        push(x): Pushes an element onto the stack.
        pop(): Removes and returns the element on the top.
        top(): Returns the top element without removing it.
        empty(): Checks whether the stack is empty.
    """

    def __init__(self):
        """
        Initialize the stack with two empty queues.

        >>> s = MyStack()
        >>> s.empty()
        True
        """

        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        """
        Push element x onto the stack.

        >>> s = MyStack()
        >>> s.push(10)
        >>> s.peek()
        10
        """

        self.q2.add(value)
        while not self.q1.is_empty():
            self.q2.add(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def peek(self):
        """
        Return the top element without removing it.

        >>> s = MyStack()
        >>> s.push(3)
        >>> s.peek()
        3
        >>> s.pop()
        3
        >>> s.peek()
        Traceback (most recent call last):
            ...
        IndexError: Stack is empty.
        """

        if self.q1.is_empty():
            raise IndexError("Stack is empty.")
        return self.q1.peek()

    def pop(self):
        """
        Remove and return the top element of the stack.

        >>> s = MyStack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s.pop()
        Traceback (most recent call last):
            ...
        IndexError: Stack is empty.
        """

        if self.q1.is_empty():
            raise IndexError("Stack is empty.")
        return self.q1.pop()

    def empty(self):
        """
        Return True if the stack is empty.

        >>> s = MyStack()
        >>> s.empty()
        True
        >>> s.push(1)
        >>> s.empty()
        False
        """

        return self.q1.is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

"""Exercise 3"""

from collections import defaultdict

class FreqStack:
    """
    A stack-like data structure that pops the most frequent element.
    If there's a tie, pops the most recently added of the most frequent elements.

    >>> fs = FreqStack()
    >>> fs.push(5)
    >>> fs.push(7)
    >>> fs.push(5)
    >>> fs.push(7)
    >>> fs.push(4)
    >>> fs.push(5)
    >>> fs.pop()
    5
    >>> fs.pop()
    7
    >>> fs.pop()
    5
    >>> fs.pop()
    4
    """

    def __init__(self):
        """
        Initialize the frequency stack.
        """

        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        """
        Push an integer onto the frequency stack.

        :type val: int
        :rtype: None

        >>> fs = FreqStack()
        >>> fs.push(10)
        >>> fs.pop()
        10
        """

        f = self.freq[val] + 1
        self.freq[val] = f
        self.group[f].append(val)
        if f > self.max_freq:
            self.max_freq = f

    def pop(self):
        """
        Pop and return the most frequent element.
        If a tie, pop the most recently pushed among the most frequent.

        :rtype: int
        """

        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

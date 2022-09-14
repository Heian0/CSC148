from queue import Queue

def removeEven(q: Queue) -> None:

    """
    Modify q to remove any elements that are even.
    Do NOT return a new queue. Modify the one that is given.
    Precondition: Each item in q is an int.
    >>> q = Queue()
    >>> q.enqueue(10)
    >>> q.enqueue(3)
    >>> q.enqueue(2)
    >>> q.enqueue(9)
    >>> q.enqueue(5)
    >>> remove_even(q)
    >>> q.dequeue()
    3
    >>> q.dequeue()
    9
    >>> q.dequeue()
    5
    >>> q.is_empty()
    True
    """

    q2 = Queue()
    while not q.empty():
        item = q.get()
        if item % 2 != 0:
            q2.put(item)

    while not q2.empty():
        q.put(q2.get())

if __name__ == "__main__":

    q = Queue()
    q.put(10)
    q.put(3)
    q.put(2)
    q.put(9)
    q.put(5)
    removeEven(q)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.empty())

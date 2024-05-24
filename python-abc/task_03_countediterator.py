# task_03_countediterator.py

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Get the next item from the original iterator
        item = next(self.iterator)
        self.counter += 1  # Increment the counter
        return item

    def get_count(self):
        return self.counter

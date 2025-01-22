class ReverseRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = end
    
    def __iter__(self):
        # Return the iterator object itself
        return self
    
    def __next__(self):
        if self.current <= self.start:
            raise StopIteration  
        self.current -= 1
        return self.current 

my_range = ReverseRange(1, 5)

for number in my_range:
    print(number)
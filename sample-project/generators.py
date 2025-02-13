def count_up_to(limit):
    """ 
    A generator that yields numbers from 1 up to the specified limit.
    Parameters:
    limit (int): The upper bound of the counting sequence.

    """
    count = 1
    while count <= limit:
        yield count  
        count += 1

counter = count_up_to(5)

for number in counter:
    print(number)

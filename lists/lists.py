import time

# traversing a list

def multiply(numbers: list, multiple: int) -> list[int]:
    start = time.time()
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * multiple
    end = time.time()
    total_time = end-start
    print(total_time)
    return numbers

def multiply_comp(numbers: list, multiple:int) -> list[int]:
    start = time.time()
    result = [i*multiple for i in numbers]
    end = time.time()
    total_time = end - start
    print(total_time)
    return result

def add_up_all(t: list[int]) -> int:
    """ adds up all the elements in a given list

    Args:
        t (list): a list of integers

    Returns:
        int: The total of the integers given in the list
    """
    total = 0
    for item in t:
        total += item
    return total

def capitalize_all_t(t:list[str]) -> list[str]:
    """ traversing a list of strings while
    building another list

    Args:
        t (str): list of originan strings

    Returns:
        list[str]: _description_
    """
    
    result: list = []
    for i in t:
        for s in i:
            result.append(s.capitalize())
    return result

def only_upper(t: list[str]) -> list[str]:
    """
    A function that traverses a list and returns a 
    sublist from the list

    Args:
        t (str): _description_

    Returns:
        list[str]: _description_
    """
    res = []
    for s in t:
        if s.isupper():
           res.append(s)
    return res


def nested_sum(t: list[list[int]]) -> int:
    count = 0
    for item in t:
        for i in item:
            count += i

    return count

def cumsum(t:list[int]) -> list[int]:
    """function that returns the cummulative sum of items in a list

    Args:
        t (list[int]): a list of integers

    Returns:
        list[int]: the cummulative sum of the integers given in the list

    Example:    
        cumsum([1, 2, 3, 4, 5]) -> [1, 3, 6, 10, 15]
        
    """
    total = 0
    result = []
    for item in t:
        total += int(item)
        result.append(total)
    return result

def middle(t:list[int]) -> list[int]:
    """ function that takes a list and returns the mid points of the list

    Args:
        t (list[int]): a list of integers

    Returns:
        list[int]: returns a list of midpoints of the original list
    """
    mid_point = len(t)//2
    first_half = t[:mid_point]
    second_half = t[mid_point:]
    result = [first_half[-1], second_half[0]]
    return result


def chop(t:list[int]) -> None:
    """a function that modifies the given list but returns None

    Args:
        t (list[int]): a list of integers

    Example:
        >>> t = [1,2,3,4]
        >>> chop(t)
        >>> t
        ... [2,3]
    """
    del t[0]
    del t[-1]
        


if __name__ == "__main__":
    array = list(range(1, 11))
    string = ['my name is chief']
    t = [[1, 2], [3], [4, 5, 6]]
    t2 = [1, 2, 3, 4, 5, 6, 7,8,9,10, 11, 12]
    # multiply(array, 2)
    print(chop(t2))
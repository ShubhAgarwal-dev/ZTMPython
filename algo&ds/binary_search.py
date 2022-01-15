def binary_search(array: list, item):
    """
    Can be used to find anything in the array much faster than simple search
    but the array provided must be sorted
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 7, 9, 51]
    print(binary_search(my_list, 9))
    print(binary_search(my_list, 3))
    print(binary_search(my_list, 4))
    print(binary_search(my_list, -1))
    print(binary_search(my_list, 51))
    print(binary_search(my_list, 8))

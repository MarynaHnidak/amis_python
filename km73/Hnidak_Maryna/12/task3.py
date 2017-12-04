def groups(list, iterator):
    """
    This function is the largest group
    Args:
        list: list, input parameter
        iterator: integer, index
    Returns:
        max(a): integer, result of the program
    Raises:
        ValueError, OverflowError, ZeroDivisionError
    Examples:
        >>> print([1,1,1,2,2,1,3,3,3,4,],0)
        "3"
    :param list:
    :param iterator:
    :return:
    """
    if iterator == len(list):
        return max(a)
    list_two = "".join(list)
    count_of_element = list.count(list[iterator])
    if (count_of_element - iterator)*str(list[iterator]) in list:
        a.append(count_of_element - iterator)
    return groups(list, iterator + 1)


a = []
list = input("Enter list : ").split()
print(groups(list, 0))

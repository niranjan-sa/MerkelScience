"""
Created on Tue May 14 20:36:50 2019

@author: niranjan_agnihotri
"""

test1 = [1, 2, 3]
test2 = [1, 3, 6, 4, 1, 2]
test3 = [-1, -3]


def positive_elem(numbers):
    """
    Initialize the variables and find the solution. This solution is based on a recursive approach.
    (As mentioned in the guidelines, looping is not used. Hashing data structures provide an amortized O(1)
    search time for the keys.
    Time complexity O(n)
    Space complexity O(n)
    :param numbers:
    :return: Least positive integer.
    """
    n = len(numbers)
    keys = list(range(1, n+1))
    hl = {}
    hl = hl.fromkeys(keys, False)
    set_keys(numbers, hl, ix=0)
    return search(hl, keys, ix=0)


def search(hl, keys, ix):
    """
    Search for the smallest positive element.
    :param hl:
    :param keys:
    :param ix:
    :return: Least positive integer.
    """
    if ix == len(keys):
        return ix+1

    if hl[keys[ix]] is False:
        return ix+1
    else:
        return search(hl, keys, ix+1)


def set_keys(numbers, hl, ix):
    """
    Initialize the hash set.
    :param numbers:
    :param hl:
    :param ix:
    :return: Updated hash set.
    """
    if ix == len(numbers):
        return hl
    if hl.has_key(numbers[ix]):
        hl[numbers[ix]] = True

    set_keys(numbers, hl, ix+1)


def main():
    """
    Driver function
    :return: None
    """
    print(positive_elem(test1))
    print(positive_elem(test2))
    print(positive_elem(test3))


if __name__ == '__main__':
    main()




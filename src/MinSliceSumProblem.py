"""
Created on Tue May 15 18:31:50 2019

@author: niranjan_agnihotri
"""


def min_sum(numbers):
    """
    This function returns minimum absolute sum. This is a trivial brute force approach with an O(n^2) time complexity.
    :param numbers:
    :return: Minimum absolute sum
    """

    if len(numbers) == 0:
        return  0

    if len(numbers) == 1:
        return numbers[0]

    i = 0
    sums = []
    while i < len(numbers):
        sums.append(abs(numbers[i]))
        j = i+1
        while j < (len(numbers)):
            sums.append(abs(sum(numbers[i:j+1])))
            j += 1
        i += 1

    return min(sums)


def min_sum_efficient(numbers):
    """
    Cumulative sum approach. Time complexity O(n*logn). O(n) Auxiliary space required.
    :param numbers:
    :return: Minimum absolute sum
    """
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    cumsum = [0]
    i = 1
    while i <= len(numbers):
        cumsum.append(cumsum[i-1]+numbers[i-1])
        i += 1

    cumsum.sort()
    cumsum_diff = []
    i = 1
    while i < len(cumsum):
        cumsum_diff.append(abs(cumsum[i] - cumsum[i-1]))
        i += 1
    return min(cumsum_diff)


def main():
    """
    Driver function.
    :return:
    """
    print (min_sum([2, -4, 6, -3, 9]))
    print (min_sum([2]))
    print (min_sum([2, 1]))
    print (min_sum([-1, -1, -10, 10]))
    print (min_sum([10, 10, 10, -30]))

    print (min_sum_efficient([2, -4, 6, -3, 9]))
    print (min_sum_efficient([2]))
    print (min_sum_efficient([2, 1]))
    print (min_sum_efficient([-1, -1, -10, 10]))
    print (min_sum_efficient([10, 10, 10, -30]))


if __name__ == '__main__':
    main()
def array_sum(a, target):
    """"
    sub array with sum = target in O(N)
    """
    elements = {}
    for i, item in enumerate(a):
        if item not in elements:
            elements[item] = i
        if target - item in elements:
            return [elements[item], elements[target - item]]

    return -1


def zero_sum(a):
    """"
    subarray with zero sum exists or not, print sub_array
    """
    dict_map = {}
    sum = 0

    for i, item in enumerate(a):
        sum += item
        if sum == 0:
            return [0, i]
        if item == 0:
            return [i]
        if sum in dict_map:
            return [dict_map[sum] + 1, i]
        if sum not in dict_map:
            dict_map[sum] = i
    return -1


def max_count_zero_one(a):
    """"# Python 3 program to find largest
    # subarray with equal number of
    # 0's and 1's.
        """
    sum_dict = {}
    end = -1
    sum1 = 0
    max_len = 0
    for i, item in enumerate(a):
        if item == 0:
            a[i] = -1
        sum1 += a[i]
        if sum1 == 0:
            if max_len < i + 1:
                max_len = i + 1
                end = i
        if sum1 in sum_dict:
            if max_len < i - sum_dict[sum1]:
                max_len = i - sum_dict[sum1]
                end = i
        if sum1 not in sum_dict:
            sum_dict[sum1] = i
    return max_len, end


def second_min(a):
    """
    second min in o(n) of unsorted array
    :param a:
    :return:
    """
    min1 = max(a)
    min2 = max(a)
    for item in a:
        if item < min1:
            min2 = min1
            min1 = item
            print(min1, min2)
        elif item < min2 and item > min1:
            min2 = item
    return min2


def subarray1(a):
    """
    check if subarray with zero sum exists or not
    :param a:
    :return:
    """
    if not a:
        return "doesnt exist"
    sum_list = 0
    dict1 = {}
    for i, item in enumerate(a):
        sum_list += item
        if sum_list not in dict1:
            dict1[sum_list] = i
        else:
            return "exists at: " + str(dict1[sum_list] + 1) + " " + str(i)

    return "doesnt exist"


def sort_zero_ones_linear_time(a):
    i = 0
    j = 0
    while i < len(a):
        if a[i] == 0:
            a[j] = 0
            j += 1
        i += 1
    while j < len(a):
        a[j] = 1
        j += 1
    print(a)


def kadane_Algorithm(a):
    """"find maximum sub array sum
    """
    max_so_far = 0
    max_ending_here = 0
    for item in a:
        max_ending_here += item

        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far,max_ending_here)

    return max_so_far


def circular_array_max_sum(a):
    a = [-item for item in a]
    neg_max = kadane_Algorithm(a)
    a = [-item for item in a]
    return max(kadane_Algorithm(a), sum(a) + neg_max)


def min_sum_subarray_k_Size(a, k):
    """"sliding  window
    """
    n = len(a)
    if n < k:
        return -1
    res = 0
    for i in range(0, k):
        res += a[i]
    curr_Sum = res
    j = k
    for j in range(k, n):
        curr_Sum += a[j] - a[j - k]
        res = min(res, curr_Sum)

    return res


def sum_subarray(a, n):
    """"longest subarray having given sum   --------sliding window---o(n)------------
    """

    start = 0
    max_len = -1
    sum1 = 0
    start_index = -1
    for i, item in enumerate(a):
        sum1 += item
        while sum1 > n:
            sum1 -= a[start]
            print("here1", sum1)
            start += 1
        if sum1 == n:
            if max_len < i - start + 1:
                max_len = i - start + 1
                start_index = start
    return max_len, a[start_index: start_index + max_len]


def equilibrium_index(a):
    """"beautiful o(n) solution
    """
    totalsum = sum(a)
    leftsum = 0
    for i, item in enumerate(a):
        totalsum -= item

        if leftsum == totalsum:
            return i

        leftsum += item






if __name__ == "__main__":
    s = "fdca"
    print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))
    pass

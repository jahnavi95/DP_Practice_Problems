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







if __name__ == "__main__":
    s = "fdca"
    print(longest_alphabetic_substring(s))
    pass

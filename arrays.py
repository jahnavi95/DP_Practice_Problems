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

if __name__ == "__main__":
    s = "fdca"
    print(sort_zero_ones_linear_time([1, 1, 0, 0,1,0,1,1]))
    pass

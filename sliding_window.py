def substring1(s, k):
    """"Find the longest substring with k unique characters in a given string -------beautyfully done in o(n)
    """

    end = 0
    begin = 0
    low = 0
    high = 0
    window = set()
    freq = [0] * 26
    while high < len(s):
        freq[ord(s[high]) - ord('s')] += 1
        window.add(s[high])

        while len(window) > k:
            freq[ord(s[low]) - ord('s')] -= 1
            if freq[ord(s[low]) - ord('s')] == 0:
                window.remove(s[low])

            low += 1

        if end - begin < high - low:
            end = high
            begin = low

        high += 1

    return s[begin:end + 1]

def substring2(s):
    """" longest substring without repeating characters ????????????????
    """
    start = 0
    dict1 = {}
    for i, item in enumerate(s):

        if item in s:
            start = max(start,dict1[item])

        dict1[item] = i



    pass

def important():
    """"Subarrays with distinct elements
    """


def check_string_validity(s):
    if type(s) == str and s and s != "":
        return True
    return False


def check_rotation(s1, s2):
    if check_string_validity(s1) and check_string_validity(s2):
        if len(s1) == len(s2):
            s3 = s1 + s1
            if s2 in s3 and s1 in s3:
                return "rotation of each other"
            return "not rotation of each other"
        return "Strings not of equal length!!"
    return "String not in proper format"


def last_index(s, c):
    if check_string_validity(s):
        index = -1
        for i, item in enumerate(s):
            if item == c:
                index = i
        return index
    return "string not in proper format"


if __name__ == "__main__":
    print(last_index("abbcb", "g"))
    pass

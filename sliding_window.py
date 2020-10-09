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

def substring2():
    """" longest substring without repeating characters ????????????????
    """
    pass

def important():
    """"Subarrays with distinct elements
    """





if __name__ == "__main__":
    print(substring1("aabacbebebe", 3))
    pass

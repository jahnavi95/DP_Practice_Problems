from collections import deque


def longest_alphabetic_substring(s):
    """" longest ascending substring o(n2)
    wrong logic doesnnt work for efyzabc
    """
    max_len = 0
    index1 = -1
    end = 0
    for i, item in enumerate(s):
        end = i
        while end < len(s) - 1 and s[end] < s[end + 1]:
            end += 1

        if end - i + 1 > max_len:
            max_len = end - i + 1
            index1 = end
    return index1, max_len

#
# def sliding_window1(s):
#     end_index = -1
#     max_len = 0
#     i = 0
#     while i < len(s):
#




def expand(str1, low, high, s):
    while low >= 0 and high < len(str1) and str1[low] == str1[high]:
        print(low, high)
        s.add(str1[low:high + 1])
        low = low - 1
        high = high + 1


def all_palindromic_substring(str1):
    s = set()
    for i in range(len(str1)):
        # find all odd length palindrome with str[i] as mid point
        print(i)
        expand(str1, i, i, s)
        # find all even length palindrome with str[i] and str[i+1]
        # as its mid points
        expand(str1, i, i + 1, s)
    return s


def map_pattern_word(pat, words):
    """"
    print all words in a list which is in a similar pattern to pat(same order of characters)
    """
    final_list = []
    for word in words:
        print(word)
        if len(word) == len(pat):
            i = 0
            dict1 = {}
            dict2 = {}
            while i < len(pat):
                if pat[i] not in dict1:
                    dict1[pat[i]] = word[i]
                else:
                    if dict1[pat[i]] != word[i]:
                        break
                if word[i] not in dict2:
                    dict2[word[i]] = pat[i]
                else:
                    if dict2[word[i]] != pat[i]:
                        break

                i += 1
            if i == len(pat):
                final_list.append(word)
    if final_list:
        return final_list
    return -1


def min_operations_to_transform_to_another_string(s1, s2):
    pass


def run_length_encoding(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
            i = i + 1
        encoding += str(count) + s[i]

        i += 1

    return encoding


def isVowel(c):
    return (c == 'a' or c == 'A' or c == 'e' or
            c == 'E' or c == 'i' or c == 'I' or
            c == 'o' or c == 'O' or c == 'u' or
            c == 'U')


def reverseVowel(str):
    """"?????????????????????????????????????????????
    """
    # Start two indexes from two corners
    # and move toward each other
    i = 0
    j = len(str) - 1
    while (i < j):
        if not isVowel(str[i]):
            i += 1
            continue
        if (not isVowel(str[j])):
            j -= 1
            continue

        # swapping
        str[i], str[j] = str[j], str[i]
        i += 1
        j -= 1
    return str


def longest_bal_parenthesis_len(s):
    """"????????????????????????????????????????????????
    """
    sum1 = 0
    max1 = 0
    for i, item in enumerate(s):
        if item == "(":
            sum1 += 1
        else:
            sum1 -= 1
        if sum1 < 0:
            break

        if sum1 == 0:
            max1 = i + 1

    return max1


def inplace_remove(s):
    """"in place remove all occurences of AB and C
    """
    k = 0
    i = 0
    l = list(s)
    c = []
    while i < len(l):
        if l[i] == "A" and l[i + 1] == "B":
            print(l[i])
            i = i + 2
        elif l[i] == "C":
            print(l[i])
            i = i + 1
        else:
            print("56", k, l[i])
            c.append(l[i])
            print("1", c[k], l[i])
            k += 1
            i += 1
    l = "".join(c)
    return l


def expand2(s, max1, low, high):
    sum_l = int(s[low])
    sum_r = int(s[high])
    while low >= 0 and high < len(s):
        if sum_r == sum_l:
            max1 = max(max1, high - low + 1)
        low -= 1
        high += 1
        if high < len(s):
            sum_r += int(s[high])
        if low >= 0:
            sum_l += int(s[low])
        if sum_r == sum_l:
            max1 = max(max1, high - low + 1)
        print(low, high)
        print(sum_l, sum_r)

        print(max1, "max")


def longest_pal_sum_substring(s):
    """"
    ???????????????????????????????????????
    """
    max1 = 0
    s1 = list
    for i in range(len(s) - 1):
        print("in func", i)
        expand2(s, max1, i, i + 1)

    return max1


def longest_substring_k_char(s, k):
    """" Return longest substring containing k distinct chars in  o(n2)
    """
    ending_index = -1
    max1 = -1
    for i, item in enumerate(s):
        dict1 = {}
        j = i
        while j < len(s):
            if s[j] not in dict1:
                dict1[s[j]] = 1
            else:
                dict1[s[j]] += 1
            if len(list(dict1.values())) == k:
                if j - i + 1 > max1:
                    max1 = j - i + 1
                    ending_index = j
            elif len(list(dict1.values())) > k:
                break
            j += 1
    return [ending_index, ending_index - max1 + 1], max1


def is_valid(a):
    val = 0
    for item in a:
        if item != 0:
            val += 1
    return val


def longest_substring_k_char1(s, k):
    """" Return longest substring containing k distinct chars in  o(n)
    """

    start = 0
    count = [0] * 256
    max_len = 0
    end = -1
    for i, item in enumerate(s):

        count[ord(item)] += 1
        while is_valid(count) > k:
            count[ord(s[start])] -= 1
            start -= 1

        if i - start + 1 > max_len:
            max_len = i - start + 1
            end = i

    return s[end - max_len: end + 1]


def window(s, pat):
    """"????// Find the smallest window in a string containing all characters of another string
    """
    pat_list = [0] * 256
    s_list = [0] * 256
    count = 0
    start = 0
    min_len = len(s)
    for item in pat:
        pat_list[ord(item)] += 1
    for i, item in enumerate(s):
        s_list[ord(item)] += 1

        if pat_list[ord(item)] != 0 and [ord(item)] <= pat_list[ord(item)]:
            count += 1
        if count == len(pat):
            while s_list[ord(s[start])] > pat_list[ord(s[start])] or pat_list[ord(s[start])] == 0:
                if s_list[ord(s[start])] > pat_list[ord(s[start])]:
                    s_list[ord(s[start])] -= 1
                start += 1
            min_len = max(min_len, i - start + 1)

    # print("hihihihi",s[start:start+min_len])
    return


# Python3 program to find the smallest window
# containing all characters of a pattern.
no_of_chars = 256


def code(s, pat):
    """" above question with O(N2)
    """
    pat_list = [0] * 256

    min_len = len(s)
    end = 0
    for item in pat:
        pat_list[ord(item)] += 1
    for i in range(len(s)):
        count = 0
        s_list = [0] * 256
        for j in range(i, len(s)):
            print(s[i:j + 1])
            s_list[ord(s[j])] += 1
            if pat_list[ord(s[j])] != 0 and s_list[ord(s[j])] <= pat_list[ord(s[j])]:
                count += 1
            if count == len(pat):
                end = j
                print("end", end, i)
                break
        print("len", end - i + 1)
        if count == len(pat) and min_len > end - i + 1:
            min_len = end - i + 1
            start = end - min_len + 1
            print("hi", min_len)
    return s[start:start + min_len]


def find_substring(s):
    """"Smallest window that contains all characters of string
    sliding window o(n)
    """
    count = 0
    start = 0
    start_index = 0
    min_len = len(s)
    dis = len(set(s))
    list_s = [0] * 256
    for i, item in enumerate(s):
        list_s[ord(item)] += 1
        if list_s[ord(item)] == 1:
            count += 1
        if count == dis:
            while list_s[ord(s[start])] > 1:
                if list_s[ord(s[start])] > 1:
                    list_s[ord(s[start])] -= 1
                start += 1
            if min_len > i - start + 1:
                min_len = i - start + 1
                start_index = start
    print(start_index, min_len)
    return s[start_index: start_index + min_len]


def string1(s, k):
    """" ??????????????Count number of substrings with exactly k distinct characters
    """
    cnt = 0
    for i, item in enumerate(s):
        list_s = [0] * 256
        count = 0
        # print(i)
        for j in range(i, len(s)):

            # print(list_s)=
            if list_s[ord(s[j])] == 0:
                # print("!")
                count += 1
            list_s[ord(s[j])] += 1
            if count == k:
                # print("here")
                cnt += 1
                break
    return cnt


def first_non_repeating(s):
    dict1 = {}
    for item in s:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1

    for item in dict1:
        if dict1[item] == 1:
            return s.index(item)
    return -1


def string2(s1, s2, m, n):
    """"Given two strings, find if first string is a subsequence of second in linear time: recursive
    """
    # s1 is subsequence of s2
    # m = len(s1)
    # n = len(s2)

    if m == 0:
        return True
    if n == 0:
        return False
    if s1[m - 1] == s2[n - 1]:
        return string2(s1, s2, m - 1, n - 1)
    return string2(s1, s2, m, n - 1)


def string3(s, k):
    """"??????????????/Find number of times a string occurs as a subsequence in given string
    """
    pass


def substring3(s, k):
    """"Number of substrings with count of each character as k
    """
    freq = [0] * 26
    # for i,item in enumerate(s):
    pass


def brackets_evaluation(a):
    """

    :param a: Identify and mark unmatched parenthesis in an expression
    :return:
    """
    s = deque()
    a1 = list(a)
    index = [None] * len(a1)
    for i, item in enumerate(a1):
        if item == "(":
            s.append(item)
            index.append(i)
        elif item == ")":
            if len(s) == 0:
                a1[i] = "-1"
            else:
                s.pop()
                j = index.pop()
                a1[j] = "0"
                a1[i] = "1"
        else:
            a1[i] = item

    final = "".join(a1)
    final = final.replace("(", "-1")
    return final


def inplace_removeAB_C(s):
    s = list(s)
    i = 0
    k = 0
    while i < len(s):
        if s[i] == 'B' and k > 0 and s[k - 1] == 'A':
            k -= 1
            i = i + 1
        elif s[i] == 'C':
            i += 1
        else:
            s[k] = s[i]
            k += 1
            i += 1

    return "".join(s[:k])


def encoding(str1):
    i = 0
    encode = ""
    while i < len(str1):
        count = 1
        while i < len(str1) - 1 and str1[i] == str1[i + 1]:
            count += 1
            i += 1

        encode += str(count) + str1[i]
        i = i + 1
    return encode


def construct_palindrome(s):
    palind = []
    dict1 = {}
    mid = ""
    for item in s:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1

    flag = False
    for item in dict1:
        if dict1[item] % 2 == 0:
            palind.extend([item] * (dict1[item] / 2))

        else:
            if not flag:
                if dict1[item] > 2:
                    palind.extend([item] * ((dict1[item] - 1) / 2))
                mid = [item]
            flag = True
    print(palind)
    return palind + mid + list(reversed(palind))


def remove_spaces(s):
    k = 0
    i = 0
    s = list(s)
    while i < len(s):
        if s[i] == " ":
            i += 1
        else:
            s[k] = s[i]
            k += 1
            i += 1
    print(s)
    return s[:k]


def remove_adjacent_dup(s):
    k = 0
    i = 0
    s = list(s)
    while i < len(s):
        if s[i] == s[i + 1]:
            i += 1
        else:
            s[k] = s[i]
            k += 1
            i += 1
    print(s)
    return s[:k]


def check_string_validity(s):
    if type(s) == str and s and s != "":
        return True
    return False


def check_palindrome(s):
    if check_string_validity(s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return "not palind"
        return "palind"
    return "string not in proper format"


def expand_string(s, low, high):
    while low >= 0 and high < len(s) and s[low] == s[high]:
        low = low - 1
        high = high + 1
    return s[low + 1:high]


def longest_palind(s):
    max_len = 0
    if check_string_validity(s):
        for i in range(len(s)):
            curr_str = expand_string(s, i, i)
            if len(curr_str) > max_len:
                max_len = curr_str
            curr_str = expand_string(s, i, i + 1)
            if len(curr_str) > max_len:
                max_len = curr_str

        return max_len
    else:
        return "string not in proper format"


def longest_distinct_substring(s):
    start = 0
    if check_string_validity(s):
        dict1 = {}
        max_len = 0
        max_str = ""
        for i, item in enumerate(s):
            if item in dict1:
                start = max(start, dict1[item] + 1)
            dict1[item] = i
            if max_len < i - start + 1:
                max_len = i - start + 1
                max_str = s[start:i + 1]

        return max_str
    else:
        return "not valid string"


def target_sum(a, k):
    if a:
        dict1 = {}
        for i, item in enumerate(a):
            if item not in dict1:
                dict1[item] = i
            if k - item in dict1:
                if i != dict1[k - item]:
                    return [i, dict1[k - item]]
        return "not present"
    else:
        return -1


def product_array(a):
    pass


def lcs(x, y):
    m = len(x)
    n = len(y)
    t = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if y[i - 1] == x[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[n][m]


def longest_plaindromic_subs(x):
    y = str(reversed(x))
    m = len(x)
    n = len(y)
    t = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if x[j - 1] == y[i - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[n][m]


def three_sum(a, k):
    a.sort()
    n = len(a)
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            if (a[l] + a[i] + a[r] == k):
                return [a[l], a[i], a[r]]

            elif a[l] + a[i] + a[r] < k:
                l += 1
            else:
                r -= 1


def stock_selling(a):
    def stockBuySell(price, n):

        # Prices must be given for at least two days
        if (n == 1):
            return

        # Traverse through given price array
        i = 0
        while (i < (n - 1)):

            # Find Local Minima
            # Note that the limit is (n-2) as we are
            # comparing present element to the next element
            while ((i < (n - 1)) and
                   (price[i + 1] <= price[i])):
                i += 1

            # If we reached the end, break
            # as no further solution possible
            if (i == n - 1):
                break

            # Store the index of minima
            buy = i
            i += 1

            # Find Local Maxima
            # Note that the limit is (n-1) as we are
            # comparing to previous element
            while ((i < n) and (price[i] >= price[i - 1])):
                i += 1

            # Store the index of maxima
            sell = i - 1

            print("Buy on day: ", buy, "\t",
                  "Sell on day: ", sell)


def four_sum(a, k):

    pass


if __name__ == "__main__":
    # print(encoding("ab4c12ed3", 4))
    s = "this is a test string"

    print(longest_distinct_substring("geeksforgeeks"))
    pass

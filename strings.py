def longest_alphabetic_substring(s):
    """" longest ascending substring
    """
    start_index = 0
    end_index = 0
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            end_index = i + 1
            print(s[i], s[i + 1])

        else:
            print(i)
            start_index = i + 1
    if end_index == 0:
        return -1
    return end_index - start_index + 1


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
    """" Return longest substring containing k distinct chars
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


if __name__ == "__main__":
    s = "aacbbcc"

    print(longest_substring_k_char(s, 4))
    pass

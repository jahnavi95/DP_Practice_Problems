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
    


if __name__ == "__main__":
    s = "fdcaacdsf"
    print(map_pattern_word("moon", ["leet", "code", "cool", "siis", "jha", "hihi"]))
    pass

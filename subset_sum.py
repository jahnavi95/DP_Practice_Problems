def subset_sum(a, sum):
    n = len(a)
    t = [[False for i in range(sum + 1)] for j in range(0,n+1)]
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, sum + 1):
        t[0][i] = False
    for i in range(n+1):
        for j in range(sum+1):
            if j >= a[i-1]:
                t[i][j] = t[i-i][j] or t[i-1][j-a[i-1]]
            else:
                t[i][j] = t[i-1][j]

    return t[i][j]




def common_characters(str1, str2):
    if isvalidinput(str1, str2):
        final_res = []
        str1_dict = char_count(str1)
        str2_dict = char_count(str2)
        for item in str1_dict:
            if item in str2_dict:
                min_count = min(str1_dict[item], str2_dict[item])
                final_res.extend([item] * min_count)
        common = "".join(final_res)
        if common:
            return common
        else:
            return "No common characters"
    else:
        return "Not valid input"


def isvalidinput(str1, str2):
    if type(str1) != str or type(str2) != str:
        return False
    elif str1 == "" or str2 == "":
        return False
    else:
        return True


def char_count(str1):
    str1_dict = dict()
    for item in str1:
        if item not in str1_dict:
            str1_dict[item] = 1
        else:
            str1_dict[item] += 1
    return str1_dict

if __name__ == "__main__":
    print(common_characters("nkjkjka","aabacc"))
    pass
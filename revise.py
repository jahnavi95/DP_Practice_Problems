
def substring1(s):
    dict1 = [0] * 256

    max_len = 0
    end = -1
    j = 0
    for i , item in enumerate(s):
        while j < len(s):
            dict1[ord(item)] +=1





from collections import deque


def N_G_R(a):
    """" NExt greater element to the right
    """
    stack = deque()
    i = len(a) - 1
    ngr = []
    while i >= 0:
        while stack:
            if a[i] < stack[-1]:
                ngr.append(stack[-1])
                break
            stack.pop()
        if not stack:
            ngr.append(-1)
        stack.append(a[i])
        i -= 1
    return list(reversed(ngr))


def stock_span(a):
    """" nearest greatest to left create ngl with indexes and get difference between list items and index
    """
    stack = deque()
    i = 0
    ngl = []
    while i < len(a):
        while stack:
            if a[i] < stack[-1]:
                ngl.append(a.index(stack[-1]))
                break
            stack.pop()
        if not stack:
            ngl.append(0)
        stack.append(a[i])
        i += 1
    print(ngl)
    res = []
    res.append(1)
    for i in range(1, len(a)):
        res.append(i - ngl[i])
    return res


def longest_balanced_parenthesis():
    s1 = deque()
    s1.append(-1)
    len1 = 0
    for i, item in enumerate(s):
        if item == "(":
            s1.append(i)
        else:
            s1.pop()
            if not s1:
                s1.append(i)
                continue

            if len1 < i - s1[-1]:
                len1 = i - s1[-1]

    return len1

    pass


def merge_overlapping_intervals(a):
    # TODO
    pass


def maximum_paren_depth(s):
    max1 = 0
    cur_max = 0
    for item in s:
        if item == "(":
            cur_max += 1
            if cur_max > max1:
                max1 = cur_max
        elif item == ")":
            if cur_max > 0:
                cur_max -=1
            else:
                return -1
    return max1


def duplicate_parenthesis_check(s1):
    """"check if string contains duplicate parenthesiis. if  a string contains dup when same xprsn surrounded by one than one parenthesis
    """
    s = deque()
    for item in s1:
        if item == ")":
            if s:
                count = 0
                top = s.pop()
                while top != "(":
                    count += 1
                    top = s.pop()
                if count < 1:
                    return True
        else:
            s.append(item)
    return False

# def smallest_window(s,t):

def array_rotate_by_one(a):
    temp = a[0]
    n = len(a)
    for i in range(n-1):
        a[i] = a[i + 1]

    a[n - 1] = temp

def rotate(a,d):
    for i in range(d):
        array_rotate_by_one(a)

    return a

def reversal(a):

    start = 0
    end = len(a)-1

    while start < end:
        a[start] , a[end] = a[end] , a[start]
        start += 1
        end -= 1
    return a

if __name__ == "__main__":
    s = [100, 80, 60, 70, 60, 75, 85]
    # s = "((a+b)+(c+d)) "
    print(reversal(s))
    pass

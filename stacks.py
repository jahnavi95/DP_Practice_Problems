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
    # TODO
    pass


def merge_overlapping_intervals(a):
    # TODO
    pass


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


if __name__ == "__main__":
    # s = [100, 80, 60, 70, 60, 75, 85]
    s = "((a+b)+(c+d)) "
    print(duplicate_parenthesis_check(s))
    pass

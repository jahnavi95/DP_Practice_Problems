def lcs():
    x = "abcdef"
    y= "abc"
    m = len(x)
    n = len(y)
    t = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]
    print(t)
    # for i in range(0,m+1):
    #     for j in range(0,n+1):
    #         if i==0 or j == 0:
    #             t[i][j] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    print("hihih",t)
    return t[n][m]


if __name__ == "__main__":
    print(lcs())

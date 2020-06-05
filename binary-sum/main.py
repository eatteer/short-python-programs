# This algorithm does not contain validations

import math

def binary_sum(a, b):
    l = []
    c = 0
    n = max(len(a), len(b))

    if len(a) == n:
        diff = len(a) - len(b)
        for i in range(diff):
            b.insert(0,0)
    else:
        diff = len(b) - len(a)
        for i in range(diff):
            a.insert(0,0)

    a = a[::-1]
    b = b[::-1]

    for j in range(n):
        d = math.floor((a[j] + b[j] + c) / 2)
        s = a[j] + b[j] + c - (2 * d)
        l.append(s)
        c = d
    s = c
    l.append(s)
    return l[::-1]

def main():

    a = [1,1,1,1,0,0,1]
    b = [1,1,1,1,0,0]
    c = binary_sum(a,b)

    print(a, " + ", b, " = ", c)


if __name__ == "__main__":
    main()

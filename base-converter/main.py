# This algorithm does not contain validations

def list_int(q):
    # int list to int
    return int("".join(map(str, q))) # int

def base10(q, b):
    r = 0
    j = len(q) - 1
    for i in q:
        r += i * pow(b, j)
        j -= 1
    return r # int

def base_b(q, ob, b):
    res = []
    if ob != 10: q = base10(q, ob)
    else: q = list_int(q)
    while(q != 0):
        a = int(q % b)
        q = int(q / b)
        res.append(a)
    return res[::-1] # return reversed list

def main():
    n = [5,8,1]
    ob = 10
    b = 3
    print(base_b(n, ob, b))


if __name__ == "__main__":
    main()

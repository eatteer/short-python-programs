# This algorithm does not contain validations

def euclides_mcd(a, b):
    x = a
    y = b
    while(y != 0):
        r = x % y
        x = y
        y = r
    return x

def main():
    print("euclides mcd")
    print("enter [a] and [b] non-zero numbers to find their [mcd]")
    a = int(input("a?: "))
    b = int(input("b?: "))
    print("mcd:", euclides_mcd(a, b))


if __name__ == "__main__":
    main()
    
def findFactor(number):
    i = 2
    while number % i != 0:
        i += 1
    return i
    
def main():
    factor = int
    number = int(input('Number?: '))
    while number != 1:
        factor = findFactor(number)
        print(f'{number} | {factor}')
        number = int(number / factor)
    print('1 |')

if __name__ == "__main__":
    main()
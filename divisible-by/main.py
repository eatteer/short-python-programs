def main():
    n = int(input('[n] value: '))
    d = int(input('[d] value: '))
    if n <= 0 or d <= 0:
        print('Natural numbers only')
    else:
        counter = 0
        print('Result')
        for i in range(1, n + 1):
            if i % d == 0:
                counter += 1
                print(f'{d}|{i} = {int(i/d)}')
        print(f'{counter} integers do not exceed n={n} and are divisible by d={d}')

if __name__ == "__main__":
    main()
    
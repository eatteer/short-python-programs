import math

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
      root = int(math.sqrt(n)) + 1
      for i in range(2, root):
          if n % i == 0:
              return False
      return True

def main():
    n = int((input('Number?: ')))
    if isPrime(n):
        print('It\'s prime')
    else:
        print('It\'s not prime')

if __name__ == "__main__":
    main()
    
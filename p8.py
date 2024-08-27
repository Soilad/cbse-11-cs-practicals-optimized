def main(l = 0):
    n = int(input('give number: '))
    for i in range(2,n):
        if n%i:
            l = 1
    print(f'{n} is prime') if l == 0 else print(f'{n} is compsite')

if __name__ == '__main__':
    main()

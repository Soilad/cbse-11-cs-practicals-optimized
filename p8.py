def main(l):
    n = int(input('give number: '))
    for i in list(range(3,round(n**0.5),2))+[2]:
        if not n%i:
            l=1
            break
    print(f'{n} is prime') if not l else print(f'{n} is compsite')

if __name__ == '__main__':
    main(0)

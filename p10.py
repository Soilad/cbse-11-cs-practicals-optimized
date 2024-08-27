from math import gcd,lcm

def main():
    n,m = int(input('give number: ')),int(input('give another number: '))
    print(f'gcd {gcd(n,m)}\nlcm {lcm(n,m)}')

if __name__ == '__main__':
    main()

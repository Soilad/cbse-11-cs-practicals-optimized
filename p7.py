def perfect(sum):
    n = int(input('give number: '))
    for i in range(1,n-1):
        if n%i == 0:
            sum += i
    print(f'{n} is a perfect number') if sum == n else print('no')

def armstrong(sum):
    n = input('give number: ')
    for i in n:
        sum += int(i)**3
    print(f'{n} is an armstrong number') if sum == int(n) else print('no')

def palindrome():
    n = input('give number: ')
    print('palindrome') if n == n[::-1] else print('no')

    
if __name__ == '__main__':
    perfect(0)
    armstrong(0)
    palindrome()

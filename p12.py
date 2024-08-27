def main(str):
    print(f'is palindrome, reversed cases: {str.swapcase()}') if str == str[::-1] else print(f'not palindrome, reversed cases: {str.swapcase()}')

if __name__ == '__main__':
    main(input('give string: '))

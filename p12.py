def main(str = input('give string: ')):
    print('is palindrome') if str == str[::-1] else print('not palindrome')

if __name__ == '__main__':
    main()

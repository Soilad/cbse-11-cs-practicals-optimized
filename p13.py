def main(l = [int(i) for i in input('give a list (separate with commas): ').split(',')]):
    print(f'highest value is {max(l)}, lowest value is {min(l)}')

if __name__ == '__main__':
    main()

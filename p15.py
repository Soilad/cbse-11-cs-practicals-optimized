def main(l,i = input('give a list (separate with commas): ').split(','),input('enter element to search'))
    print(f'{i} is in {l}') if i in l else print(f'{i} is not in {l}')

if __name__ == '__main__':
    main()

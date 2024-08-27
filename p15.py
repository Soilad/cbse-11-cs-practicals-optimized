def main(l,i = input('enter element to search: ')):
    print(f'{i} is in {l}') if i in l else print(f'{i} is not in {l}')

if __name__ == '__main__':
    l,t = ['a','s','d','f'],('a','s','d','f')
    main(l)
    main(t)

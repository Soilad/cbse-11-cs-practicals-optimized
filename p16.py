def main(l):
    while ['exit'] not in l:
        l.append(input('give students detail in the form of name,roll no.,mark (type exit to exit): ').split(','))
    l.remove(['exit'])
    print(*list(filter(lambda x: (int(x[2])>75),l)))

if __name__ == '__main__':
    main([])

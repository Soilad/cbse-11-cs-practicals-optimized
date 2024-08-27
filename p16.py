def main(l):
    while ['0','0','0'] not in l:
        l.append(input('give students detail in the form of name,roll no.,mark (type 0,0,0 to exit): ').split(','))
    print(*list(filter(lambda x: (int(x[2])>75),l)))

if __name__ == '__main__':
    main([])

def main(str = input('give string: ')):
    vowels = ['a','e','i','o','u']
    allcaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    vcount = acount = 0
    length = len(str)
    for i in vowels:
        vcount += str.lower().count(i)
    for j in allcaps:
        acount += str.count(j)
    ccount,lcount = length - vcount,length - acount
    print(f'number of vowels: {vcount} \nnumber of consonants {ccount} \nnumber of uppercase letters {acount} \nnumber of lowercase letters {lcount}')

if __name__ == '__main__':
    main()

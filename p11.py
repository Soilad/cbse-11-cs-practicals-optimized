def main(str = input('give string: ')):
    vowels = ['a','e','i','o','u']
    vcount = acount = 0
    length = len(str)
    for i in vowels:
        vcount += str.lower().count(i)
    for j in set(str):
        acount += str.count(j) if not j.islower() else 0
    ccount,lcount = length - vcount,length - acount
    print(f'number of vowels: {vcount} \nnumber of consonants {ccount} \nnumber of uppercase letters {acount} \nnumber of lowercase letters {lcount}')

if __name__ == '__main__':
    main()

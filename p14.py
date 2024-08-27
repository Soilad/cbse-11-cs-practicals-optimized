def main(l = input('give a list (separate with commas): ').split(','))
    try:
        print(f'list before swap: {l}')
        for i in range(0,len(l),2):
            l[i],l[i+1]=l[i+1],l[i]
        print(f'list after swap: {l}')
    except:
        print('error')

if __name__ == '__main__':
    main()

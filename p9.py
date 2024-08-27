def main(n=0,t=1):
    while n<10:
        n,t = t,n+t
        print(n)

if __name__ == '__main__':
    main()

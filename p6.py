def main(a):
    x,n = int(input("give number: ")),int(input("give power: "))
    for i in range(1,n+1):
        a+=(x**(i))/i if i%3!=0 else -(x**(i))/i
    print(a)

if __name__ == '__main__':
    main(0)



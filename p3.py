#pattern 1????
def pattern1():
    for i in range(1,6):
            print("*"*i)

# pattern 2???????????????
def pattern2():
    for i in reversed(range(0,6)):
        print(*range(1,i+1))

# pattern 3??????
def pattern3(x=''):
    for i in range(65,70):
        print(x := f"{x}{chr(i)}")

if __name__ == '__main__':
      pattern3()

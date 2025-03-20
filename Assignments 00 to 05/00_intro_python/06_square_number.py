def Square_Of_Numbers():
    num: float = float(input("Type a number to see its square: ")) # casting it with float so we can do math 
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!



if __name__ == '__main__':
    Square_Of_Numbers()

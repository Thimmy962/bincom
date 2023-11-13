def main():
    x = input("Number to be searched for: ")
    b = list(range(1, 10001))
    g = recursive(int(x), b)
    print(g)
    
def recursive(target, number, begin=0):
    # target = the number to search for
    # number = a list of numbers in which target is to be searched from

    if begin == len(number):
        return "Not Found"
    
    if target == number[begin]:
        return "Found"
    else:
        return recursive(target, number, begin + 1)

if __name__ == "__main__":
    main()

def main():
    print(fib_sum())
def fib_sum():
    num = [0, 1]

    while len(num) < 50:
        nxt = num[-2] + num[-1]
        num.append(nxt)
    return sum(num)


if __name__ == "__main__":
    main()
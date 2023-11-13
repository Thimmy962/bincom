import random

def main():
    # Generate a random binary number
    bi_num = generate_binary_number()
  

    # print("Generated Binary Number:", bi_num)

    # Convert binary to decimal
    decimal_number = binary_to_decimal(bi_num)
    print("Decimal Equivalent:", decimal_number)


def generate_binary_number():
    # Generate a random 4-digit binary number
    bi_num = ''.join(random.choice(["0", "1"]) for _ in range(4))
    return bi_num

def binary_to_decimal(bi_num):
    # Convert binary to decimal
    decimal_number = int(bi_num, 2)
    return decimal_number


if __name__ == "__main__":
    main()

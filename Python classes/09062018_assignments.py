# WTP to check the number of ones in the binary of a number

def count_one_bits(num):
    x, y = 1, -1
    count = 0
    while (y & num) != 0:
        if (x & num) != 0:
            count += 1
        x = x << 1
        y = y << 1
    return count

def count_zero_bits(num):
    x, y = 1, -1
    count = 0
    while (y & num) != 0:
        if (x & num) == 0:
            count += 1
        x = x << 1
        y = y << 1
    return count

# WTP to accept a number and check if it is divisible without using arithmetic operators
def check_if_divisible(num):
    if num & 7:
        return False
    else:
        return True

# hw: wtp to check if a number is multiple of 64
# hw: wtp to accept a number from user, accept a bit position which should be turned off from the given number

def main():
    number = 120
    print("Number of zero bits in {} is {}".format(number, count_zero_bits(number)))
    print("Number of one bits in {} is {}".format(number, count_one_bits(number)))

    if check_if_divisible(number):
        print("{} is divisible by 8".format(number))
    else:
        print("{} is not divisible by 8".format(number))

if __name__ == "__main__":
    main()

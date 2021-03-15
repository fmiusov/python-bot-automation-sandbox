
numbers = []

def loopo(start, range, increment):
    """feed in starting int, range of ints, and incrementing int"""
    i = start
    while i < range:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

loopo(2, 15, 3)
if __name__ == '__main__':
    # Read the input integer
    n = int(input().strip())

    # Check if the input is within the valid range of 1 to 100
    if n >= 1 and n <= 100:
        # Check the conditions based on the given problem statement

        # If n is odd
        if n % 2 != 0:
            print("Weird")

        # If n is even and in the range of 2 to 5 (inclusive)
        elif n % 2 == 0 and n in range(2, 6):
            print("Not Weird")

        # If n is even and in the range of 6 to 20 (inclusive)
        elif n % 2 == 0 and n in range(6, 21):
            print("Weird")

        # If n is even and greater than 20
        elif n % 2 == 0 and n > 20:
            print("Not Weird")

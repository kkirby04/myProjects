if __name__ == '__main__':
    # Read an integer from STDIN
    n = int(input())

    # Create a list comprehension to generate the numbers from 1 to n
    numbers = [str(i+1) for i in range(n)]

    # Join the numbers using an empty string as the separator and print on one line
    print(''.join(numbers))
    
if __name__ == '__main__':
    # Prompt the user to input a string
    s = input()

    # Check if the string contains any alphanumeric characters
    print(any(char.isalnum() for char in s))  # True if alphanumeric characters present, False otherwise

    # Check if the string contains any alphabetical characters
    print(any(char.isalpha() for char in s))  # True if alphabetical characters present, False otherwise

    # Check if the string contains any digits
    print(any(char.isdigit() for char in s))  # True if digits present, False otherwise

    # Check if the string contains any lowercase characters
    print(any(char.islower() for char in s))  # True if lowercase characters present, False otherwise

    # Check if the string contains any uppercase characters
    print(any(char.isupper() for char in s))  # True if uppercase characters present, False otherwise

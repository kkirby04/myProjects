def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    
    return count

if __name__ == '__main__':
    original_string = input()
    
    sub_string = input()
    
    result = count_substring(original_string,sub_string)
    print(result)
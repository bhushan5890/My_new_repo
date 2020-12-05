# Python code to check palindrome


def check_palindrome(ip_string):
    ip_string = ip_string.replace(' ', '')
    return ip_string == ip_string[::-1]


if __name__ == "__main__":
    input_string = input("Enter the string to be validated-Case sensetive : ")
    if check_palindrome(input_string) == True:
        print(f'String {input_string} is a Palindrome')
    else:
        print(f'String {input_string} is not a Palindrome')

# 10. The palindrome of a number is the number obtained by reversing the order of its digits
# (e.g. the palindrome of 237 is 732). For a given natural number n, determine its palindrome.


def palindrome(number):
    """
    The function calculates the palindrome of a given number n
    :param number: natural number n
    :return: the palindrome of the number n
    """
    x = 0
    while number != 0:
        x = x * 10
        x = x + number % 10
        number = int((number - number % 10)/10)
    return x


if __name__ == '__main__':
    n = input("Read n=")
    print(palindrome(int(n)))

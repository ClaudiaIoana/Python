# 5. Generate the largest prime number smaller than a given natural number n.
# If such a number does not exist, a message should be displayed.

def prime(numb):
    """ The function tests if a given number n is prime or not
    :param numb: natural number n
    :return: 1 if the number is prime and 0 otherwise
    """
    if numb == 2:
        return 1
    if numb <= 1 or numb % 2 == 0:
        return 0
    for i in range(numb-1, 2, -1):
        if numb % i == 0:
            return 0
    return 1


def search(numb):
    """
    The function searches for the largest prime number smaller than a given number n
    :param numb: natural number n
    :return: 1 if the prime number smaller than num exists and 0 otherwise
    """
    for i in range(numb-1, 1, -1):
        if prime(i) == 1:
            return i
    return 0


if __name__ == '__main__':
    num = input("Read n = ")
    x = search(int(num))
    if x == 0:
        print('there is no prime number smaller that '+str(num))
    else:
        print(x)

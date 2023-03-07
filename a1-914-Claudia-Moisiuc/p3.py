# 15. Generate the largest perfect number smaller than a given natural number n.
# If such a number does not exist, a message should be displayed.
# A number is perfect if it is equal to the sum of its divisors, except itself.
# (e.g. 6 is a perfect number, as 6=1+2+3).


def perfect_number(num):
    """
    the function calculates the sum of the given n number's divisors
    :param num:natural number n
    :return:the sum of n's divisors
    """
    summ = 0
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            summ = summ + i
    return summ


def perf_smaller_than_n(num):
    """
    the function generates the largest perfect number smaller than a given natural number n
    :param num: natural number n
    :return: the largest perfect number smaller than n
    """
    for i in range(num-1, -1, -1):
        if i == perfect_number(i):
            return i
    return -1


if __name__ == '__main__':
    n = input("Read n=")
    x = perf_smaller_than_n(int(n))
    if x == -1:
        print("a perfect number smaller than n does not exist")
    else:
        print(x)

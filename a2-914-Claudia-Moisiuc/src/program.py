# 6.Distinct numbers.
# 12.Both real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)

def set_complex(real, imaginary):
    real = int(real)
    imaginary = int(imaginary)
    return [real, imaginary]


def get_real(complex_number):
    return complex_number.get('real')


def get_imaginary(complex_number):
    return complex_number.get('imaginary')


def reading():
    """
        the function reads the new variables of the program
    """
    numb = int(input('The number of pairs:  '))
    com = {'real': [], 'imaginary': []}
    for i in range(0, numb):
        print('Pair ', i+1)
        com['real'].append(int(input('a = ')))
        com['imaginary'].append(int(input('b = ')))
    return com


def printing(complex_number):
    """
    the function prints the complex numbers
    :param complex_number: the list
    """
    r = get_real(complex_number)
    im = get_imaginary(complex_number)
    for i in range(0, int(len(r))):
        print('z = ', r[i], ' + ', im[i], ' * i')


def double(complex_number, i):
    """
    the function determines the longest sequence with different numbers starting from a given point i
    """
    secv = 0
    real = get_real(complex_number)
    imaginary = get_imaginary(complex_number)
    for x in range(i, len(real)-1):
        if real[i] == real[x] and imaginary[i] == imaginary[x]:
            print(x)
            secv = secv + 1
        else:
            i = len(real) + 3
    return secv


def log_sec(complex_number):
    """
    the function the largest sequence of different numbers
    :param complex_number: a list
    """
    li = {'real': [], 'imaginary': []}
    secv_max = 1
    start = 0
    for i in range(0, len(get_real(complex_number))-1):
        x = double(complex_number, i)
        if secv_max < x:
            secv_max = x
            start = i
    for i in range(start, start + secv_max):
        li['real'].append(get_real(complex_number)[i])
        li['imaginary'].append(get_imaginary(complex_number)[i])
    printing(li)
    print('the sequence contains', secv_max, 'numbers')


def same_dig(x):
    """
    the function determines if the number is formed like aaa
    """
    dig = x % 10
    x = x//10
    while x != 0:
        if x % 10 != dig:
            return 0
        else:
            x = x//10
    return 1


def same_ri(complex_number):
    """
    the function determines the largest sequence where both real and imaginary part can be written using the same digits
    """
    li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    secv_max = 0
    secv = 0

    for i in range(0, 5):
        if same_dig(complex_number[i*2]) == 1 and same_dig(complex_number[2*i+1]) == 1:
            secv += 2
        elif secv_max < secv:
            secv_max = secv
            inc = 2*i-secv
            secv = 0
            li = complex_number[inc:inc+secv_max]

    if secv_max >= 1:
        print(li)


if __name__ == '__main__':
    complex = {'real': [7, 77, 81, 21, 5], 'imaginary': [20, 23, 45, 21, 9]}
    print('Now we would like for you to choose an option. The available options are displayed here: ')
    print('1. Read a list of complex numbers (in `z = a + bi` form).')
    print('2. Display the entire list of numbers on the console.')
    print('3. Display the entire list of numbers on the console in `z = a + bi` form.')
    print('4. Calculate the longest sequence of distinct complex numbers')
    print('5. Print the groups where both real and imaginary parts can be written using the same base 10 digits ')
    print('6. If you do not like the program you can exit')
    ok = True
    while ok:
        av = int(input('Which option would you prefer  '))
        if av == 1:
            complex = reading()
        elif av == 2:
            print("Real numbers: ")
            print(get_real(complex))
            print("Imaginary numbers: ")
            print(get_imaginary(complex))
        elif av == 3:
            printing(complex)
        elif av == 4:
            log_sec(complex)
        elif av == 5:
            same_ri(complex)
        else:
            print('We are sorry that you fell like leaving the program. We hope to see you soon')
            ok = False

"""
  Write non-UI functions below
"""
# 4. Bank Account


def test():
    assert nr('19') == 1
    assert set_transaction([], 3, 12, 'in', 'pizza') == [3, 12, 'in', 'pizza']
    assert nr_day('text 24') == 24
    assert elim_cuv('text de 24') == 'de 24'
    assert find_day('insert 24') == 24
    assert find_value('24 text') == 24
    assert find_type('in text') == 'in'
    assert find_desc('pizza in text') == 'pizza'


def nr(aux):
    i = 0
    while i != len(aux) and aux[i] != ' ':
        if aux[i] < '0' or aux[i] > '9':
                return 0
        i = i + 1
    return 1


def error_op1():
    ok = True
    while ok:
        error = 0
        ok = False
        t = input('addition: ')
        aux = t
        if aux[0:4] != 'add ' and aux[0:7] != 'insert ':
            print(' ERROR ! Please try again. The data introduced is wrong')
            error = 1
        elif aux[0:7] == 'insert ' and (0 >= nr_day(aux) >= 31):
            print(' ERROR ! Please try again. The data introduced is wrong')
            error = 1
        elif aux[0:7] == 'insert ':
            aux = elim_cuv(aux)
        aux = elim_cuv(aux)
        if nr(aux) == 0:
            if error == 0:
                print(' ERROR ! Please try again. The data introduced is wrong')
                error = 1
        aux = elim_cuv(aux)
        if find_type(aux) == '-':
            if error == 0:
                print(' ERROR ! Please try again. The data introduced is wrong')
                error = 1
        if error == 1:
            ok = True
    return t


def error_op2():
    ok = True
    while ok:
        error = 0
        ok = False
        t = input('modification: ')
        aux = t
        if aux[0:7] != 'remove ' and aux[0:8] != 'replace ':
            print(' ERROR ! Please try again. The data introduced is wrong')
            error = 1
        elif aux[0:7] == 'remove ':
            aux = elim_cuv(aux)
            if '0' <= aux[0] <= '9':
                if nr(aux) == 0:
                    if error == 0:
                        print(' ERROR ! Please try again. The data introduced is wrong')
                        error = 1
                if len(aux) > 2:
                    aux = elim_cuv(aux)
                    if aux[0:3] != 'to ':
                        if error == 0:
                            print(' ERROR ! Please try again. The data introduced is wrong')
                            print(1)
                            error = 1
                    else:
                        aux = elim_cuv(aux)
                        if nr(aux) == 0:
                            if error == 0:
                                print(' ERROR ! Please try again. The data introduced is wrong')
                                error = 1
            elif find_type(aux) == '-':
                if error == 0:
                    print(' ERROR ! Please try again. The data introduced is wrong')
                    error = 1
        else:
            aux = elim_cuv(aux)
            if nr(aux) == 0:
                if error == 0:
                    print(' ERROR ! Please try again. The data introduced is wrong')
                    error = 1
            aux = elim_cuv(aux)
            if find_type(aux) == '-':
                if error == 0:
                    print(' ERROR ! Please try again. The data introduced is wrong')
                    print('aici2')
                    error = 1
            aux = elim_cuv(aux)
            aux = elim_cuv(aux)
            if aux[0:5] != 'with ':
                if error == 0:
                    print(' ERROR ! Please try again. The data introduced is wrong')
                    error = 1
            else:
                aux = elim_cuv(aux)
                if nr(aux) == 0:
                    if error == 0:
                        print(' ERROR ! Please try again. The data introduced is wrong')
                        error = 1
        if error == 1:
            ok = True
    return t


def error_op3():
    ok = True
    while ok:
        error = 0
        ok = False
        t = input('listing: ')
        aux = t
        if aux[0:4] != 'list':
            print(' ERROR ! Please try again. The data introduced is wrong')
            error = 1
        if len(aux) > 4:
            aux = elim_cuv(aux)
            if aux[0] == '>' or aux[0] == '=' or aux[0] == '<' or aux[0:8] == 'balance ':
                aux = elim_cuv(aux)
                if nr(aux) == 0:
                    if error == 0:
                        print(' ERROR ! Please try again. The data introduced is wrong')
                        error = 1
            elif find_type(aux) == '-':
                if error == 0:
                    print(' ERROR ! Please try again. The data introduced is wrong')
                    error = 1
        if error == 1:
                ok = True
    return t


def creat_transaction(day, amount, type, description):
    return [day, amount, type, description]


def set_transaction(transactions, day, amount, type, description):
    trans = creat_transaction(day, amount, type, description)
    transactions.append(trans)


def auto_set_transaction(transactions):
    """
    Setting 10 initial transactions in the list
    :param transactions:
    """
    set_transaction(transactions, 1, 115, 'in', 'salary')
    set_transaction(transactions, 3, 16, 'out', 'food')
    set_transaction(transactions, 7, 8, 'in', 'economy')
    set_transaction(transactions, 10, 2, 'out', 'cat food')
    set_transaction(transactions, 13, 5, 'in', 'economy')
    set_transaction(transactions, 16, 12, 'out', 'food')
    set_transaction(transactions, 18, 10, 'out', 'party')
    set_transaction(transactions, 20, 8, 'out', 'vet')
    set_transaction(transactions, 20, 13, 'out', 'vet')
    set_transaction(transactions, 30, 115, 'in', 'salary')


def get_day(transactions,i):
    return transactions[i][0]


def get_value(transactions, i):
    return transactions[i][1]


def get_type(transactions, i):
    return transactions[i][2]


def get_description(transactions, i):
    return transactions[i][3]

# A. Add transaction


def insert(transactions, i):
    """
    The function is used for inserting transactions, so when we display the transactions they are ordered considering the 'day' as a the main criteria.
    """
    day = get_day(transactions, -1)
    j = -1
    if i < day:
        # we memorise the items of the last transaction
        value = get_value(transactions, -1)
        type = get_type(transactions, -1)
        desc = get_description(transactions, -1)
        set_transaction(transactions, day, value, type, desc)
        while i < day:
            transactions[j] = transactions[j-1]
            j = j-1
            day = get_day(transactions, j)
    else: set_transaction(transactions, 0, 0, '0', '0')
    return j+1


def nr_day(list):
    """
    The function separates the first number from a text
    :param list: the text
    :return: the first natural number
    """
    i = 0
    while list[i] < '0' or list[i] > '9':
        i = i+1
    nr = int(list[i])
    i = i+1
    while i < len(list) and '0' <= list[i] <= '9':
        nr = nr*10+int(list[i])
        i = i+1
    return nr


def elim_cuv(list):
    """
    The program eliminates the first word from the text
    :param list: the text
    :return: the text without the first word
    """
    spatiu = 0
    i = 0
    while spatiu != 1:
        if list[i] == ' ':
            spatiu = spatiu + 1
        i = i + 1
    list = list[i:]
    return list


def find_day(list):
    """
    the function separates the day from the text
    :param list: the text
    :return: the day
    """
    if list[0:7] == 'insert ':
        day = nr_day(list)
    else:
        day = -1
    return day

def find_value(list):
    """
    the function returns the value from the text
    :param list: the text
    :return: the value
    """
    i = 0
    value = 0
    while list[i] != ' ':
        value = value * 10 + int(list[i])
        i = i + 1
    return value

def find_type(list):
    """
    the function returns the type of the transaction if there is one
    :param list: the text
    :return: type
    """
    if list[0:3] == 'out':
        t = 'out'
    elif list[0:2] == 'in':
        t = 'in'
    else: t = '-'
    return t

def find_desc(list):
    """
    the function returns the description of the transaction
    :param list: the text
    :return: the description
    """
    i = 0
    while list[i] != ' ':
        i = i + 1
    list = list[:i]
    return list


def add_trans(transactions, t):
    """
    the function adds a new transaction according to the text that was read. it also separets the parts of the text that are crutial to understanding the transaction.
    :param transactions: the transactions that already exist
    :param t: the text inputted
    """
    if t[0:4] == 'add ':
        day = 22
    else:
        day = find_day(t)
        t = elim_cuv(t)
    t = elim_cuv(t)
    value = find_value(t)
    t = elim_cuv(t)
    type = find_type(t)
    t = elim_cuv(t)
    description = t
    poz = insert(transactions, day)
    transactions[poz] = creat_transaction(day, value, type, description)

# B. Modify transactions


def elim_transaction(transactions, index):
    '''
    the funtion eliminates the transaction with index == index
    '''
    del transactions[index]


def elim_trans_days(transactions, day1, day2):
    '''
    the function eliminates the transactions between the inputted days
    :param transactions: the transactions
    :param day1: the first day
    :param day2: the last day
    '''
    n = len(transactions)
    elim = 0
    i = 0
    while i < n-elim:
        day = get_day(transactions, i)
        if day1 <= day <= day2:
            elim_transaction(transactions, i)
            elim = elim + 1
        else: i = i + 1


def elim_trans_type(transactions,type):
    '''
    the function eliminates the transactions that have the same type as the one inputted
    :param transactions: the rtransactions
    :param type: the inputted type
    '''
    n = len(transactions)
    elim = 0
    i = 0
    while i < n - elim:
        ty = get_type(transactions, i)
        if ty == type:
            elim_transaction(transactions, i)
            elim = elim + 1
        else:
            i = i + 1


def replace(transactions, day, type, description, value):
    '''
    the function replaces the transactions that meet the requirements inputted
    :param transactions: the transactions
    :param day: the inputted day
    :param type: the inputted type
    :param description: the inputted description
    :param value: the value with which the transaction is going to be replaced
    '''
    n = len(transactions)
    i = 0
    while i < n:
        dy = get_day(transactions, i)
        ty = get_type(transactions, i)
        desc = get_description(transactions, i)
        if dy == day and ty == type and desc == description:
            transactions[i][1] = value
        i = i + 1


def modify(transactions,t):
    """
    the function is the main body for the second option
    :param transactions: the transactions
    :param t: the text
    """
    if t[0:7] == 'remove ':
        t = elim_cuv(t)
        if '0' <= t[0] <= '9':
            day1 = nr_day(t)
            if len(t) > 2:
                t = elim_cuv(t)
                t = elim_cuv(t)
                day2 = nr_day(t)
            else: day2 = day1
            elim_trans_days(transactions, day1, day2)
        else:
            type = find_type(t)
            elim_trans_type(transactions, type)

            if type == '-':
                print(-1)
    elif t[0:8] == 'replace ':
        t = elim_cuv(t)
        day = nr_day(t)
        t = elim_cuv(t)
        type = find_type(t)
        t = elim_cuv(t)
        desc= find_desc(t)
        t = elim_cuv(t)
        t = elim_cuv(t)
        value = int(t)
        replace(transactions,  day, type, desc, value)

# Display


def list_all(transactions):
    """
    the program displays all the transactions
    :param transactions: the transactions
    """
    n = len(transactions)
    for i in range(0, n):
        print(transactions[i])


def list_type(transactions, type):
    """
    the program displays all the transactions with type as the one inputted
    :param transactions: the transactions
    :param type: the type inputted
    """
    n = len(transactions)
    i = 0
    while i < n:
        ty = get_type(transactions, i)
        if ty == type:
            print(transactions[i])
        i = i + 1


def list_same_amount(transactions, t):
    """
    the function displays all the transactions with a value [ < | = | > ] than the inputted value
    :param transactions: the transactions
    :param t: the text
    """
    simbol = t[0]
    t = elim_cuv(t)
    nr = int(t)
    n = len(transactions)
    i = 0
    while i < n:
        v = get_value(transactions, i)
        if simbol == '=':
            if nr == v:
                print(transactions[i])
        elif simbol == '>':
            if v > nr:
                print(transactions[i])
        elif v < nr:
            print(transactions[i])
        i = i + 1


def balance_day(transactions, day):
    """
    the function calculates the amount of money spent and saved till an inputted day
    :param transactions: the transactions
    :param day: the given day
    """
    n = len(transactions)
    sum = 0
    i = 0
    while i < n:
        dy = get_day(transactions, i)
        if dy <= day:
            type = get_type(transactions, i)
            if type == 'in':
                sum = sum + get_value(transactions, i)
            else:
                sum = sum - get_value(transactions, i)
        i = i + 1
    return sum


def display(transactions, t):
    """
    the function is the main body for the last option
    :param transactions: the transactions
    :param t: the text
    """
    if len(t) == 4:
        list_all(transactions)
    else:
        t = elim_cuv(t)
        type = find_type(t)
        if type != '-':
            list_type(transactions, type)
        elif t[0] == '=' or t[0] == '>' or t[0] == '<':
            list_same_amount(transactions, t)
        else:
            t = elim_cuv(t)
            nr = int(t)
            sum=balance_day(transactions, nr)
            print(sum)

"""
  Write the command-driven UI below
"""

if __name__ == '__main__':
    transactions = []
    auto_set_transaction(transactions)
    a = """The options you can choose from:
            A. Add transactions
            B. Modify transactions
            C. Display transactions having different properties
            D. Stop the program"""
    op1 = """the inputs available for this option are:
            add <value> <type> <description>
            insert <day> <value> <type> <description>"""
    op2 = """the inputs available for this option are:
            remove <day>
            remove <start day> to <end day>
            remove <type>
            replace <day> <type> <description> with <value>"""
    op3 = """the inputs available for this option are:
            list
            list <type>
            list [ < | = | > ] <value>
            list balance <day>"""
    print(a)
    print(op1)
    print(op2)
    print(op3)
    ok = True
    while ok == True:
        option= input('Introduce the option: ')
        if option == 'A' or option == 'a':
            t = error_op1()
            add_trans(transactions, t)
        elif option == 'B' or option == 'b':
            t = error_op2()
            modify(transactions,t)
        elif option == 'C' or option == 'c':
            t = error_op3()
            display(transactions,t)
        elif option == 'D' or option == 'd':
            ok = False
        else: print('ERROR! the option inputted is not available. please try again ')





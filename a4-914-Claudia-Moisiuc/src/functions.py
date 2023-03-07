"""
  Program functionalities module
"""


def creat_transaction(day, amount, typ, description):
    return [day, amount, typ, description]


def set_transaction(transactions, day, amount, typ, description):
    trans = creat_transaction(day, amount, typ, description)
    transactions. append(trans)


def auto_set_transaction(transactions):
    """
    Setting 10 initial transactions in the list
    :param transactions:
    """
    set_transaction(transactions, 1, 115, 'in', 'salary')
    set_transaction(transactions, 3, 16, 'out', 'food')
    set_transaction(transactions, 7, 8, 'in', 'economy')
    set_transaction(transactions, 10, 2, 'out', 'cat food')
    set_transaction(transactions, 16, 5, 'in', 'economy')
    set_transaction(transactions, 20, 21, 'in', 'food')
    set_transaction(transactions, 20, 10, 'out', 'party')
    set_transaction(transactions, 20, 8, 'out', 'vet')
    set_transaction(transactions, 20, 13, 'out', 'vet')
    set_transaction(transactions, 30, 115, 'in', 'salary')


def get_day(transactions, i):
    return transactions[i][0]


def get_value(transactions, i):
    return transactions[i][1]


def get_type(transactions, i):
    return transactions[i][2]


def get_description(transactions, i):
    return transactions[i][3]


def nr(aux):
    i = 0
    while i != len(aux) and aux[i] != ' ':
        if aux[i] < '0' or aux[i] > '9':
                return 0
        i = i + 1
    return 1


def option_error(option):
    y = option.split()
    error = 0
    if y[0] == 'add' or y[0] == 'insert':
        if y[0] == 'add' and len(y) != 4:
            error = 1
        elif y[0] == 'insert' and len(y) != 5:
            error = 1
        if error == 0:
            if nr(y[1]) == 0:
                error = 1
            elif y[0] == 'insert' and nr(y[2]) == 0:
                error = 1
            elif find_type(y[3]) == '-' and find_type(y[2]) == '-':
                error = 1
    elif y[0] == 'remove':
        if len(y) == 1:
            error = 1
        if error == 0:
            if len(y) == 4:
                if y[2] != 'to' or nr(y[3]) == 0:
                    error = 1
            if nr(y[1]) == 0 and find_type(y[1]) == '-':
                error = 1
    elif y[0] == 'replace':
        if len(y) != 6:
            error = 1
        if error == 0:
            if nr(y[1]) == 0 or nr(y[5]) == 0:
                error = 1
            if find_type(y[2]) == '-':
                error = 1
            if y[4] != 'with':
                error = 1
    elif y[0] == 'list':
        if len(y) != 1:
            if len(y) == 2:
                if find_type(y[1]) == '-':
                    error = 1
            elif len(y[1]) == 1:
                if y[1] != '=' and y[1] != '<' and y[1] != '>':
                    error = 1
                if nr(y[2]) == 0:
                    error = 1
            elif y[1] != 'balance' or nr(y[2]) == 0:
                error = 1
    elif y[0] == 'sum':
        if len(y) != 2:
            error = 1
        elif find_type(y[1]) == '-':
            error = 1
    elif y[0] == 'max' or y[0] == 'filter':
        if len(y) != 3:
            error = 1
        elif find_type(y[1]) == '-' or nr(y[2]) == 0:
            error = 1
        if y[0] == 'filter' and len(y) == 2 and find_type(y[1]) != '-':
            error = 0
    return error


def tests():
    assert elim_space('    ana   are  mere   ') == 'ana are mere'
    assert creat_transaction(2, 3, 'in', 'pizza') == [2, 3, 'in', 'pizza']
    assert elim_cuv('text de 24') == 'de 24'
    assert take_word('text de 24') == 'text'
    assert elim_space('    text   of   23   ') == 'text of 23'
    assert find_type('in mag') == 'in'
    t = [[2, 3, 'in', 'pizza'], [4, 3, 'in', 'pizza']]
    elim_transaction(t, 0)
    assert t == [[4, 3, 'in', 'pizza']]
    add_trans(t, 'insert 12 13 in pizza')
    assert t == [[4, 3, 'in', 'pizza'], [12, 13, 'in', 'pizza']]
    elim_trans_days(t, 4, 5)
    assert t == [[12, 13, 'in', 'pizza']]
    add_trans(t, 'insert 22 13 out pizza')
    elim_trans_type(t, 'out')
    assert t == [[12, 13, 'in', 'pizza']]
    add_trans(t, 'insert 22 13 out pizza')
    add_trans(t, 'add 5 in pizza')
    assert balance_day(t, 30) == 5
    assert sum_in(t, 'in') == 18
    add_trans(t, 'add 15 in pizza')
    assert maxi(t, 'in', 29) == 3
    filteri(t, 'filter in')
    assert t == [[12, 13, 'in', 'pizza'], [29, 5, 'in', 'pizza'], [29, 15, 'in', 'pizza']]
    op = ['add 5 in pizza']
    undo_add(op, t)
    assert t == [[12, 13, 'in', 'pizza'], [29, 15, 'in', 'pizza']]


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


def take_word(list):
    """
    the function returns the description of the transaction
    :param list: the text
    :return: the description
    """
    i = 0
    n = len(list)
    while i < n and list[i] != ' ':
        i = i + 1
    list = list[:i]
    return list


def elim_space(text):
    """
    the function eliminates the unnecessary spaces of the option
    """
    while text[0] == ' ':
        text = text[1:]
    i = 1
    n = len(text)
    while i < n:
        if text[i] == ' ' and text[i-1] == ' ':
            c = text[0:i]
            b = text[i+1:]
            text = c + b
            n = n - 1
        else:
            i = i + 1
    if text[-1] == ' ':
        text = text[:-1]
    return text


def insert(transactions, i):
    """
    The function is used for inserting transactions, so when we display the transactions they are ordered considering
        the 'day' as the main criteria.
    """
    day = get_day(transactions, -1)
    j = -1
    if i < day:
        # we memorise the items of the last transaction
        value = get_value(transactions, -1)
        typ = get_type(transactions, -1)
        desc = get_description(transactions, -1)
        set_transaction(transactions, day, value, typ, desc)
        while i < day:
            transactions[j] = transactions[j-1]
            j = j - 1
            day = get_day(transactions, j)
    else:
        set_transaction(transactions, 0, 0, '0', '0')
        return -1
    return j + 1


def find_type(list):
    """
    the function returns the type of the transaction if there is one
    :param list: the text
    :return: type
    """
    cuv = take_word(list)
    if cuv == 'out':
        t = 'out'
    elif cuv == 'in':
        t = 'in'
    else:
        t = '-'
    return t


def add_trans(transactions, option):
    """
    the function adds a new transaction according to the text that was read. it also separates the parts of the text
        that are crucial to understanding the transaction.
    :param transactions: the transactions that already exist
    :param option: the text inputted
    """
    y = option.split()
    if y[0] == 'add':
        day = 29
        value = int(y[1])
        typ = y[2]
        description = y[3]
    else:
        day = int(y[1])
        value = int(y[2])
        typ = y[3]
        description = y[4]
    poz = insert(transactions, day)
    transactions[poz] = creat_transaction(day, value, typ, description)


def elim_transaction(transactions, index):
    """the function eliminates the transaction with index == index"""
    del transactions[index]


def elim_trans_days(transactions, day1, day2):
    """
    the function eliminates the transactions between the inputted days
    :param transactions: the transactions
    :param day1: the first day
    :param day2: the last day
    """
    n = len(transactions)
    elim = 0
    i = 0
    while i < n-elim:
        day = get_day(transactions, i)
        if day1 <= day <= day2:
            elim_transaction(transactions, i)
            elim = elim + 1
        else:
            i = i + 1


def elim_trans_type(transactions, typ):
    """
    the function eliminates the transactions that have the same type as the one inputted
    :param transactions: the transactions
    :param typ: the inputted type
    """
    n = len(transactions)
    elim = 0
    i = 0
    while i < n - elim:
        ty = get_type(transactions, i)
        if ty == typ:
            elim_transaction(transactions, i)
            elim = elim + 1
        else:
            i = i + 1


def replace(transactions, day, typ, description, value):
    """
    the function replaces the transactions that meet the requirements inputted
    :param transactions: the transactions
    :param day: the inputted day
    :param typ: the inputted type
    :param description: the inputted description
    :param value: the value with which the transaction is goind to be replaced
    """
    n = len(transactions)
    i = 0
    while i < n:
        dy = get_day(transactions, i)
        ty = get_type(transactions, i)
        desc = get_description(transactions, i)
        if dy == day and ty == typ and desc == description:
            transactions[i][1] = value
        i = i + 1


def modify(transactions, option):
    """
    the function is the main body for the second option
    :param transactions: the transactions
    :param option: the text
    """
    y = option.split()
    if y[0] == 'remove':
        day1 = nr(y[1])
        if day1 != 0:
            day1 = int(y[1])
            if len(y) > 2:
                day2 = int(y[3])
            else:
                day2 = day1
            elim_trans_days(transactions, day1, day2)
        else:
            typ = y[1]
            elim_trans_type(transactions, typ)
    elif y[0] == 'replace':
        day = int(y[1])
        typ = y[2]
        desc = y[3]
        value = int(y[5])
        replace(transactions,  day, typ, desc, value)


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
            typ = get_type(transactions, i)
            if typ == 'in':
                sum = sum + get_value(transactions, i)
            else:
                sum = sum - get_value(transactions, i)
        i = i + 1
    return sum


def sum_in(transactions, typ):
    """
    the function calculates the amount of money spent and saved till an inputted day
    :param transactions: the transactions
    """
    n = len(transactions)
    sum = 0
    i = 0
    while i < n:
        type1 = get_type(transactions, i)
        if typ == type1:
            sum = sum + get_value(transactions, i)
        i = i + 1
    return sum


def maxi(transactions, typ, day):
    """
    the function determines the maximum transaction that meets the requirements
    :param transactions: the transactions
    :param typ: the type
    :param day: the day
    :return: the position of the transaction
    """
    poz = -1
    n = len(transactions)
    max = 0
    for i in range(0, n):
        if get_day(transactions, i) == day:
            if get_type(transactions,i) == typ:
                v = get_value(transactions, i)
                if max < v:
                    max = v
                    poz = i
    return poz


def filteri(transactions, option):
    """
    the program filters the transactions
    :param transactions: the transactions
    :param option: the option
    """
    y = option.split()
    n = len(transactions)
    i = 0
    while i < n:
        if len(y) == 3:
            if get_value(transactions, i) > int(y[2]):
                elim_transaction(transactions, i)
                n = n - 1
            else:
                i = i + 1
        else:
            if get_type(transactions, i) != y[1]:
                elim_transaction(transactions, i)
                n = n - 1
            else:
                i = i + 1


def undo_add(options, transactions):
    """
    the function undo the adding operations
    """
    y = options[-1].split()
    if y[0] == 'add':
        day = 29
        value = int(y[1])
        typ = y[2]
        desc = y[3]
    else:
        day = int(y[1])
        value = int(y[2])
        typ = y[3]
        desc = y[4]
    n = len(transactions)
    i = 0
    while i < n:
        if get_day(transactions, i) == int(day):
            if get_value(transactions, i) == value:
                if get_type(transactions, i) == typ and get_description(transactions, i) == desc:
                    elim_transaction(transactions, i)
                    break
        i = i + 1
    return transactions


def undo(options, transactions, eliminate):
    """
    the function is the main body for the undo operation
    :param options: the option
    :param transactions: the transactions
    :param eliminate: the modified lists
    """
    if len(options) == 0:
        print('there are no more options to undo')
    else:
        y = options[-1].split()
        if y[0] == 'add' or y[0] == 'insert':
            transactions = undo_add(options, transactions)
        elif y[0] == 'remove' or y[0] == 'replace' or y[0] == 'filter':
            transactions = eliminate[-1].copy()
            del eliminate[-1]
        del options[-1]
    return transactions

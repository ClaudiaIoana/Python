"""
  User interface module
"""



def list_all(transactions):
    '''
    the program displays all the transactions
    :param transactions: the transactions
    '''
    n = len(transactions)
    for i in range(0, n):
        print(transactions[i])

def list_type(transactions, type):
    '''
    the program displays all the transactions with type as the one inputted
    :param transactions: the transactions
    :param type: the type inputted
    '''
    n = len(transactions)
    i = 0
    while i < n:
        from src.functions import get_type
        ty = get_type(transactions, i)
        if ty == type:
            print(transactions[i])
        i = i + 1

def list_same_amount(transactions, t):
    '''
    the function displays all the transactions with a value [ < | = | > ] than the inputted value
    :param transactions: the transactions
    :param t: the text
    '''
    simbol = t[0]
    from src.functions import elim_cuv
    t = elim_cuv(t)
    nr = int(t)
    n = len(transactions)
    i = 0
    while i < n:
        from src.functions import get_value
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

def display(transactions, t):
    '''
    the function is the main body for the last option
    :param transactions: the transactions
    :param t: the text
    '''
    if len(t) == 4:
        list_all(transactions)
    else:
        from src.functions import elim_cuv
        t = elim_cuv(t)
        from src.functions import find_type
        type = find_type(t)
        if type != '-':
            list_type(transactions, type)
        elif t[0] == '=' or t[0] == '>' or t[0] == '<':
            list_same_amount(transactions, t)
        else:
            t = elim_cuv(t)
            nr = int(t)
            from src.functions import balance_day
            sum=balance_day(transactions, nr)
            print(sum)

def characteristics(transactions, option):
    '''
    the program is the main body for the forth option
    :param transactions: the transactions
    :param option: the option
    '''
    y=option.split()
    if y[0]== 'sum':
        from src.functions import sum_in
        print(sum_in(transactions, y[1]))
    else:
        from src.functions import maxi
        poz=maxi(transactions, y[1], int(y[2]))
        if poz==-1:
            print('there is no tranasction that meets the requirements')
        else:
            print(transactions[poz])

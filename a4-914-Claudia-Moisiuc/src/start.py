"""
  Start the program by running this module
"""
from src.functions import tests, auto_set_transaction, elim_space, option_error, filteri


def option_reader(option, transactions, options, eliminate):
    '''
    this function interpretations the inputted options
    :param option: the option
    :param transactions: the transactions
    '''
    #from src.functions import take_word
    #op = take_word(option)
    op = option
    if op == 'add' or op == 'insert':
        options.append(option)
        from src.functions import add_trans
        add_trans(transactions, option)
    elif op == 'remove' or op == 'replace':
        options.append(option)
        t=transactions.copy()
        eliminate.append(t)
        from src.functions import modify
        modify(transactions, option)
    elif op == 'list':
        from src.ui import display
        display(transactions, option)
    elif op == 'sum' or op == 'max':
        from src.ui import characteristics
        characteristics(transactions,option)
    elif op == 'filter':
        options.append(option)
        t = transactions.copy()
        eliminate.append(t)
        filteri(transactions,option)
    elif op == 'undo':
        from src.functions import undo
        transactions = undo(options,transactions,eliminate)
    elif op == 'leave':
        pass
    else:
        print('Invalid input')
    return transactions


if __name__ == '__main__':
    tests()
    transactions = []
    options = []
    eliminate = []
    auto_set_transaction(transactions)
    a = """The options you can choose from:
                A. Add transactions
                B. Modify transactions
                C. Display transactions having different properties
                D. Obtain different characteristics of the transactions
                E. Filter
                F. Undo
                G. Stop the program"""
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
    ok = True
    while ok:
        option = input('the option:  ')
        option = elim_space(option)
        if option_error(option) == 0:
            transactions = option_reader(option, transactions, options, eliminate)
            if option == 'leave':
                ok = False
        else:
            print('Invalid input')



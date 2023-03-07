class Out:
    def inv(self):
        print('invalid')

    def afis(self, i, stud):
        print(stud[i]._id, '  ', stud[i].name, '  ', stud[i].group)

    def no_more(self):
        print('no more options to undo')

    def print_menu(self):
        a = '''Options:
            1. Add a student.
            2. Display the list of students.
            3. Filter the list so that students in a given group (read from the console) are deleted from the list.
            4. Undo the last operation that modified program data. This step can be repeated.
            5. Leave'''


def afis(stud, outi):
    """
    the function lists the data
    :param stud: the data
    :param outi: the massage writer
    """
    n = len(stud)
    for i in range(0, n):
        outi.afis(i, stud)

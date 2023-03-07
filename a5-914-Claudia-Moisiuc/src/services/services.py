def test(f):
    """
    Here we test the non-ui functions
    """
    s = []
    from src.domain.domain import Student
    si = Student(0, '0', 0)
    s.append(si)
    s.append(si)
    s[0]._id = 10092
    s[0].name = 'Alesia'
    s[0].group = 101
    s[1]._id = 10023
    s[1].name = 'Ana'
    s[1].group = 102
    f.filteri(s, 101)
    assert s[0]._id == 10023
    assert s[0].name == 'Ana'
    assert s[0].group == 102
    e = []
    from src.domain.domain import Student
    ei = Student(0, '0', 0)
    e.append(ei)
    e[0]._id = 10012
    e[0].name = 'Alesia'
    e[0].group = 103
    s = f.copy_in(s, e, f)
    assert s[0]._id == 10012
    assert s[0].name == 'Alesia'
    assert s[0].group == 103


class Service:

    def getter_id(self, stud, i):
        return stud[i]._id

    def getter_name(self, stud, i):
        return stud[i].name

    def getter_group(self, stud, i):
        return stud[i].group

    def auto_set(self, stud):
        """
        the function auto-sets 10 random student data
        :param stud:the list of data
        """
        for i in range(0,10):
            from src.domain.domain import Student
            studi = Student(0, '0', 0)
            stud.append(studi)
            stud[i]._id = stud[i].rand_id(stud)
            stud[i].name = stud[i].rand_nm()
            stud[i].group = stud[i].rand_gr()

    def id_inv(self, stud, idi, f):
        """
        the funstion tests if the id is uique
        :param stud: the list
        :param idi: the id
        :return: 0 if it is not unigue and 1 if it is unique
        """
        n = len(stud)
        for i in range(0,n):
            #print(stud[i].id, idi)
            if f.getter_id(stud, i) == idi:
                return 0
        return 1

    def add(self, stud, outi, f):
        """
        the function adds the student data
        :param stud: the data
        :param outi: the message variable
        """
        ok = True
        while ok:
            idi = int(input('ID =  '))
            if f.id_inv(stud, idi, f) == 0:
                outi.inv()
            else:
                ok = False
        nam = input('name = ')
        ok = True
        while ok:
            grp = int(input('group number = '))
            if grp < 100 or grp > 107:
                outi.inv()
            else:
                ok = False
        from src.domain.domain import Student
        studi = Student(idi, nam, grp)
        stud.append(studi)

    def filteri(self, stud, grp):
        """
        eliminates the students from an inputted group
        :param stud:the data
        :param grp:the group
        """
        n = len(stud)
        i = 0
        while i < n:
            if stud[i].group == grp:
                del stud[i]
                n = n - 1
            else:
                i = i + 1

    def copy_in(self, stud, elim, f):
        """
        the functions forms a list with the data from the stud
        :param stud: the data
        :param elim: the other list
        :return: the new data
        """
        t = []
        n = len(stud)
        for i in range(0, n):
            r = [0, '0', 0]
            t.append(r)
            t[i][0] = f.getter_id(stud, i)
            t[i][1] = f.getter_name(stud, i)
            t[i][2] = f.getter_group(stud, i)
        elim.append(t)
        return elim

    def undo(self, stud, elim, outi):
        """
        the unoes the last operation that changed the data
        :param stud: the data
        :param elim: the old lists
        :param outi: the massage variable
        """
        if len(elim) == 0:
            outi.no_more()
            return 0
        else:
            n = len(elim[-1])
            while len(stud) != 0:
                del stud[0]
            for i in range(0,n):
                idd = elim[-1][i][0]
                na = elim[-1][i][1]
                g = elim[-1][i][2]
                from src.domain.domain import Student
                studi = Student(idd, na, g)
                stud.append(studi)
            del elim[-1]

    def menu(self, stud, elim, outi, f):
        """
        the function is the menu reader
        :param stud: the data
        :param elim: the old lists
        :param outi: the massage variable
        """
        ok = True
        while ok:
            op = input('option:  ')
            if op == 'add':
                elim = f.copy_in(stud, elim ,f)
                f.add(stud, outi, f)
            elif op == 'list':
                from src.ui.ui import afis
                afis(stud, outi)
            elif op == 'filter':
                elim = f.copy_in (stud, elim, f)
                oki = True
                while oki:
                    grp = int(input('group number = '))
                    if grp < 100 or grp > 107:
                        stud[0].inv()
                    else:
                        oki = False
                f.filteri(stud, grp)
            elif op == 'undo':
                f.undo(stud, elim, outi)
            elif op == 'leave':
                ok = False
            else:
                outi.inv()

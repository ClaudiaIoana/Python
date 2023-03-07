from datetime import date

from src.domain.assignment import Assignment
from src.domain.student import Student
from src.domain.validators import WrongInputError, AvailabilityError, UniqueError
from src.services.undo_redo_services import UndoObject


class UI:
    def __init__(self, student_service, assignment_service, grade_service, statistic_service, undo_service):
        self.__student_service = student_service
        self.__assignment_service = assignment_service
        self.__grade_service = grade_service
        self.__statistic_service = statistic_service
        self.__undo_service = undo_service
        self.__dict_ui_op = {
            "s": {"a": self.ui_add_student,
                  "r": self.ui_remove_student,
                  "u": self.ui_update_student,
                  "l": self.ui_list_student
                  },
            "a": {"a": self.ui_add_assignment,
                  "r": self.ui_remove_assignment,
                  "u": self.ui_update_assignment,
                  "l": self.ui_list_assignment
                  },
            "g": {"l": self.ui_list_grade,
                  "g": self.ui_give_sa,
                  "gr": self.grading
                  },
            "st": {"sa": self.ui_stud_assi,
                   "l": self.ui_late,
                   "m": self.ui_med
                   },
            "u": {"u": self.ui_undo,
                  "r": self.ui_redo
                  },
            "stop": {"stop": self.stop}
        }

    def start(self):
        '''The function searches for the errors in the imputed data. '''
        self.menu()
        ok = True
        while ok == True:
            try:
                service = input("Enter a service: ").lower().strip()
                option = input("Enter a command: ").lower().strip()

                if service not in self.__dict_ui_op:
                    raise WrongInputError("*The input is not valid.*")

                self.__dict_ui_op[service][option]()

            except AvailabilityError as a:
                print(a)
            except UniqueError as u:
                print(u)
            except WrongInputError as w:
                print(w)

    def menu(self):
        op = """Options available:
        SERVICE 1: Student
        OPTIONS: (a) add
                 (r) remove
                 (u) update
                 (l) list

        SERVICE 2: Assignment
        OPTIONS: (a) add
                 (r) remove
                 (u) update
                 (l) list

        SERVICE 3: Grade
        OPTIONS: (l) list
                 (g) give an assignment to a student
                 (gr) grade

        SERVICE 4: Statistics
        OPTIONS: (sa) All students who have a graded assignment, ordered descending by grade.
                 (l) late assignment
                 (m) students in descending order of the average grade received

        SERVICE 5: Undo and redo
        OPTIONS: (u) undo
                 (r) redo

        SERVICE 6: Stop
        OPTIONS: (stop) stop the program
        """
        print(op)

    def ui_add_student(self):
        '''The function adds a student. '''
        idd = int(input("ID =  ").strip())
        name = input("Name =  ").strip()
        group = int(input("Group =  ").strip())
        self.__undo_service.register_operation(UndoObject(lambda: self.__student_service.remove(idd),
                                                          lambda: self.__student_service.add(idd, name, group)))
        self.__student_service.add(idd, name, group)

    def ui_remove_student(self):
        '''The function removes a student. '''
        idd = int(input("ID =  ").strip())
        student = None
        for ids in self.__student_service.database:
            if idd == self.__student_service.database[ids].id:
                nm = self.__student_service.database[ids].name
                g = self.__student_service.database[ids].group
                student = Student(idd, nm, g)

        if not student:
            raise UniqueError("No student with given id")
        grades = list(filter(lambda x: x.student_id == idd, self.__grade_service.database))

        def undo_function():
            self.__student_service.add(idd, nm, g)
            for grade in grades:
                self.__grade_service.add(grade.assign_id, idd, grade.grade)

        def redo_function():
            self.__student_service.remove(idd)
            self.__grade_service.removes(idd)

        self.__undo_service.register_operation(UndoObject(undo_function, redo_function))
        self.__student_service.remove(idd)
        self.__grade_service.removes(idd)

    def ui_update_student(self):
        '''The function updates a student. '''
        idd = int(input("ID =  ").strip())
        op = '''What do you want to update?
        (n) the name
        (g) the group
        (b) both
        '''
        print(op)
        option = input("option =  ").strip()
        student = None
        for ids in self.__student_service.database:
            if idd == self.__student_service.database[ids].id:
                nm = self.__student_service.database[ids].name
                g = self.__student_service.database[ids].group
                student = Student(idd, nm, g)
                idss = ids

        if not student:
            raise UniqueError("No student with given id")
        if option == 'n':
            new = input('New name:  ').strip()
            old_name = self.__student_service.database[idss].name
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__student_service.update(idd, old_name, None),
                           lambda: self.__student_service.update(idd, new, None))
                )
            self.__student_service.update(idd, new, None)
        elif option == 'g':
            new = int(input('New group:  ').strip())
            old = self.__student_service.database[idss].group
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__student_service.update(idd, None, old),
                           lambda: self.__student_service.update(idd, None, new))
            )
            self.__student_service.update(idd, None, new)
        else:
            new1 = input('New name:  ').strip()
            new2 = int(input('New group:  ').strip())
            old1 = self.__student_service.database[idss].name
            old2 = self.__student_service.database[idss].group
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__student_service.update(idd, old1, old2),
                           lambda: self.__student_service.update(idd, new1, new2))
            )
            self.__student_service.update(idd, new1, new2)

    def ui_list_student(self):
        '''The function lists a student. '''
        database = self.__student_service.database
        for ids in database:
            print(database[ids].id, '  ', database[ids].name, '  ', database[ids].group)

    def ui_add_assignment(self):
        '''The function adds an assignment. '''
        idd = int(input("ID assignment =  ").strip())
        desc = input('description =  ')
        d = input('deadline =  ')
        y = d.split()
        deadline = date(int(y[0]), int(y[1]), int(y[2]))
        self.__undo_service.register_operation(UndoObject(lambda: self.__assignment_service.remove(idd),
                                                          lambda: self.__assignment_service.add(idd, desc, deadline)))
        self.__assignment_service.add(idd, desc, deadline)

    def ui_remove_assignment(self):
        '''The function removes an assignment. '''
        idd = int(input("ID assignment =  ").strip())
        assi = None
        for ids in self.__assignment_service.database:
            if idd == self.__assignment_service.database[ids].id:
                ds = self.__assignment_service.database[ids].description
                d = self.__assignment_service.database[ids].deadline
                assi = Assignment(idd, ds, d)

        if not assi:
            raise UniqueError("No assignment with given id")
        grades = list(filter(lambda x: x.assign_id == idd, self.__grade_service.database))

        def undo_function():
            self.__assignment_service.add(idd, ds, d)
            for grade in grades:
                self.__grade_service.add(idd, grade.student_id, grade.grade)

        def redo_function():
            self.__assignment_service.remove(idd)
            self.__grade_service.remove(idd)

        self.__undo_service.register_operation(UndoObject(undo_function, redo_function))
        self.__assignment_service.remove(idd)
        self.__grade_service.remove(idd)

    def ui_update_assignment(self):
        '''The function updates an assignment. '''
        idd = int(input("ID assignment =  ").strip())
        op = '''What do you want to update?
        (d) the description
        (dl) the deadline
        (b) both
        '''
        print(op)
        option = input("option =  ").strip()
        assi = None
        for ids in self.__assignment_service.database:
            if idd == self.__assignment_service.database[ids].id:
                ds = self.__assignment_service.database[ids].description
                d = self.__assignment_service.database[ids].deadline
                assi = Assignment(idd, ds, d)
                idss = ids

        if not assi:
            raise UniqueError("No assignment with given id")

        if option == 'd':
            new = input('New description:  ').strip()
            old = self.__assignment_service.database[idss].description
            self.__undo_service.register_operation(UndoObject(lambda: self.__assignment_service.update(idd, old, None),
                                                              lambda: self.__assignment_service.update(idd, new, None)))
            self.__assignment_service.update(idd, new, None)
        elif option == 'dl':
            x = input('New deadline:  ').strip()
            y = x.split()
            new = date(int(y[0]), int(y[1]), int(y[2]))
            old = self.__assignment_service.database[idss].deadline
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__assignment_service.update(idd, None, old),
                           lambda: self.__assignment_service.update(idd, None, new)))
            self.__assignment_service.update(idd, None, new)
        else:
            new1 = input('New description:  ').strip()
            x = input('New deadline:  ').strip()
            y = x.split()
            new2 = date(int(y[0]), int(y[1]), int(y[2]))
            old1 = self.__assignment_service.database[idss].description
            old2 = self.__assignment_service.database[idss].deadline
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__assignment_service.update(idd, old1, old2),
                           lambda: self.__assignment_service.update(idd, new1, new2))
            )
            self.__assignment_service.update(idd, new1, new2)

    def ui_list_assignment(self):
        '''The function lists the assignments. '''
        database = self.__assignment_service.database
        for ids in database:
            print(database[ids].id, ',', database[ids].description, ',', database[ids].deadline)

    def ui_list_grade(self):
        '''The function lists the grades. '''
        database = self.__grade_service.database
        n = len(self.__grade_service.database)
        for ids in range(0, n):
            print(database[ids].assign_id, '  ', database[ids].student_id, '  ', database[ids].grade)

    def ui_give_sa(self):
        '''The function gives assignments to students. '''
        op = '''
        (n) n students
        (g) a group
        '''
        print(op)
        l = []
        option = input('What option?  ')
        data = self.__student_service.database
        if option == 'n':
            ida = int(input('ID assignment  '))
            self.__assignment_service.verify_existence(ida)
            n = int(input('How many? '))
            for i in range(0, n):
                iddd = int(input('ID student  '))
                self.__student_service.verify_existence(iddd)
                ir = iddd
                l.append(ir)
                self.__grade_service.add(ida, iddd, None)
            self.__undo_service.register_operation(UndoObject(lambda: self.__grade_service.remov(l, ida),
                                                              lambda: self.__grade_service.ad(l, ida)))
        else:
            ida = int(input('ID assignment  '))
            self.__assignment_service.verify_existence(ida)
            n = int(int(input('Group number?  ')))
            for idd in data:
                if data[idd].group == n:
                    ir = idd
                    l.append(ir)
                    self.__grade_service.add(ida, data[idd].id, None)
            self.__undo_service.register_operation(UndoObject(lambda: self.__grade_service.remov(l, ida),
                                                              lambda: self.__grade_service.ad(l, ida)))

    def stop(self):
        exit()

    def grading(self):
        '''The function grades a student'''
        database = self.__grade_service.database
        sid = int(input('ID student  '))
        self.__grade_service.verify_existence(sid)
        n = len(self.__grade_service.database)
        print('Assignments for grading ')
        for ids in range(0, n):
            if database[ids].student_id == sid:
                print(database[ids].assign_id)
        asi = int(input('ID assignment  '))
        self.__grade_service.verify_unique(sid, asi)
        gr = int(input('Grade   '))
        self.__undo_service.register_operation(UndoObject(lambda: self.__grade_service.give_grade(sid, asi, None),
                                                          lambda: self.__grade_service.give_grade(sid, asi, gr)))
        self.__grade_service.give_grade(sid, asi, gr)

    def ui_stud_assi(self):
        '''The program displays a statistic'''
        idd = int(input('ID assignment  '))
        l = self.__statistic_service.desc_order(idd)
        n = len(l)
        for i in range(0, n):
            print(l[i][0], l[i][1])

    def ui_late(self):
        '''The program displays a statistic'''
        l = self.__statistic_service.list_assi()
        print(l)

    def ui_med(self):
        '''The program displays a statistic'''
        l = self.__statistic_service.med_order()
        n = len(l)
        for i in range(0, n):
            print(l[i][0], l[i][1])

    def ui_undo(self):
        try:
            self.__undo_service.undo()
            print("Operation successfully undone!")
        except Exception as e:
            print(e)

    def ui_redo(self):
        try:
            self.__undo_service.redo()
            print("Operation successfully undone!")
        except Exception as e:
            print(e)
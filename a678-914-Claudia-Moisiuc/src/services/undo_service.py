from src.domain.validators import UndoBounds


class UndoObject:
    def __init__(self, undo_function, redo_function):
        """
        Object which will be inserted in the undo stack in service
        :param undo_function: function that calls the undo operation
        :param redo_function: function that calls the redo operation
        """
        self.undo_function = undo_function
        self.redo_function = redo_function


class UndoService:
    def __init__(self, student_repo, assignment_repo, grade_repo):
        """
        Service class which maintains the undo and redo operations for student, discipline and grade repos
        :param student_repo: StudentRepo
        :param assignment_repo: AssignmentRepo
        :param grade_repo: GradeRepo
        """
        self._student_repo = student_repo
        self._assignment_repo = assignment_repo
        self._grade_repo = grade_repo
        self._undo_stack = []
        self._undo_pointer = 0

    def register_operation(self, operation):
        """
        Registers the operation and pushes it onto the stack
        """
        self._normalise_stack()
        self._undo_stack.append(operation)
        self._undo_pointer += 1

    def _normalise_stack(self):
        """
        When an operation is executed that is not undo or redo everything beyond self._undo_pointer has to be
        eliminated from the stack. This is what the function does
        :return: None
        """
        while len(self._undo_stack) != self._undo_pointer:
            self._undo_stack.pop()

    def undo(self):
        """
        Undoes the last performed operation
        :return: None
        """
        if self._undo_pointer == 0:
            raise UndoBounds("No operations to undo")
        self._undo_pointer -= 1
        self._undo_stack[self._undo_pointer].undo_function()

    def redo(self):
        """
        Redoes the last undone operation
        :return: None
        """
        if self._undo_pointer == len(self._undo_stack):
            raise UndoBounds("No operations to redo")
        self._undo_stack[self._undo_pointer].redo_function()
        self._undo_pointer += 1

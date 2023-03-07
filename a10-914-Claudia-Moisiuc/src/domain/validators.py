
class UniqueError(Exception):
    pass


class AvailabilityError(Exception):
    pass


class WrongInputError(Exception):
    pass


class PastDeadlineError(Exception):
    pass


class GradedError(Exception):
    pass


class UndoBounds(Exception):
    pass


class TestValidator:
    @staticmethod
    def validate(test):
        return True
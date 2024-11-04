class WrongIdError(Exception):
    """
    Исключение, при вводе ID не числом
    """

    def __init__(self):
        self.message = "Error: ID should be a digit"


class NotExistingId(Exception):
    """
    Исключение возникает, когда введеное ID не существует
    """

    def __init__(self):
        self.message = "Error: ID does not exist"

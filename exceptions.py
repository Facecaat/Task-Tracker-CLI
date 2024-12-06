class FileDoesNotExist(Exception):
    '''
    Исключение срабатывает, когда вводится имя файла, который не существует
    '''
    def __init__(self):
        self.message = "Error. That file does not exist"
        super().__init__(self.message)

class FileAlreadyExist(Exception):
    '''
    Исключение срабатывает, когда вводится имя файла, который уже существует
    '''
    def __init__(self):
        self.message = "Error. That filename already exists"
        super().__init__(self.message)

class UnknownCommand(Exception):
    '''
    Исключение срабатывает, когда вводится несуществующая команда
    '''
    def __init__(self):
        self.message = ("Error. Unknown command.\n"
                        "If you want to see commands, write \"commands\"")
        super().__init__(self.message)

class WrongId(Exception):
    '''
    Исключение срабатывает, когда вводится неверный id
    '''
    def __init__(self):
        self.message = "Error. That ID does not exist"
        super().__init__(self.message)
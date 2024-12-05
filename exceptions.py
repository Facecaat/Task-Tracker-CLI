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
        self.message = ("Error. That filename already exists")
        super().__init__(self.message)

        #todo добавь общие ексепшены в run, а так же ексепшены на все функции



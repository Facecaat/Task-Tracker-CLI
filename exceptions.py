class FileDoesNotExist(Exception):
    '''
    Исключение срабатывает тогда, когда вводится имя файла, который не существует
    '''
    def __init__(self):
        self.message = "Error. That file does not exist"
        super().__init__(self.message)



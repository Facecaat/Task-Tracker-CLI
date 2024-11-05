class FileDoesNotExist(Exception):
    def __init__(self):
        self.message = "Error. That file does not exist"
        super().__init__(self.message)



class FileHelper:
    def __init__(self, path):
        self.path = path
        self.file_exists = self.check_file_exists()

    def check_file_exists(self):
        try:
            with open(self.path, 'r'):
                return True
        except FileNotFoundError:
            return False

    def create_file(self):
        if not self.file_exists:
            with open(self.path, 'w'):
                pass
            self.file_exists = True

    def read(self):
        if not self.file_exists:
            return "File does not exist."

        with open(self.path, 'r') as file:
            content = file.read()
        return content

    def write(self, text):
        self.create_file()

        with open(self.path, 'w') as file:
            file.write(text)

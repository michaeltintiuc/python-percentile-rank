class FileHandler():
    """
    Calculate percentile rank based on index
    """

    FILE_TYPES = ['csv', 'json', 'yaml', 'auto']

    input_file = None
    output_file = None
    file_type = ""
    data = ""

    def __init__(self, input_file, output_file, file_type):
        self.input_file = input_file
        self.output_file = output_file
        self.file_type = file_type

    def write(self):
        self.data = self.input_file.read()
        self.output_file.write(self.data + "\nchanged!")

        self.input_file.close()
        self.output_file.close()

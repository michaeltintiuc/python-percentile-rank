from argparse import ArgumentTypeError


class FileHandler(object):
    """
    Handle file I/O
    """

    FILE_TYPES = ['csv', 'json', 'yaml', 'auto']

    type_handler = {}
    input_file = None
    output_file = None
    file_type = ""
    data = []

    def __init__(self, input_file, output_file, file_type):
        self.input_file = input_file
        self.output_file = output_file
        self.file_type = self.setFileType(file_type)
        self.type_handler = self.setTypeHandler()

    def readDataFromFile(self):
        self.data = self.type_handler['read'](self.input_file)

    def writeDatatoFile(self, skip_index):
        if skip_index is not None:
            self.skipIndex(skip_index)

        self.type_handler['write'](self.data, self.output_file)

    def skipIndex(self, skip_index):
        for item in self.data:
            try:
                del item[skip_index]
            except (KeyError, TypeError):
                pass

    def setFileType(self, file_type):
        if file_type == 'auto':
            try:
                return self.input_file.name.split('.')[1]
            except IndexError:
                raise ValueError('Could not determine file type')

        return file_type

    def setTypeHandler(self):
        return {
            'json': self.jsonHandler,
            'yaml': self.yamlHandler,
            'csv': self.csvHandler
        }[self.file_type]()

    def jsonHandler(self):
        import json
        return {
            'read': lambda file: json.load(file),
            'write': lambda data, file: json.dump(data, file)
        }

    def yamlHandler(self):
        import yaml
        return {
            'read': lambda file: yaml.load(file),
            'write': lambda data, file: yaml.safe_dump(
                data, file, allow_unicode=True, default_flow_style=False)
        }

    def csvHandler(self):
        import csv
        return {
            'read': lambda file: [row for row in csv.reader(
                                  file, skipinitialspace=True)],
            'write': lambda data, file: csv.writer(file).writerows(data)
        }

    @staticmethod
    def parse_file_types(file_type):
        if file_type.lower() not in FileHandler.FILE_TYPES:
            msg = 'File type "%s" not supported' % file_type
            raise ArgumentTypeError(msg)

        return file_type

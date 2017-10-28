from argparse import ArgumentTypeError
from abc import ABCMeta, abstractmethod


class FileHandler(object):
    """
    Calculate percentile rank based on index
    """

    __metaclass__ = ABCMeta

    FILE_TYPES = ['csv', 'json', 'yaml', 'auto']

    input_file = None
    output_file = None
    data = ""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = self.loadFileData()

    @abstractmethod
    def loadFileData(self):
        pass

    @abstractmethod
    def writeDatatoFile(self, skip_index):
        pass

    def exportFile(self, skip_index=None):
        if skip_index is not None:
            self.skipIndex(skip_index)

        self.writeDatatoFile()

    def skipIndex(self, skip_index):
        for item in self.data:
            try:
                del item[skip_index]
            except KeyError:
                pass

    @staticmethod
    def make(input_file, output_file, file_type):
        if file_type == 'auto':
            try:
                file_type = input_file.name.split('.')[1]
            except IndexError:
                raise ValueError('Could not determine file type')

        if file_type == 'json':
            from json_handler import JsonHandler
            return JsonHandler(input_file, output_file)
        elif file_type == 'csv':
            pass
        elif file_type == 'yaml':
            pass

    @staticmethod
    def parse_file_types(file_type):
        if file_type.lower() not in FileHandler.FILE_TYPES:
            msg = 'File type "%s" not supported' % file_type
            raise ArgumentTypeError(msg)

        return file_type

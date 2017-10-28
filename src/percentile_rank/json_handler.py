import json
from file_handler import FileHandler


class JsonHandler(FileHandler):
    """
    Handle JSON read/write
    """

    def loadFileData(self):
        return json.load(self.input_file)

    def writeDatatoFile(self):
        json.dump(self.data, self.output_file)

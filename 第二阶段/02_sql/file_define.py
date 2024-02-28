import json

from data_record import Record


class FileReader:
    def read_file(self) -> list[Record]:
        """读取文件中的数据，并将其每一条转化为Record对象，把它们都封装到List中返回"""
        pass


class CsvFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件的路径
        self.my_encoding = "utf-8"

    @classmethod
    def init_sec(cls, path, encoding):
        cls.my_encoding = encoding
        return cls(path)

    def read_file(self) -> list[Record]:
        f = open(self.path, 'r', encoding=self.my_encoding)
        result = []
        for line in f.readlines():
            line = line.strip()
            element = line.split(",")
            result.append(Record(element[0], element[1], element[2], element[3]))
        return result


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path
        self.my_encoding = "utf-8"

    @classmethod
    def init_sec(cls, path, encoding):
        cls.path = path
        cls.my_encoding = encoding

    def read_file(self):
        result = []
        data_lines = open(self.path, 'r', encoding=self.my_encoding).readlines()
        for line in data_lines:
            data = json.loads(line)
            result.append(Record(data["date"], data["order_id"], data["money"], data["province"]))
        return result


if __name__ == '__main__':
    reader = CsvFileReader.init_sec("2011年1月销售数据.txt", "utf-8")
    for data in reader.read_file():
        print(data)

    reader = JsonFileReader("2011年2月销售数据JSON.txt")
    for data in reader.read_file():
        print(data)

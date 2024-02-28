from dao import DataRecordDao
from file_define import CsvFileReader, JsonFileReader


jan_data = CsvFileReader("2011年1月销售数据.txt").read_file()
feb_data = JsonFileReader("2011年2月销售数据JSON.txt").read_file()
all_data = jan_data + feb_data

dao = DataRecordDao()
for data in all_data:
    dao.insert(data)

for data in dao.selectAll():
    print(data)


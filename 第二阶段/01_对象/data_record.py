"""
数据定义类
"""


class Record:

    def __init__(self, date, order_id, sale_volume, province):
        self.date = date
        self.order_id = order_id
        self.sale_volume = sale_volume
        self.province = province

    def __str__(self):
        return f"date: {self.date}, order_id: {self.order_id}, sale_volume: {self.sale_volume}, province: {self.province}"
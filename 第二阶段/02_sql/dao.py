from data_record import Record
from pymysql import Connection


class Dao:
    def insert(self, info):
        pass

    def delete(self, info):
        pass

    def update(self, info):
        pass

    def selectAll(self):
        pass

    def selectOne(self, info):
        pass


class DataRecordDao(Dao):
    def __init__(self):
        self.connection = Connection(
            host='localhost',
            port=3306,
            user='root',
            password='000000',
            autocommit=True
        )
        self.cursor = self.connection.cursor()

        self.db_name = 'test'
        self.table_name = 'sale_volume'
        self.connection.select_db(self.db_name)

    def insert(self, record):
        return self.cursor.execute(f"insert into {self.table_name}"
                            f"(sv_date,sv_order_id,sv_money,sv_province) "
                            f"values "
                            f"('{record.date}','{record.order_id}','{record.sale_volume}','{record.province}')")

    def delete(self, record):
        return self.cursor.execute(f"delete from {self.table_name} where sv_date <= '{record.date}'")

    def update(self, record):
        return self.cursor.execute(f"update {self.table_name} set sv_sale_volume = '{record.sale_volume}'"
                                   f",sv_province = '{record.province}' where sv_order_id = '{record.order_id}'")

    def selectAll(self):
        self.cursor.execute(f"select sv_date,sv_order_id,sv_money,sv_province from {self.table_name}")
        return self.cursor.fetchall()

    def selectOne(self, record):
        self.cursor.execute(f"select sv_date,sv_order_id,sv_money,sv_province from {self.table_name} "
                            f"where sv_order_id = '{record.order_id}'")
        return self.cursor.fetchone()

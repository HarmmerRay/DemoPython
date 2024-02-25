class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g通话")


class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_NFC(self):
        print("读出NFC卡")

    def write_NFC(self):
        print("写入NFC卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


# tip: 从左到右，谁先继承谁的变量优先级高
class Phone2024(Phone, NFCReader, RemoteControl):
    face_id = "1----"

    def call_by_5g(self):
        print("5G通话")


class Phone2025(Phone2024, NFCReader, RemoteControl):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print(f"Phone2024的厂商{Phone2024.producer}")
        super().call_by_4g()
        print("开启CPU单核模式，确保通话的时候省电")
        print("使用5G网络进行通话")
        print("关闭CPU单核模式，确保性能")


phone = Phone2024()
print(phone.producer)
print(phone.IMEI)
print(phone.face_id)
phone.call_by_4g()
phone.call_by_5g()
phone.read_NFC()
phone.write_NFC()
phone.control()

phone2 = Phone2025()
phone2.call_by_5g()

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "000999"
clock1.price = 19.99
print(f"闹钟ID:{clock1.id},闹钟价格:{clock1.price}")
clock1.ring()

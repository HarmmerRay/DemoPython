class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_udlr(self):
        """上下左右摇摆"""
        pass


class MideaAC(AC):
    def cool_wind(self):
        print("美的空调核心制冷技术")

    def hot_wind(self):
        print("美的空调核心制热技术")

    def swing_udlr(self):
        print("美的空调无风感上下左右摆风技术")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频省电制冷")

    def hot_wind(self):
        print("格力空调变频省电制热")

    def swing_udlr(self):
        print("格力空调静音上下左右摆风技术")


def cool_wind(ac: AC):
    ac.cool_wind()


midea_ac = MideaAC()
gree_ac = GREE_AC()
cool_wind(midea_ac)
cool_wind(gree_ac)

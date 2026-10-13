class Chess:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        # 先处理公共逻辑
        if self.moveRule(x, y):
            self.x = x
            self.y = y

    # 父类不知道具体的移动规则
    def moveRule(self, x, y):
        pass


class HorseRule(Chess):
    def __init__(self, x, y):
        super().__init__(x, y)

    def moveRule(x, y):
        # 子类编写移动规则
        pass

h = HorseRule(3, 5)
h.move(10, 20)
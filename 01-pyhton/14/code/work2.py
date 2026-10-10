class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def celsius(self):
        return self.temperature

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        elif value > 1000:
            raise ValueError("温度不能超过1000")
        self.temperature = value

    @property
    def fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    @property
    def kelvin(self):
        return self.temperature + 273.15


t = Temperature(25)
print(t.celsius)  # 25
print(t.fahrenheit)  # 77.0（只读属性，自动计算）
print(t.kelvin)  # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度

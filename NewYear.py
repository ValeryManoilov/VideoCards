class Vehicle:
    def __init__(self, year = None, price =None):
        self._year = year
        self._price = price

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def set_price(self, price):
        self._price = price

    def get_capacity(self):
        return self._price

    def info(self):
        print(f'Цена: {self._price}\nГод выпуска: {self._year}\n')


class VideoCard(Vehicle):
    def __init__(self, mark = None, model = None, cooler_count = None):
        super().__init__()
        self.__mark = mark
        self.__model = model
        self.__cooler_count = cooler_count

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_cooler_count(self, cooler_count):
        self.__cooler_count = cooler_count

    def get_cooler_count(self):
        return self.__cooler_count

    def info(self):
        print(f'Производитель: {self.__mark}\nМодель: {self.__model}\nКоличество кулеров: {self.__cooler_count}')
        super().info()

# NVidia GeForseRTX3060Ti
VideoCard1 = VideoCard()
VideoCard1.set_year(2020)
VideoCard1.set_price('40.000 рублей')
VideoCard1.set_mark('MSI')
VideoCard1.set_model('NVidia GeForseRTX3060Ti')
VideoCard1.set_cooler_count(2)
VideoCard1.info()
# NVidia GeForseRTX4090
VideoCard2 = VideoCard()
VideoCard2.set_year(2022)
VideoCard2.set_price('Твоя душа')
VideoCard2.set_mark('MSI')
VideoCard2.set_model('NVidia GeForseRTX4090')
VideoCard2.set_cooler_count(3)
VideoCard2.info()

# AMD RadeonRX6650XT
VideoCard3 = VideoCard()
VideoCard3.set_year(2022)
VideoCard3.set_price('30.000 рублей')
VideoCard3.set_mark('Asus')
VideoCard3.set_model('AMD Radeon RX 6650XT')
VideoCard3.set_cooler_count(2)
VideoCard3.info()

# AMD RadeonRX6650XT
VideoCard4 = VideoCard()
VideoCard4.set_year(2021)
VideoCard4.set_price('40.000 рублей')
VideoCard4.set_mark('GIGABYTE')
VideoCard4.set_model('AMD Radeon RX 6650XT')
VideoCard4.set_cooler_count(3)
VideoCard4.info()
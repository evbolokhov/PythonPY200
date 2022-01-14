# TODO Добавить методы add_water и remove_water
from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)
    @staticmethod
    def __check_capacity_volume(value) -> Union[int, float]:
        """
        :param value:
        :return:
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value
    @staticmethod
    def __check_occupied_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value
    @staticmethod
    def __check_overflow(capacity, occupied):
        if (capacity < occupied) or (occupied < 0):
            raise ValueError
    def get_capacity_volume(self) -> Union[int, float]:
        """
        Функция возвращает объём стакана
        :return: значение объёма стакана
        """
        return self.__capacity_volume
    def get_occupied_volume(self) -> Union[int, float]:
        """
        Функция возвращает занятый объём стакана
        :return: значение занятого объёма стакана
        """
        return self.__occupied_volume
    def add_water(self, value: Union[int, float]) -> None:
        self.__check_occupied_volume(value)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume + value)
        self.__occupied_volume += value
    def remove_water(self, value: Union[int, float]) -> None:
        self.__check_occupied_volume(value)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume - value)
        self.__occupied_volume -= value


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())
    glass1.add_water(100)
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())
    glass1.remove_water(101)
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())


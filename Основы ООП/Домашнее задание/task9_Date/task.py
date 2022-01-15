class Date:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.occupied_volume = self.__check_occupied_volume(occupied_volume)
        # self.__check_overflow(self.capacity_volume, self.occupied_volume)
        self.__check_overflow()

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




# TODO class Date
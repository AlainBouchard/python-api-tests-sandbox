from src.contracts.AbstractResponse import AbstractResponse


class UsersIdResponse(AbstractResponse):
    def __init__(self):
        super().__init__()
        self.__data = None
        self.__support = None

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def support(self) -> dict:
        return self.__support

    def update(self, data: dict, support: dict) -> "UsersIdResponse":
        self.__data = data
        self.__support = support

        return self

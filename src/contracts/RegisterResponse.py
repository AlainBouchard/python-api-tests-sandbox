from requests import Response
from src.contracts.AbstractResponse import AbstractResponse


class RegisterResponse(AbstractResponse):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__token = None

    @property
    def response(self) -> Response:
        return self._response

    def update(self, id: str, token: str) -> "RegisterResponse":
        self.__id = id
        self.__token = token

        return self

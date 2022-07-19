import json
import logging
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

    def load(self, response: Response) -> "RegisterResponse":
        try:
            args = json.loads(response.text)
            self.update(**args)
        except TypeError as e:
            logging.info(f"Could not load update the data: {e}")
        finally:
            self._response = response

        return self

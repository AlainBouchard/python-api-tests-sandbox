import json
import logging
from abc import ABC, abstractmethod
from requests import Response


class AbstractResponse(ABC):
    def __init__(self):
        self._response = None

    @property
    def response(self) -> Response:
        return self._response

    @abstractmethod
    def update(self, **kwargs) -> "AbstractResponse":
        pass

    def load(self, response: Response) -> "AbstractResponse":
        try:
            args = json.loads(response.text)
            self.update(**args)
        except TypeError as e:
            logging.info(f"Could not load update the data: {e}")
        finally:
            self._response = response

        return self

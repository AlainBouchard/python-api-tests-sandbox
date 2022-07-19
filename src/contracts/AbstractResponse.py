import json
import logging
from abc import ABC, abstractmethod
from requests import Response


class AbstractResponse(ABC):
    """
    Abstract Class for the REST APIs Request contacts.
    """
    def __init__(self):
        self._response = None

    @property
    def response(self) -> Response:
        return self._response

    @abstractmethod
    def update(self, **kwargs) -> "AbstractResponse":
        """
        Needed method to create an object from the contract. To be implemented by the child class.
        This method will be used to create an object with Requests Response body values.
        :param kwargs: the Response body values (e.g., JSON formatted)
        :return: the child class should return "self"
        """
        pass

    def load(self, response: Response) -> "AbstractResponse":
        """
        Used to load an API Response using the contract.
        :param response: The Requests.Response object as received from the API using Requests methods.
        :return: the child class should return "self"
        """
        try:
            args = json.loads(response.text)
            self.update(**args)
        except TypeError as e:
            logging.info(f"Could not load data: {e}")
        finally:
            self._response = response

        return self

from abc import ABC, abstractmethod
from faker import Faker


Faker.seed(0)


class AbstractRequest(ABC):
    """
    Abstract Class for the REST APIs Request contacts.
    """
    def __init__(self):
        self._faker = Faker(locale="en_US")

    @property
    def faker(self):
        return self._faker

    @abstractmethod
    def create(self, **kvargs) -> "AbstractRequest":
        """
        Needed method to create an object from the contract. To be implemented by the child class.
        This method will be used to create an object from a list of keys/values.
        :param kvargs: keys/values information.
        :return: the child class should return "self"
        """
        pass

    @abstractmethod
    def fake_data(self) -> "AbstractRequest":
        """
        Needed method to create an object from the contract. To be implemented by the child class.
        This method will be used to randomly generate an object of the child class.
        :return: the child class should return "self"
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Needed method to return an object attribute values. To be implemented by the child class.
        :return: a dictionary that contain the object attributes as defined by the API contract.
        """
        pass

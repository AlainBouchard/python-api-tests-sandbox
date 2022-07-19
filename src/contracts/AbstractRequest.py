from abc import ABC, abstractmethod
import logging
from faker import Faker


Faker.seed(0)
logging.error("############### bang bang! #################")


class AbstractRequest(ABC):
    def __init__(self):
        self._faker = Faker(locale="en_US")

    @property
    def faker(self):
        return self._faker

    @abstractmethod
    def create(self, email: str, password: str) -> "AbstractRequest":
        pass

    @abstractmethod
    def fake_data(self) -> "AbstractRequest":
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

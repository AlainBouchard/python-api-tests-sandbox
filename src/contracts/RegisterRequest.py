import random
from src.contracts.AbstractRequest import AbstractRequest


class RegisterRequest(AbstractRequest):
    """
    Contract for the Register endpoint when used with a request.
    """
    def __init__(self):
        super().__init__()
        self.__email = None
        self.__password = None

    def create(self, email: str, password: str) -> "RegisterRequest":
        self.__email = email
        self.__password = password

        return self

    def fake_data(self) -> "RegisterRequest":
        # For this exercise, reqres.in has a defined set of test users, and any other value is bad.
        users = ["michael.lawson@reqres.in", "lindsay.ferguson@reqres.in",  "tobias.funke@reqres.in"]
        self.create(email=random.choice(users), password=super().faker.password(length=12))

        return self

    def to_dict(self) -> dict:
        return {
            "email": self.__email,
            "password": self.__password
        }

from src.contracts.AbstractResponse import AbstractResponse


class UsersResponse(AbstractResponse):
    """
    Contract for the Users (Users List) endpoint.
    """
    def __init__(self):
        super().__init__()
        self.__page = None
        self.__per_page = None
        self.__total = None
        self.__total_pages = None
        self.__data = None
        self.__support = None

    @property
    def page(self) -> int:
        return self.__page

    @property
    def per_page(self) -> int:
        return self.__per_page

    @property
    def total(self) -> int:
        return self.__total

    @property
    def total_pages(self) -> int:
        return self.__total_pages

    @property
    def data(self) -> list:
        return self.__data

    @property
    def support(self) -> dict:
        return self.__support

    def update(self, page: int, per_page: int, total: int, total_pages: int, data: list, support: dict) -> "UsersResponse":
        self.__page = page
        self.__per_page = per_page
        self.__total = total
        self.__total_pages = total_pages
        self.__data = data
        self.__support = support

        return self

import requests
from src.ConfigFile import ConfigFile
from src.contracts.UsersIdResponse import UsersIdResponse
from src.contracts.UsersResponse import UsersResponse


class UsersWrapper:
    def __init__(self):
        self._test_config = ConfigFile()
        self._endpoint = "api/users"
        self._base_url = self._test_config.config["base_url"]

    def get_users(self, page: int = None, per_page: int = None) -> UsersResponse:
        url = f"{self._base_url}/{self._endpoint}"

        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        response = requests.get(url, params=params)
        users_response = UsersResponse().load(response=response)

        return users_response

    def get_users_id(self, id: int) -> UsersIdResponse:
        url = f"{self._base_url}/{self._endpoint}/{id}"

        response = requests.get(url)
        users_response = UsersIdResponse().load(response=response)

        return users_response

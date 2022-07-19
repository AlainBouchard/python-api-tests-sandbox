import json
import requests
from src.ConfigFile import ConfigFile
from src.contracts.RegisterRequest import RegisterRequest
from src.contracts.RegisterResponse import RegisterResponse


class RegisterWrapper:
    """
    Wrapper for the Register API.
    """
    def __init__(self):
        self._test_config = ConfigFile()
        self._endpoint = "api/register"
        self._base_url = self._test_config.config["base_url"]

    def post_register(self, register_dict: dict) -> RegisterResponse:
        """
        Send a POST request to the Register API to register a user.
        :param register_dict: the dictionary with the register user content.
        :return: the endpoint response.
        """
        url = f"{self._base_url}/{self._endpoint}"
        register_json = json.dumps(register_dict)

        headers = {"content-type": "application/json"}
        response = requests.post(url, data=register_json, headers=headers)

        register_response = RegisterResponse().load(response=response)

        return register_response

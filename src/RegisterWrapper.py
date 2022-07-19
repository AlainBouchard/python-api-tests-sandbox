import json
import requests
from src.ConfigFile import ConfigFile
from src.contracts.RegisterResponse import RegisterResponse


class RegisterWrapper:
    def __init__(self):
        self._test_config = ConfigFile()
        self._endpoint = "api/register"
        self._base_url = self._test_config.config["base_url"]

    def post_register(self, register_dict) -> RegisterResponse:
        url = f"{self._base_url}/{self._endpoint}"
        register_json = json.dumps(register_dict)

        headers = {"content-type": "application/json"}
        response = requests.post(url, data=register_json, headers=headers)

        register_response = RegisterResponse().load(response=response)

        return register_response

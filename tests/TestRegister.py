import json
import pytest
from src.RegisterWrapper import RegisterWrapper
from src.contracts.RegisterRequest import RegisterRequest


class TestRegister(object):
    def test_register_with_good_body_expect_200(self):
        # As a user, I want to register so that I can eventually login to the application
        register_request = RegisterRequest().fake_data()
        response = RegisterWrapper().post_register(register_request.to_dict())

        assert response.response.status_code == 200

    @pytest.mark.parametrize("keys, expected_text", [
        (["password"], "Missing password"),
        (["email"], "Missing email or username"),
        (["email", "password"], "Missing email or username")
    ])
    def test_register_with_bad_request_expect_400(self, keys, expected_text):
        # As an admin, I want to refuse the register process to an unknown user.
        register_request = RegisterRequest().fake_data().to_dict()

        for each_key in keys:
            del register_request[each_key]  # removing a key to provoke a bad request.

        response = RegisterWrapper().post_register(register_request)

        assert response.response.status_code == 400
        assert json.loads(response.response.text)["error"] == expected_text

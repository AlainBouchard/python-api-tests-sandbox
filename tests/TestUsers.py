import pytest
from src.UsersWrapper import UsersWrapper


class TestUsers(object):
    def test_get_users_list_with_default_params_then_expect_200(self):
        # As a user, I want to get all users list using default params
        response = UsersWrapper().get_users()

        assert response.response.status_code == 200
        assert response.page == 1
        assert response.per_page == 6
        assert response.total == 12
        assert response.total_pages == 2
        assert len(response.data) == 6
        assert response.support.get("url", None) is not None
        assert response.support.get("text", None) is not None

    @pytest.mark.parametrize("page, per_page, total, total_pages, data_len", [
        (2, 4, 12, 3, 4),
        (20, 6, 12, 2, 0)
    ])
    def test_get_users_list_misc_parameters_then_expect_200(self, page, per_page, total, total_pages, data_len):
        # As a user, I want to get users list using given params
        response = UsersWrapper().get_users(page=page, per_page=per_page)

        assert response.response.status_code == 200
        assert response.page == page
        assert response.per_page == per_page
        assert response.total == total
        assert response.total_pages == total_pages
        assert len(response.data) == data_len
        assert response.support.get("url", None) is not None
        assert response.support.get("text", None) is not None

    def test_get_single_users_id_then_expect_200(self):
        # As a user, I want to get data of a single users id
        response = UsersWrapper().get_users_id(id=2)

        # NOTE: A real API would allow to dynamically create data and faked data could be used.
        assert response.response.status_code == 200
        assert response.data == {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }

        assert response.support == {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }

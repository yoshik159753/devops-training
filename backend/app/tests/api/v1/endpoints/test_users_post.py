import re

import pytest
from src.database.models.user import User


@pytest.fixture(scope='function', autouse=True)
def setup_teardown_for_module(migrate):
    """モジュール内のテストに対して準備、後処理を行います。
    """
    ...


def test_ok(client, server_url, api_version):
    """正常終了
    """
    before_user_count = User.count()

    url = f"{server_url}{api_version}/users"
    request_body = {"name": "username",
                    "email": "username@example.com",
                    "password": "p@ssw0rd",
                    "password_confirmation": "p@ssw0rd"}
    response = client.post(url, json=request_body)

    assert response.status_code == 200, response.get_json()

    response_body = response.get_json()
    assert "id" in response_body.keys()
    uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    assert re.fullmatch(uuid_pattern, response_body.get("id")) is not None

    assert before_user_count + 1 == User.count()


def test_badrequest(client, server_url, api_version):
    """エラー
    """
    before_user_count = User.count()

    url = f"{server_url}{api_version}/users"
    request_body = {"email": "username@example",
                    "password": "123",
                    "password_confirmation": "456"}
    response = client.post(url, json=request_body)

    assert response.status_code == 400

    response_body = response.get_json()
    assert "summary" in response_body.keys()
    assert type(response_body.get("summary")) is str
    assert "errors" in response_body.keys()
    assert len(response_body.get("errors")) == 3
    for error in response_body.get("errors"):
        assert "message" in error.keys()
        assert type(error.get("message")) is str

    assert before_user_count == User.count()

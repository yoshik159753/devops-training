import datetime as dt

import pytest
from src.database.models.user import User


@pytest.fixture(scope='function', autouse=True)
def setup_teardown_for_module(migrate):
    """モジュール内のテストに対して準備、後処理を行います。
    """
    ...


@pytest.fixture()
def users():
    """テスト用の Users を返します。
    """
    _users = []
    for i in range(3):
        user = User(name=f"Example User {i}",
                    email=f"user{i}@example.com",
                    password="foobar",
                    password_confirmation="foobar")
        user.save()
        _users.append(user)
    return _users


def test_get_users(client, server_url, api_version, users):
    """取得した User が期待通りであることをテストします。
    """
    for user in users:
        headers = {}
        url = f"{server_url}{api_version}/users/{user.id}"
        response = client.get(url, headers=headers)

        assert response.status_code == 200
        response_body = response.get_json()
        for key in ['id', 'name', 'email']:
            message = f"{key} is unmatched. acutal[{response_body.get(key)}], expected[{getattr(user, key)}]"
            assert response_body.get(key) == getattr(user, key), message
        for key in ['created_at', 'updated_at']:
            message = f"{key} is unmatched. acutal[{response_body.get(key)}], expected[{getattr(user, key)}]"
            assert dt.datetime.fromisoformat(response_body.get(key)) == getattr(user, key), message

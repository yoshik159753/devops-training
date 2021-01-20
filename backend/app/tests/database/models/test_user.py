import pytest

from src.database.models.user import User


@pytest.fixture(scope="module", autouse=True)
def user():
    user = User(name="Example User", email="user@example.com")
    yield(user)


def test_should_be_valid(user):
    """ User が有効かテスト
    """
    assert user.is_valid()

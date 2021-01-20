import pytest

from src.database.models.user import User


@pytest.fixture(scope="function", autouse=True)
def user():
    user = User(name="Example User", email="user@example.com")
    yield(user)


def test_should_be_valid(user):
    """ User が有効かテスト
    """
    assert user.is_valid()


@pytest.mark.parametrize(
    "name", [
        pytest.param(""),
        pytest.param("   "),
        pytest.param("　　　"),
        pytest.param(" 　 　 　"),
    ])
def test_name_should_be_present(user, name):
    """ User の name が空文字、空白のみの場合は無効であること
    """
    user.name = name
    assert not user.is_valid()


@pytest.mark.parametrize(
    "email", [
        pytest.param(""),
        pytest.param("   "),
        pytest.param("　　　"),
        pytest.param(" 　 　 　"),
    ])
def test_email_should_be_present(user, email):
    """ User の email が空文字、空白のみの場合は無効であること
    """
    user.email = email
    assert not user.is_valid()


def test_name_should_not_be_too_long(user):
    """ User の name が50文字を超過している場合は無効であること
    """
    user.name = "a" * 51
    assert not user.is_valid()


def test_email_should_not_be_too_long(user):
    """ User の email が255文字を超過している場合は無効であること
    """
    domain = "@example.com"
    user.email = "a" * (256 - len(domain)) + domain
    assert not user.is_valid()

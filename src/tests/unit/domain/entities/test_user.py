import mock
import pytest
from datetime import datetime

from api.domain.repositories.user_repository import UserRepository
from api.domain.entities.user import User, UserNotFound, UserCredentialsInvalid


@mock.patch.object(UserRepository, "get_user")
@mock.patch.object(User, "check_password")
def test_authenticate_success(check_password_mock, get_user_mock, app):
    username = "test_user"
    password = "test_password"
    user = User(username, "test_role", "hashed_password", datetime.now(), datetime.now())

    get_user_mock.return_value = user
    check_password_mock.return_value = True

    token = User.authenticate(username, password, UserRepository)

    assert type(token) is str


@mock.patch.object(UserRepository, "get_user")
def test_authenticate_user_not_found_error(get_user_mock, app):
    username = "test_user"
    password = "test_password"

    get_user_mock.return_value = None
    with pytest.raises(UserNotFound):
        User.authenticate(username, password, UserRepository)


@mock.patch.object(UserRepository, "get_user")
@mock.patch.object(User, "check_password")
def test_authenticate_invalid_password(check_password_mock, get_user_mock, app):
    username = "test_user"
    password = "test_password"
    user = User(username, "test_role", "hashed_password", datetime.now(), datetime.now())

    get_user_mock.return_value = user
    check_password_mock.return_value = False

    with pytest.raises(UserCredentialsInvalid):
        User.authenticate(username, password, UserRepository)

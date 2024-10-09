import mock
import pytest
from flask import request
import flask_jwt_extended

from api.domain.entities.user import User, UserNotFound, UserCredentialsInvalid
from api.views import decorators


@mock.patch.object(User, "authenticate")
def test_token_success(authenticate_mock, app):
    
    authenticate_mock.return_value = 'token_abc'
    payload = {"username": "test", "password": "test"}
    response = app.post(
        "/api/v1/token",
        json=payload
    )

    assert response.json == {'token': 'token_abc'}
    assert response.status_code == 200


@mock.patch.object(User, "authenticate")
def test_token_user_not_found(authenticate_mock, app):
    
    authenticate_mock.side_effect = UserNotFound("User not found")
    payload = {"username": "test", "password": "test"}
    response = app.post(
        "/api/v1/token",
        json=payload
    )

    assert response.json == {'message': 'User not found'}
    assert response.status_code == 401


@mock.patch.object(User, "authenticate")
def test_token_invalid_credentials(authenticate_mock, app):
    
    authenticate_mock.side_effect = UserCredentialsInvalid("Invalid credentials")
    payload = {"username": "test", "password": "test"}
    response = app.post(
        "/api/v1/token",
        json=payload
    )

    assert response.json == {'message': 'Invalid credentials'}
    assert response.status_code == 401


def test_user_get_success(create_jwt_user, app):
    
    headers = {"Authorization": f"Bearer {create_jwt_user}"}
    response = app.get(
        "/api/v1/user",
        headers=headers
    )
    assert response.json == {'message': 'OK'}
    assert response.status_code == 200


def test_user_no_jwt_error(app):
    headers = {"Authorization": f"Bearer token_abc"}
    response = app.get(
        "/api/v1/user",
        headers=headers
    )
    assert response.json == {'msg': 'Not enough segments'}
    assert response.status_code == 422
    

def test_user_role_error(create_jwt_admin, app):
    headers = {"Authorization": f"Bearer {create_jwt_admin}"}
    response = app.get(
        "/api/v1/user",
        headers=headers
    )
    assert response.json == {'message': 'Unauthorized role admin'}
    assert response.status_code == 403


def test_admin_get_success(create_jwt_admin, app):
    
    headers = {"Authorization": f"Bearer {create_jwt_admin}"}
    response = app.get(
        "/api/v1/admin",
        headers=headers
    )
    assert response.json == {'message': 'OK'}
    assert response.status_code == 200


def test_admin_no_jwt_error(app):
    headers = {"Authorization": f"Bearer token_abc"}
    response = app.get(
        "/api/v1/admin",
        headers=headers
    )
    assert response.json == {'msg': 'Not enough segments'}
    assert response.status_code == 422
    

def test_admin_role_error(create_jwt_user, app):
    headers = {"Authorization": f"Bearer {create_jwt_user}"}
    response = app.get(
        "/api/v1/admin",
        headers=headers
    )
    assert response.json == {'message': 'Unauthorized role user'}
    assert response.status_code == 403
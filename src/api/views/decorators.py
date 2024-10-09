from flask_jwt_extended import get_jwt_identity
from flask import abort


def validate_role(required_role):
    def wrapper(view_func):
        def inner(*args, **kwargs):
            user_data = get_jwt_identity()
            if user_data.get("role") != required_role:
                abort(403, f"Unauthorized role {user_data.get('role')}")
            return view_func(*args, **kwargs)
        return inner
    return wrapper
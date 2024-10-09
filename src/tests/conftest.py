import pytest

from api.app import create_app, db
from flask_jwt_extended import create_access_token


@pytest.fixture(scope="package")
def app():
    app = create_app("Testing")
    app.config["TESTING"] = True
    client = app.test_client()
    with app.app_context():
        yield client


@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    db.session.rollback()

def pytest_addoption(parser):
    parser.addoption("--skip-startfinish", default=False, action="store_true")


@pytest.fixture
def skip_startfinish(request):
    return request.config.getoption("--skip-startfinish")


def pytest_sessionstart(session):
    from sqlalchemy import text, exc

    if session.config.getoption("--skip-startfinish"):
        return

    app = create_app("Testing")
    app.config["TESTING"] = True

    with app.app_context():
        db.metadata.bind = db.engine
        try:
            db.session.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
        except exc.OperationalError:
            session.db_connected = False
        else:
            session.db_connected = True
            db.session.commit()
            db.create_all()


def pytest_sessionfinish(session):
    if session.config.getoption("--skip-startfinish") or not session.db_connected:
        return

    app = create_app("Testing")
    with app.app_context():
        db.metadata.bind = db.engine
        db.drop_all()
        


@pytest.fixture()
def create_jwt_user():
    return create_access_token(identity={"username": "user", "role": "user"})


@pytest.fixture()
def create_jwt_admin():
    return create_access_token(identity={"username": "admin", "role": "admin"})
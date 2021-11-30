from init_db import init_db


def pytest_configure():
    init_db()

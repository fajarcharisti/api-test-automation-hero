import pytest

@pytest.fixture(scope="function")
def context():
    return {
        "payload": None,
        "response": None
    }
import pytest
import logging


@pytest.fixture(scope="session", autouse=True)
def set_logging() -> None:
    print("###################")
    logging.info("set_logging on conftest.py")

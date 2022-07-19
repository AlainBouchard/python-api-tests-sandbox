import pytest
import logging


@pytest.fixture(scope="session", autouse=True)
def setup_session() -> None:
    # Location to add the session setup, called once, before all tests.
    logging.info("setup session in conftest.py")

import logging
import pytest


@pytest.fixture(scope="class")
def set_logging() -> None:
    logging.info("set_logging in ReqResTests class")


class TestReqRes:
    @classmethod
    def setup_class(cls):
        logging.debug('This will get logged')
        logging.info("starting class: {} execution".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        logging.info("starting class: {} execution".format(cls.__name__))

    def setup_method(self, method):
        logging.info("starting execution of tc: {}".format(method.__name__))

    def teardown_method(self, method):
        logging.info("starting execution of tc: {}".format(method.__name__))

    def test_tc1(self):
        logging.info("running tc1")
        assert True

    def test_tc2(self):
        logging.info("running tc2")
        assert True

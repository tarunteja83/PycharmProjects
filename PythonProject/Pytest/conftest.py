import logging
import pytest


@pytest.fixture(scope='session')
#This is to determine the fixture for test execution
def preEnvSetUp():
    print("Environment setup up for test execution")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info("Automation started")
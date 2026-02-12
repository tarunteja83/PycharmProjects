#Fixtures
import pytest


@pytest.fixture(scope='module')
#This is to determine the fixture for test execution
def envSetUp():
    #Scope module determines only 1 time execution of fixture
    #Scope function determines complete function for execution where ever in use
    #Scope Class when the test is written in form of class it can be used however class and module is similar
    #Scope session works for current session
    print("Environment setup up for test execution module")
    return "Pass"

@pytest.fixture(scope='function')
#This is to determine the fixture for test execution
def testSetUp():
    print("Environment setup up for test execution module")
    yield#Pause the fixture execution and execute post yield post remaining tests
    print("Teardown process completed")

def test_firstCheck(envSetUp, testSetUp):
    print("This is a First Test")
    assert envSetUp == "pass"

@pytest.mark.skip
def test_secondCheck(preEnvSetUp, testSetUp):
    print("This is a Second Test")

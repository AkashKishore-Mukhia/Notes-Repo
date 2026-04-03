import pytest



# we must have the `test_` prefix for pytest to recognize the test function
# def test_first_test_work():
#     print("Hello World")



# @pytest.fixture
# def my_worker():
#     print("Configure setup before test run")

# def test_first_test_work(my_worker):
#     # fixture will be executed before the test function
#     print("Hello World")


# @pytest.fixture
# def my_worker():
#     print("Configure setup before test run")
#     # we can return any value from the fixture, and it will be passed to the test function as an argument
#     return True

# def test_first_test_work(my_worker):
#     print("first test work")
#     assert my_worker


# we can also use the `yield` statement in the fixture to perform some actions after the test function has been executed
# @pytest.fixture
# def my_worker():
#     print("Configure setup before test run")
#     yield
#     print("Tear down after test run")

# def test_first_test_work(my_worker):
#     print("first test work")


# will run fixture only once for the entire module
@pytest.fixture(scope='module')
def my_worker():
    print("Configure setup before test run")
   

def test_first_test_work(my_worker):
    print("first test work")

def test_second_test_work(my_worker):
    print("second test work")
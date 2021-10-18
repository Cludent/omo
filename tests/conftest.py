import pytest
from omo_tests.pages import omo


@pytest.fixture(scope='function', autouse=True)
def close_app():
    yield
    omo.driver.quit()

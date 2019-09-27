from model.group import Group
from fixture.application import Application
import pytest

# scope="session"
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


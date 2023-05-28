import pytest
from fixture.application import Application
import json
import os.path

fixture = None
targer = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if targer is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        request.config.getoption("--target"))
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    fixture.session.ensure_login(username=target["username"], password=target["password"], base_url=target["baseurl"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
import pytest
import requests
from endpoints.employees import Employees
from env_setup import Credentials, Endpoints
from support.custom_errors import TokenNotFoundError, TokenNotGeneratedError


@pytest.fixture()
def create_session():
    yield requests.Session()


@pytest.fixture(scope="session")
def credentials():
    return Credentials.get_env_variables()


@pytest.fixture(scope="session")
def bearer_token(credentials):
    response = requests.post(f"{Endpoints.TOKEN_URL}",
                             json={"username": credentials.APP_USERNAME, "password": credentials.APP_PASSWORD},
                             headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        token = response.json().get("token")
        if token is None:
            raise TokenNotFoundError
        yield token
    else:
        raise TokenNotGeneratedError(response.status_code)


@pytest.fixture()
def employees_endpoint(create_session, bearer_token):
    yield Employees(Endpoints.EMPLOYEES_URL, create_session, bearer_token)



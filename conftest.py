import pytest
import requests
from data import BASE_URL,DATA_AUTHORIZATION,STATIC_DATA
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@pytest.fixture
def user():
    return UserMethods()

@pytest.fixture
def order():
    return OrderMethods()

@pytest.fixture
def user_1():

    response = requests.post(f'{BASE_URL}auth/register', json=STATIC_DATA)
    requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
    yield response
    r = response.json()['accessToken']
    requests.delete(f'{BASE_URL}auth/user', headers={'authorization':f'{r}'})


@pytest.fixture
def user_2():
    response = requests.post(f'{BASE_URL}auth/register', json=STATIC_DATA)
    yield response
    r = response.json()['accessToken']
    requests.delete(f'{BASE_URL}auth/user', headers={'authorization':f'{r}'})
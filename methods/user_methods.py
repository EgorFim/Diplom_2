import allure
import requests
from data import BASE_URL,DATA_LOGIN_WITHOUT_FIELD,STATIC_DATA,DATA_AUTHORIZATION,DATA_AUTHORIZATION_WRONG_PASSWORD,DATA_CHANGE


class UserMethods:

    @allure.step('создаем пользователя')
    def create_user(self):
        response = requests.post(f'{BASE_URL}auth/register',data=STATIC_DATA)
        requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        r = response.json()['accessToken']
        requests.delete(f'{BASE_URL}auth/user', headers={'authorization': f'{r}'})
        return response.status_code

    @allure.step('создаем пользователя без запол обязательных полей')
    def create_user_without_field(self):
        response = requests.post(f'{BASE_URL}auth/register', data=DATA_LOGIN_WITHOUT_FIELD)
        return response.status_code, response.json()['message']

    @allure.step('создаем ранее созданного пользователя')
    def create_user_already_exist(self):
        ac_token = requests.post(f'{BASE_URL}auth/register', data=STATIC_DATA)
        r = ac_token.json()['accessToken']
        response = requests.post(f'{BASE_URL}auth/register', data=STATIC_DATA)
        requests.delete(f'{BASE_URL}auth/user', headers={'authorization': f'{r}'})
        return response.status_code, response.json()['message']

    @allure.step('авторизация пользователя')
    def authorization_user(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        return response.json()['success']

    @allure.step('авторизация с неправильным паролем')
    def authorization_user_with_wrong_password(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION_WRONG_PASSWORD)
        return response.json()['success'], response.status_code

    @allure.step('изменение информации о пользователе после авторизации')
    def change_user_information_after_authorization(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        ar = response.json()['accessToken']
        change_res = requests.patch(f'{BASE_URL}auth/user',headers={'authorization':f'{ar}'}, json=DATA_CHANGE)
        return change_res.json()['user']

    @allure.step('изменение информации о пользователе без авторизации')
    def change_user_info_without_authrization(self):
        change_res = requests.patch(f'{BASE_URL}auth/user' , json=DATA_CHANGE)
        return change_res.json()['success'], change_res.status_code

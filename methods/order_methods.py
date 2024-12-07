import allure
import requests
from data import BASE_URL, INGREDIENTS, DATA_AUTHORIZATION,DATA_WITHOUT_INGREDIENTS,DATA_WRONG_HASH_INGREDIENT


class OrderMethods:

    @allure.step('создаем заказ')
    def create_order(self):
        ord = requests.post(f'{BASE_URL}orders',data=INGREDIENTS)
        return ord.status_code,ord.json()['success']

    @allure.step('создаем заказ с авторизацией')
    def create_order_with_authorization(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        ar = response.json()['accessToken']
        ord = requests.post(f'{BASE_URL}orders',headers={'authorization':f'{ar}'}, data=INGREDIENTS)
        return ord.status_code,ord.json()['success']

    @allure.step('создаем заказ без ингредиентов')
    def create_order_without_ingredients(self):
        ord = requests.post(f'{BASE_URL}orders', data=DATA_WITHOUT_INGREDIENTS)
        return ord.status_code, ord.json()['message']

    @allure.step('создаем заказ с неправильным хэшем ингредиентов')
    def create_order_wrong_hash_ingredients(self):
        ord = requests.post(f'{BASE_URL}orders', data=DATA_WRONG_HASH_INGREDIENT)
        return ord.status_code

    @allure.step('получаем заказы авторизованного юзера')
    def receive_orders_authorized_user(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        ar = response.json()['accessToken']
        requests.post(f'{BASE_URL}orders', headers={'authorization': f'{ar}'}, data=INGREDIENTS)
        rec = requests.get(f'{BASE_URL}orders',headers={'authorization':f'{ar}'})
        return rec.status_code, rec.json()['success'], rec.json()['orders']

    @allure.step('получаем заказы без авторизации')
    def receive_orders_without_authorization(self):
        response = requests.post(f'{BASE_URL}auth/login', json=DATA_AUTHORIZATION)
        ar = response.json()['accessToken']
        requests.post(f'{BASE_URL}orders', headers={'authorization': f'{ar}'}, data=INGREDIENTS)
        rec = requests.get(f'{BASE_URL}orders')
        return rec.status_code, rec.json()['message']


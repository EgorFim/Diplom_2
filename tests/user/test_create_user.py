import allure
from data import RESPONSE_TEXT_LOGIN_WITHOUT_FIELD, FORBIDDEN_CODE, RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST,SUCCESS,NOT_SUCCESS,UNAUTHORIZED_CODE,OK_CODE
import requests

class TestCreateUser:

    @allure.title('Тест на создание пользователя')
    def test_create_user(self,user):
        assert user.create_user() == OK_CODE

    @allure.title('Тест создания пользователя с незаполненными обязательными полями')
    def test_create_user_without_field(self,user):
        user.create_user_without_field()
        assert user.create_user_without_field()[0] == FORBIDDEN_CODE  and user.create_user_without_field()[1] == RESPONSE_TEXT_LOGIN_WITHOUT_FIELD

    @allure.title('Тест создания ранее созданного пользователя')
    def test_create_user_already_exist(self,user):
        assert user.create_user_already_exist()[0] == FORBIDDEN_CODE and user.create_user_already_exist()[1] == RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST

    @allure.title('Тест на успешнкю авторизацию пользователя')
    def test_authorization_user_success(self,user,user_2):
        assert user.authorization_user() == SUCCESS

    @allure.title('Тест на авторизацию пользователя с неправильным паролем')
    def test_authorization_user_wrong_password(self,user,user_2):
        assert user.authorization_user_with_wrong_password()[0] == NOT_SUCCESS and user.authorization_user_with_wrong_password()[1] == UNAUTHORIZED_CODE
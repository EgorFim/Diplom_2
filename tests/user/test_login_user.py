import allure
from data import SUCCESS,NOT_SUCCESS,UNAUTHORIZED_CODE


class TestLoginUser:

    @allure.title('Тест на авторизацию ранее созданного пользователя')
    def test_login_user_already_exist(self,user,user_2):
        assert user.authorization_user() == SUCCESS

    @allure.title('Тест на авторизацию пользователя с неправильным паролем')
    def test_login_user_wrong_password(self,user,user_2):
        n = user.authorization_user_with_wrong_password()
        assert n[0] == NOT_SUCCESS and n[1] == UNAUTHORIZED_CODE

import allure
from data import CHANGE_INF_RESPONSE,NOT_SUCCESS,UNAUTHORIZED_CODE


class TestInformation:

    @allure.title('Тест на изменение информации о пользователе после авторизации')
    def test_change_information_after_authorization(self,user,user_2):
        assert user.change_user_information_after_authorization() == CHANGE_INF_RESPONSE

    @allure.title('Тест на измененме информации о пользователе без авторизации')
    def test_change_information_without_authorization(self,user,user_2):
        r = user.change_user_info_without_authrization()
        assert r[0] == NOT_SUCCESS and r[1] == UNAUTHORIZED_CODE
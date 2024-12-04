
from data import RESPONSE_TEXT_LOGIN_WITHOUT_FIELD, FORBIDDEN_CODE, RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST, BASE_URL, \
    STATIC_DATA, DATA_AUTHORIZATION, SUCCESS,DATA_AUTHORIZATION_WRONG_PASSWORD,NOT_SUCCESS,UNAUTHORIZED_CODE


class TestLoginUser:
    def test_login_user_already_exist(self,user,user_2):
        assert user.authorization_user() == SUCCESS

    def test_login_user_wrong_password(self,user,user_2):
        n = user.authorization_user_with_wrong_password()
        assert n[0] == NOT_SUCCESS and n[1] == UNAUTHORIZED_CODE

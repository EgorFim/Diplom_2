from data import RESPONSE_TEXT_LOGIN_WITHOUT_FIELD, FORBIDDEN_CODE, RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST, BASE_URL, \
    STATIC_DATA, DATA_AUTHORIZATION, SUCCESS,DATA_AUTHORIZATION_WRONG_PASSWORD,NOT_SUCCESS,UNAUTHORIZED_CODE,OK_CODE
import requests

class TestCreateUser:

    def test_create_user(self,user):
        assert user.create_user() == OK_CODE


    def test_create_user_without_field(self,user):
        user.create_user_without_field()
        assert user.create_user_without_field()[0] == FORBIDDEN_CODE  and user.create_user_without_field()[1] == RESPONSE_TEXT_LOGIN_WITHOUT_FIELD

    def test_create_user_already_exist(self,user):
        assert user.create_user_already_exist()[0] == FORBIDDEN_CODE and user.create_user_already_exist()[1] == RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST


    def test_authorization_user_success(self,user,user_2):
        assert user.authorization_user() == SUCCESS

    def test_authorization_user_wrong_password(self,user,user_2):
        assert user.authorization_user_with_wrong_password()[0] == NOT_SUCCESS and user.authorization_user_with_wrong_password()[1] == UNAUTHORIZED_CODE
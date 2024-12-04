from data import CHANGE_INF_RESPONSE, SUCCESS, NOT_SUCCESS,UNAUTHORIZED_CODE


class TestInformation:
    def test_change_information_after_authorization(self,user,user_2):
        assert user.change_user_information_after_authorization() == CHANGE_INF_RESPONSE

    def test_change_information_without_authorization(self,user,user_2):
        r = user.change_user_info_without_authrization()
        assert r[0] == NOT_SUCCESS and r[1] == UNAUTHORIZED_CODE
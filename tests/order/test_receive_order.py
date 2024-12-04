from data import SUCCESS,OK_CODE, UNAUTHORIZED_CODE,RESPONSE_TEXT_UNAUTHORIZED_USER

class TestReceiveOrder:
    def test_receive_order_authorized_user(self,order,user_2):
        ord = order.receive_orders_authorized_user()
        assert ord[1] == SUCCESS  and ord[0] == OK_CODE

    def test_receive_order_without_authorization(self,order,user_2):
        ord = order.receive_orders_without_authorization()
        assert ord[0] == UNAUTHORIZED_CODE and ord[1] == RESPONSE_TEXT_UNAUTHORIZED_USER
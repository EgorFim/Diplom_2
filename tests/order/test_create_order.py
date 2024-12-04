
from data import SUCCESS, OK_CODE,UNAUTHORIZED_CODE,NOT_SUCCESS,RESPONSE_TEXT_ORDER_WITHOUT_INGREDIENTS,BAD_REQUEST,DATA_WRONG_HASH_INGREDIENT,INTERNAL_SERVER_ERROR


class TestCreateOrder:
    def test_create_order_without_authorization(self,order):
        ord = order.create_order()
        assert ord[0] == OK_CODE and ord[1] == SUCCESS

    def test_create_order_with_authorization(self,order,user_2):
        ord = order.create_order_with_authorization()
        assert ord[0] == OK_CODE and ord[1] == SUCCESS

    def test_create_order_without_ingredients(self,order):
        ord = order.create_order_without_ingredients()
        assert ord[0] == BAD_REQUEST and ord[1] == RESPONSE_TEXT_ORDER_WITHOUT_INGREDIENTS

    def test_create_order_wrong_hash_ingredients(self,order):
        ord = order.create_order_wrong_hash_ingredients()
        assert ord == INTERNAL_SERVER_ERROR

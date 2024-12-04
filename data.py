BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
DATA_LOGIN_WITHOUT_FIELD = {
"email": f'egorfimushkin11@yandex.ru',
"password": "password",
"name": ""
}

RESPONSE_TEXT_LOGIN_WITHOUT_FIELD = "Email, password and name are required fields"
RESPONSE_TEXT_LOGIN_USER_ALREADY_EXIST = 'User already exists'
RESPONSE_TEXT_ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
RESPONSE_TEXT_UNAUTHORIZED_USER = "You should be authorised"


DATA_AUTHORIZATION = {
"email": "testma221il3@yandex.ru",
"password": "password"
}
STATIC_DATA = {
            "email": "testma221il3@yandex.ru",
            "password": "password",
            "name": "Username"
        }
INTERNAL_SERVER_ERROR = 500
BAD_REQUEST = 400
UNAUTHORIZED_CODE = 401
FORBIDDEN_CODE = 403
OK_CODE = 200
SUCCESS = True
NOT_SUCCESS = False
DATA_AUTHORIZATION_WRONG_PASSWORD = {
"email": "testmail3@yandex.ru",
"password": "passsword"
}

DATA_CHANGE = {
"email": "chanwgemail3@yandex.ru",
"password": "password1"
}

CHANGE_INF_RESPONSE = {'email': 'chanwgemail3@yandex.ru', 'name': 'Username'}
INGREDIENTS = {
"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
}

DATA_WITHOUT_INGREDIENTS = {
"ingredients": []
}


DATA_WRONG_HASH_INGREDIENT = {
"ingredients": ["figjriojbrojbpor"]
}



# import random
import base64
import datetime


def activation_key_generator(email):
    expire_date = datetime.datetime.today() + datetime.timedelta(3)
    activation_key = base64.b64encode(
        str(expire_date)) + base64.b64encode(
        str(email)).split('=')[0]

    return activation_key


def tokens_email(token_id):
    email = base64.b64decode(token_id.split('=')[1] + '==')

    return email


def tokens_expire_date(token_id):
    expire_date = token_id.split('=')[0]

    return expire_date
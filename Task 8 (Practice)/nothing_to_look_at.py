from hashlib import pbkdf2_hmac
import os

app_key = '_5#y2L"F4Q8z.n_xec]/'
salt = os.urandom(32)


def encode(message):
    return pbkdf2_hmac('sha256', message.encode('utf-8'), salt, 100000)

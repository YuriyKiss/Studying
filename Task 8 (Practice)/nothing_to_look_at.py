import jwt

app_key = '_5#y2L"F4Q8z.n_xec]/'
secret_key = "cake_is_a_lie"


def encode(message):
    info = jwt.encode({"pass": message}, secret_key, algorithm='HS256')
    print(info)
    print(type(info))
    return info


def decode(message):
    return jwt.decode(message, secret_key, algorithms='HS256')["pass"]

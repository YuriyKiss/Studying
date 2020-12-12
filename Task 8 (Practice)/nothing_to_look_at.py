from passlib.hash import pbkdf2_sha256

app_key = '_5#y2L"F4Q8z.n_xec]/'


def encode(message):
    return pbkdf2_sha256.hash(message)


def validate(hash_, password):
    return pbkdf2_sha256.verify(password, hash_)

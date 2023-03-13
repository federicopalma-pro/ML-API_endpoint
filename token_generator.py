import secrets
import hashlib


def generate_token():
    token = secrets.token_hex(32)
    token_sha256 = encode_sha256(token)
    return (token, token_sha256)


def encode_sha256(string):
    # encode string to bytes using utf-8
    byte_string = string.encode('utf-8')
    # create SHA-256 hash object
    hash_object = hashlib.sha256()
    # update hash object with byte string
    hash_object.update(byte_string)
    # get hexadecimal representation of hash
    hex_dig = hash_object.hexdigest()
    return hex_dig


# generate token and its SHA256 hash
token, token_sha256 = generate_token()

# print out token and its SHA256 hash
print(f"Token: {token}, Token encoded sha256: {token_sha256}")

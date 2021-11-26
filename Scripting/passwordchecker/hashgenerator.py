import hashlib


def sha1_hasher(key:str):
    result = hashlib.sha1(key.encode('utf-8'))
    return result.hexdigest()

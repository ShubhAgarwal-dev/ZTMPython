# Work left:
# -> to make the count_key-addition function work
# ->to have a option to clear the file read for password
# ->to improve the code redability

import requests
from hashlib import sha1


def passwords_to_check(pass_file):
    with open(file=pass_file) as file:
        password_list = file.read().split(' ')
    return password_list


def hash_generator(value):
    hashed_value = sha1(value.encode('utf-8'))
    return hashed_value.hexdigest()


def preparing_password(password_list: list):
    hashed_password_dict = {
        'first5_char_list': [],
        'tail_list': []
    }
    for password in password_list:
        hashed_password = hash_generator(value=password)
        first5_char, tail = hashed_password[:5], hashed_password[5:]
        hashed_password_dict['first5_char_list'].append(first5_char)
        hashed_password_dict['tail_list'].append(tail)
    return hashed_password_dict


def request_api_data(first5_hashed_char_list: list):
    responce_dict = {}
    for first5_char in first5_hashed_char_list:
        responce = requests.get(
            'https://api.pwnedpasswords.com/range/'+first5_char)
        if (n := responce.status_code) != 200:
            raise RuntimeError(f'error fetching {n}')
        responce_dict[first5_char] = responce.text
    print(type(responce_dict))
    return responce_dict


def count_key_addition(hashed_password_dict: dict, responce_dict: dict):
    # Required to ask to seniors about why I am  getting this error
    hashed_password_dict['count'] = []
    for i in range(len(responce_dict)):
        hashes_returned = responce_dict[hashed_password_dict['first5_char_list'][i]]
        hashes = (line.split(':') for line in hashes_returned.text.splitlines())
        for hash, count in hashes:
            if hash.upper() == hashed_password_dict['tail_list'][i].upper():
                print(count)
                hashed_password_dict['count'].append(count)
            else:
                hashed_password_dict['count'].append(1)
    return None


def check_your_password(filename):
    password_list = passwords_to_check(filename)
    hashed_password_dict = preparing_password(password_list)
    responce_dict = request_api_data(hashed_password_dict['first5_char_list'])
    count_key_addition(hashed_password_dict, responce_dict)
    for i in range(len(responce_dict)):
        if(n := hashed_password_dict['count'][i]) == 0:
            print(f'Feel free to use {password_list[i]}')
        else:
            print(f'{password_list[i]} have been pawned {n} times')


if __name__ == '__main__':
    # dictionary = preparing_password(passwords_to_check('password.txt'))
    # print(request_api_data(dictionary['first5_char_list']))
    check_your_password(r'password.txt')

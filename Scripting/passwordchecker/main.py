from sys import argv
import requests
from hashgenerator import sha1_hasher

password_list = argv[1:]


def request_api_data(password_list):
    count_list = []
    for password in password_list:
        hashed = sha1_hasher(password).upper()
        first_5char, tail = hashed[:5], hashed[5:]
        responce = requests.get(
            "https://api.pwnedpasswords.com/range/" + first_5char)
        # We would only provide first 5 elements of our sha object and it will tell if it does have similar password in its leaked password database
        if (n := responce.status_code) != 200:
            raise RuntimeError(f'Error fetching: {n}')
            # Response of 400 is not good, ideally we must get 200 as response
        count_list.append(get_password_leaked_count(responce.text, tail))
    return count_list


def get_password_leaked_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def main(password_list):
    num_of_args = len(password_list)
    count = request_api_data(password_list)
    print(count)
    for i, password in enumerate(password_list):
        if count[i] == 0:
            print("Not found to have been found in any breech")
        else:
            print(
                f"{password} have been found to have been part of a data breech\nChange your password")


if __name__ == '__main__':
    main(password_list)

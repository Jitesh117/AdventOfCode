import hashlib
from typing import List, Optional


def find_password(door_id):
    password = ""
    index = 0

    while len(password) < 8:
        hash_input = door_id + str(index)
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            password += hash_result[5]
            print(f"Found character: {hash_result[5]}, Current password: {password}")

        index += 1

    return password


def find_password2(door_id: str) -> str:
    password: List[Optional[str]] = [None] * 8
    index = 0

    while None in password:
        hash_input = door_id + str(index)
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            position = int(hash_result[5], 16)
            if position < 8 and password[position] is None:
                password[position] = hash_result[6]
                print(f"Found character: {hash_result[6]} at position {position}")
                print(f"Current password: {''.join(c if c else '_' for c in password)}")

        index += 1

    return "".join(char for char in password if char is not None)


door_id = "wtnhxymk"
print(f"Finding password for door ID: {door_id}")
password = find_password(door_id)
print(f"The password is: {password}")
print()
print(f"Finding 2nd password for door ID: {door_id}")
password = find_password2(door_id)
print(f"The password is: {password}")

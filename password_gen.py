import random
import string

"""
Set #1 -
Password must have at least 12 characters
Characters must be alphanumeric and must have at least one special character
Ask how many passwords required to the user

"""


def simple_password_gen(count=12):
    if count < 12:
        return 'Password must have at least 12 characters'

    simple_password = ''

    while count != 0:
        total = random.choice(string.ascii_letters) + \
                random.choice(string.digits) + \
                random.choice(string.punctuation)
        simple_password += ''.join(random.sample(total, 1))
        count -= 1

    return simple_password


total_passwords = int(input('How many passwords do you need? '))
for i in range(total_passwords):
    print(simple_password_gen())


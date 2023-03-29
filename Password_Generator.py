import secrets
import string

letters = string.ascii_letters
digits = string.digits

alphabet = letters + digits

password_length = 16

password = ''

for i in range(password_length):
    if i != 0 and i % 4 == 0:
        password += '-'
    password += ''.join(secrets.choice(alphabet))

print(password)

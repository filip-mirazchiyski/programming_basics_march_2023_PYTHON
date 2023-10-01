from string import ascii_letters, digits
import random

password_signs = ascii_letters + digits
password_lenght = 10

password = "".join(random.sample(password_signs, password_lenght))
print("Your generated password is: " + password)

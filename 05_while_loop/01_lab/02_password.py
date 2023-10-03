db_username = input()
db_password = input()
password = input()

while db_password != password:
    password = input()

if db_password == password:
    print(f"Welcome {db_username}!")
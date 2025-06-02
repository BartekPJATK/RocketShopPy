import hashlib
from management.repository import insert_company, insert_account, get_account_by_username
from management.helper import pretty_print

def register(username, password, company_name, budget):
    exists = get_account_by_username(username)
    if exists:
        pretty_print("Company already exists!", tag="ERROR")
    else:
        company_id = insert_company(company_name, budget)
        insert_account(company_id, username, hash_password(password))
        pretty_print("Registration successful!", tag="SUCCESS")


def login(username, password):
    user = get_account_by_username(username)
    if user:
        hashed = user["password"]
        if check_password(password, hashed):
            pretty_print("Login successful", tag="SUCCESS")
            return user
        else:
            pretty_print("Incorrect password!", tag="ERROR")
    else:
        pretty_print("User not found!")
    return None


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password, hashed):
    return hash_password(password) == hashed

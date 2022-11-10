from db import DB

def validate(email, password):
    result = DB().execute(f"select * from users where email = '{email}' and password = HashBytes('{password}')").fetchall()

    if result:
        return True
    return False


def registerUser(user_details):
    query  = f"""Insert into users values('{user_details["name"]}', 
    '{user_details["email"]}',
    '{user_details["dob"]}',
    '{user_details["gender"]}',
    HashBytes('{user_details["password"]}'))"""


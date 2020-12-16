import time
import sqlite3
from hashlib import sha512
from .models import User

def create_token(login):
    conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    current_time = time.time()
    token = sha512((login + str(current_time)).encode('utf-8')).hexdigest()
    ttl = current_time + 60*60

    try:
        cursor.execute(f""" update my_api_user set token='{token}', ttl='{ttl}' where my_api_user.login='{login}' """)
        conn.commit()
        return token
    except:
        return False
    

def check_token(user_token):
    conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    current_time = time.time()
    res = {}

    try:
        hash_data = User.objects.get(token=user_token)
        if float(hash_data.ttl) >= current_time:
            user_login = hash_data.login
            create = create_token(login=user_login)
            res['is_valid'] = 'True'
            res['token'] = create
        else:
            res['is_valid'] = 'False'
            res['token'] = ''
    except:
        res['is_valid'] = 'False'
        res['token'] = ''
    return res
            
        
from datetime import datetime
from pathlib import Path

import pymysql
import json
import os
from dotenv import load_dotenv

"""Creds"""
env_path = Path('.CREDS')
load_dotenv(dotenv_path=env_path)
db_table = os.environ['DB_NAME']
host_connection = os.environ['SERVER']
port_connection = os.environ['PORT']
password_connection = os.environ['DB_PASSWORD']
username_connection = os.environ['DB_USERNAME']
creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
connection = pymysql.connect(host='remotemysql.com',
                             port=3306,
                             user='cReOSxv10Q',
                             passwd='iKFLyKI8Aw',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connection.autocommit(True)


def add_user(user_id, username):
    try:
        connection.connect()
        cur = connection.cursor()
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"INSERT INTO {db_table}.users VALUES (%s, %s, %s)", (user_id, username, creation_date))
    except:
        print("FAILED TO CONNECT")
    cur.close()
    connection.close()


def user_info(user_id):
    try:
        connection.connect()
        cur = connection.cursor()
        cur.execute(f"SELECT * FROM {db_table}.users WHERE user_id = %s", user_id)
        for row in cur:
            name = row['user_name']
        return name
    except:
        print("FAILED to get user info!")
    finally:
        cur.close()
        connection.close()


def update_username(user_id, new_name):
    try:
        connection.connect()
        cur = connection.cursor()
        cur.execute(f"UPDATE {db_table}.users SET name = %s where id = %s", (new_name, user_id))
    except:
        print("FAILED to modify username!")

    cur.close()
    connection.close()


def delete_user_id(user_id):
    try:
        connection.connect()
        cur = connection.cursor()
        cur.execute(f"DELETE FROM {db_table}.users WHERE user_id = %s", user_id)
    except:
        print("FAILED to DELETE user ID")
    cur.close()
    connection.close()


def get_all_info():
    try:
        connection.connect()
        cur = connection.cursor()
        cur.execute(f'SELECT * FROM {db_table}.users')
        table = cur.fetchall()
        print(table)
    except:
        print("FAILED TO CONNECT")
    finally:
        cur.close()
        connection.close()

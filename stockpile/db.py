from hashlib import sha256

import sqlite3
import asyncio


async def async_get_cursor(db_file_name: str):
    conn = sqlite3.connect(db_file_name)
    cur = conn.cursor()
    return cur

async def async_drop_cursor_connection(cursor):
    cursor.connection.commit()
    cursor.connection.close()

async def async_execute_sql(sql: str, cursor):
    cursor.execute((sql))

async def async_execute_script(script, cursor):
    with open(script, 'r') as file:
        text = file.read()
        for line in text.split('\n'):
            if line:
                cursor.execute(line)

async def async_hash256(secret: str, codec='utf-8'):
    if isinstance(secret, str):
        passwd = sha256(secret.encode(codec)).digest()
        return passwd
    else:
        raise TypeError('secret must be a string')


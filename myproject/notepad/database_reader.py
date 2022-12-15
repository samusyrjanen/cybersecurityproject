from .database_connection import get_database_connection

connection = get_database_connection()

def get_all_notes():
    cursor = connection.cursor()
    sql = 'select content, username from notes'
    cursor.execute(sql)
    rows = cursor.fetchall()
    return [(row['content'], row['username']) for row in rows]

def get_user_notes(username):
    cursor = connection.cursor()
    sql = f'select content, username from notes where username="{username}"' #SQL injection
    cursor.execute(sql)
    rows = cursor.fetchall()
    return [(row['content'], row['username']) for row in rows]

def write_note(content, username):
    print(type(username), type(content))
    cursor = connection.cursor()
    sql = f'insert into notes (content, username) values ("{content}", "{username}")' #SQL injection
    cursor.execute(sql)
    connection.commit()

#This is the correct way to make SQL queries:
'''
def get_user_notes(username):
    cursor = connection.cursor()
    sql = 'select content, username from notes where username=:username'
    cursor.execute(sql, {'username': username})
    rows = cursor.fetchall()
    return [(row['content'], row['username']) for row in rows]

def write_note(content, username):
    print(type(username), type(content))
    cursor = connection.cursor()
    sql = 'insert into notes (content, username) values (:content, :username)'
    cursor.execute(sql, {'content': content, 'username': username})
    connection.commit()
'''
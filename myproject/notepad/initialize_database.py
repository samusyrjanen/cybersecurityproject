import database_connection

def drop_tables(connection):
    '''
    Poistaa kaikki taulut tietokannasta.

    Args:
        connection: Yhteys tietokantaan.
    '''

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists notes;
    ''')

    connection.commit()

def create_tables(connection):
    '''
    Luo uudet taulut tietokantaan.

    Args:
        connection: Yhteys tietokantaan.
    '''

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE notes (
            id integer primary key,
            content text,
            username text
        );
    ''')

    connection.commit()

def initialize_database():
    '''
    Alustaa tietokannan luomalla uudet tyhjät taulut.
    '''

    connection = database_connection.get_database_connection()

    drop_tables(connection)
    create_tables(connection)

initialize_database()

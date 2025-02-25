import sqlite3

class DBManager:
    def __init__(self, db_name='edm_contacts.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                genre TEXT NOT NULL,
                contact_info TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_contact(self, name, genre, contact_info):
        self.cursor.execute('''
            INSERT INTO contacts (name, genre, contact_info)
            VALUES (?, ?, ?)
        ''', (name, genre, contact_info))
        self.connection.commit()

    def get_contact(self, name):
        self.cursor.execute('''
            SELECT genre, contact_info FROM contacts WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()

    def update_contact(self, name, genre, contact_info):
        self.cursor.execute('''
            UPDATE contacts
            SET genre = ?, contact_info = ?
            WHERE name = ?
        ''', (genre, contact_info, name))
        self.connection.commit()

    def close(self):
        self.connection.close()
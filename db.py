import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()

    # Create the Accounts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        currency TEXT NOT NULL,
        balance REAL NOT NULL
    );
    ''')

    # Create the Transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    account_from INTEGER,
    account_to INTEGER,
    amount_sent REAL NOT NULL,
    amount_received REAL NOT NULL,
    FOREIGN KEY(account_from) REFERENCES accounts(id),
    FOREIGN KEY(account_to) REFERENCES accounts(id)
);

    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

create_database()

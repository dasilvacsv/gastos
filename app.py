import sqlite3

## Adding account script
def add_account(name, currency, balance):
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to insert the new account
    insert_account_sql = '''
    INSERT INTO accounts (name, currency, balance) 
    VALUES (?, ?, ?)
    '''
    
    # Execute the command
    try:
        cursor.execute(insert_account_sql, (name, currency, balance))
        conn.commit()
        print(f"Account '{name}' added successfully.")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Adding transaction script
def add_transaction(account_from, account_to, amount_sent, amount_received):
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to insert the new transaction
    insert_transaction_sql = '''
    INSERT INTO transactions (account_from, account_to, amount_sent, amount_received) 
    VALUES (?, ?, ?, ?)
    '''
    
    # Execute the command
    try:
        cursor.execute(insert_transaction_sql, (account_from, account_to, amount_sent, amount_received))
        conn.commit()
        print("Transaction added successfully.")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Fetching accounts script
def fetch_accounts():
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to fetch all accounts
    fetch_accounts_sql = '''
    SELECT * FROM accounts
    '''
    
    # Execute the command
    try:
        cursor.execute(fetch_accounts_sql)
        accounts = cursor.fetchall()
        return accounts
    except sqlite3.Error as error:
        print("Failed to fetch data from sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Fetching transactions script
def fetch_transactions():
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to fetch all transactions
    fetch_transactions_sql = '''
    SELECT * FROM transactions
    '''
    
    # Execute the command
    try:
        cursor.execute(fetch_transactions_sql)
        transactions = cursor.fetchall()
        return transactions
    except sqlite3.Error as error:
        print("Failed to fetch data from sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Fetching account by id script
def fetch_account_by_id(account_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to fetch the account by id
    fetch_account_by_id_sql = '''
    SELECT * FROM accounts WHERE id = ?
    '''
    
    # Execute the command
    try:
        cursor.execute(fetch_account_by_id_sql, (account_id,))
        account = cursor.fetchone()
        return account
    except sqlite3.Error as error:
        print("Failed to fetch data from sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Fetching transactions by account id script
def fetch_transactions_by_account_id(account_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('moneyflow.db')
    cursor = conn.cursor()
    
    # SQL command to fetch the transactions by account id
    fetch_transactions_by_account_id_sql = '''
    SELECT * FROM transactions WHERE account_from = ? OR account_to = ?
    '''
    
    # Execute the command
    try:
        cursor.execute(fetch_transactions_by_account_id_sql, (account_id, account_id))
        transactions = cursor.fetchall()
        return transactions
    except sqlite3.Error as error:
        print("Failed to fetch data from sqlite table", error)
    finally:
        # Make sure that the connection is closed even if an error occurred
        if conn:
            conn.close()

## Script to use the functions with a 
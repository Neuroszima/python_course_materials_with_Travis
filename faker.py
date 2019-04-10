import random, datetime, math, os

import psycopg2
from localsettings import DB, superuser

random.seed(1147)

CUSTOM_QUERRY = '''SELECT * FROM (SELECT * FROM (Select table_name FROM (
SELECT * FROM information_schema.tables
WHERE table_name NOT LIKE 'pg_%') AS foo
WHERE table_type='BASE TABLE') AS foo3
WHERE table_name NOT LIKE 'sql_%') as foo WHERE table_name NOT LIKE 'auth%';'''

TRANSACTION_HISTORY = os.getcwd() + '/client_transactions.txt'


def readnames(fem_names=250, male_names=250, surnames=500):

    with open('txt_files/female-first-names.txt', 'r') as name_file:
        female = [line for line in zip(name_file, range(fem_names))]

    with open('txt_files/male-first-names.txt', 'r') as name_file:
        male = [line for line in zip(name_file, range(male_names))]

    with open('txt_files/male-first-names.txt', 'r') as name_file:
        last = [line for line in zip(name_file, range(surnames))]

    print(len(female))
    print(len(male))
    print(len(last))

    return female, male, last


'''
faker faking bank transactions and accounts
'''


def create_bank(db_settings, database):
    # language=Postgres SQL
    sql_querry = '''CREATE DATABASE bank;'''
    established = False
    while not established:
        try:
            conn = psycopg2.connect(**db_settings,
                                    database=database)
            established = True
        except psycopg2.OperationalError:
            conn = psycopg2.connect(**db_settings)
            conn.autocommit = True
            temp_cursor = conn.cursor()
            temp_cursor.execute(sql_querry)
            temp_cursor.close()
            conn.close()

    conn.autocommit = True
    temp_cursor = conn.cursor()
    try:
        fake_tables(temp_cursor)
        account_numbers = fake_accounts(temp_cursor, readnames())
        print(account_numbers[0])
        fake_bank_services(temp_cursor)
        fake_transactions(temp_cursor, account_numbers)
    except Exception as e:
        print(e)
    temp_cursor.close()
    print("Albercik")
    return conn


def delete_bank(cursor):
    sql_querry = '''DROP DATABASE bank;'''
    cursor.execute(sql_querry)


def fake_tables(temp_cursor):
    create_account_tab = '''
    CREATE TABLE Accounts(
    id serial,
    name VARCHAR(255),
    surname VARCHAR(255),
    balance DECIMAL,
    account_nr INTEGER UNIQUE,
    PRIMARY KEY (id));'''
    create_bank_service_tab = '''
    CREATE TABLE Bank_services(
    id serial,
    name VARCHAR(255),
    PRIMARY KEY (id));'''
    create_transaction_tab = '''
    CREATE TABLE Transactions(
    id serial,
    source_account_nr INTEGER,
    destination_account_nr INTEGER,
    transfer_amount DECIMAL,
    date date,
    service_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(source_account_nr) REFERENCES Accounts(account_nr),
    FOREIGN KEY(destination_account_nr) REFERENCES Accounts(account_nr),
    FOREIGN KEY(service_id) REFERENCES Bank_services(id));'''
    temp_cursor.execute(create_account_tab)
    temp_cursor.execute(create_bank_service_tab)
    temp_cursor.execute(create_transaction_tab)


def fake_accounts(temp_cursor, client_data):
    # table structure:
    # id serial,
    # name VARCHAR(255),
    # surname VARCHAR(255),
    # balance DECIMAL,
    # account_nr INTEGER UNIQUE,
    female, male, surnames = client_data
    names = female + male
    random.shuffle(names)
    random.shuffle(surnames)
    print("surnames:", len(surnames))
    print("names:", len(names))
    account_nr = [10000 + 5*i for i in range(len(surnames))]
    print(account_nr[::50])
    random.shuffle(account_nr)
    temp = [] + account_nr
    for name, surname in zip(names, surnames):
        n = str(name[0]).replace('\n', '')
        s = str(surname[0]).replace('\n', '')
        balance = math.floor(random.gauss(50000, 10000)*100)/100
        if balance < 0:
            balance = 0
        sql_querry = f"""INSERT INTO Accounts(name, surname, balance, account_nr)
        VALUES ('{n}', '{s}', {balance}, {temp.pop()})"""
        # print(sql_querry)
        temp_cursor.execute(sql_querry)
    temp_cursor.execute(f"""INSERT INTO Accounts(name, surname, balance, account_nr)
                            VALUES ('IDEA', 'BANK', 1000000, 1500)""")
    return account_nr


def fake_bank_services(temp_cursor):
    # table structure:
    # id serial,
    # name VARCHAR(255),
    services = [
        'loan',
        'deposit',
        'transfer',
    ]
    for service in services:
        sql_querry = f"""INSERT INTO Bank_services(name)
        VALUES ('{service}')"""
        temp_cursor.execute(sql_querry)


def transaction_generator(client_data, max_transactions=20):
    for client in client_data:  # account number
        for _ in range(random.randint(0, max_transactions)):  # random number of transactions a client has made
            service = service_choice(random.random())
            transfer_amount = math.floor(random.random()*30000)/100
            date = datetime.date(random.randint(1990, 2010), random.randint(1, 11), random.randint(1, 28))
            if service == 1:
                source_account_nr = 1500
                destination_account_nr = client
            elif service == 2:
                source_account_nr, destination_account_nr = [client]*2
            else:  # service == 3
                source_account_nr, destination_account_nr = client, random.choice(client_data)
            data = f"{source_account_nr},{destination_account_nr},{transfer_amount},{date},{service}\n"
            yield data


def service_choice(propability):
    services = {
        'loan': 1,
        'deposit': 2,
        'transfer': 3,
    }
    if propability < 0.02:
        return services['loan']
    elif propability < 0.05:
        return services['deposit']
    else:
        return services['transfer']


def fake_transactions(temp_cursor, client_data):
    # structure of table:
    # id serial,
    # source_account_nr INTEGER,
    # destination_account_nr INTEGER,
    # transfer_amount DECIMAL,
    # date date,
    # service_id INTEGER,
    try:
        transaction_data = open(TRANSACTION_HISTORY, 'x')
    except FileExistsError:
        transaction_data = open(TRANSACTION_HISTORY, 'w')

    transaction_data.writelines(transaction_generator(client_data))
    transaction_data.close()
    print("Begin copy from:", TRANSACTION_HISTORY, " ... ")
    temp_cursor.execute(f"""COPY Transactions(
    source_account_nr, 
    destination_account_nr, 
    transfer_amount, 
    date, 
    service_id) FROM '{TRANSACTION_HISTORY}' WITH DELIMITER AS ',';""")


if __name__ == '__main__':
    print('faker')
    conn = create_bank(DB, database='bank')
    cursor = conn.cursor()
    print(cursor.execute(CUSTOM_QUERRY))
    cursor.close()
    conn.close()
    conn = psycopg2.connect(**superuser)
    conn.autocommit = True
    cursor = conn.cursor()
    # print(cursor.execute("""DROP DATABASE bank;"""))
    cursor.close()
    conn.close()


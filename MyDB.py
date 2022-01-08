import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=os.getenv('passwd'),
    database="testdatabase"
    )

mycursor=db.cursor(buffered=True)

def create_db(table_name):
    mycursor.execute(f"CREATE TABLE {table_name} (name VARCHAR(50),password VARCHAR(50), money int UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# create_db('Discord_DB')

def insert_user(name,password):
    mycursor.execute("INSERT INTO Discord_DB (name,password,money) VALUES (%s,%s,%s)", (name,password,1000))
    db.commit()

# insert_user('enemy of my enemy','3977')


def show_entries(table_name):
    user=[]
    mycursor.execute(f"SELECT * FROM {table_name}")
    for i in mycursor:
        print(i)
        user.append(i)
        # return i
    # return [i for i  in mycursor]
    # print([i for i in mycursor])
    return user

# show_entries('Discord_db')

def delete_user(name,password):
    mycursor.execute(f"DELETE FROM Discord_DB WHERE name='{name}' AND password='{password}'")
    db.commit()


# delete_user('enemy of my enemy','3977')


def update_data(password,math,new_value):
    mycursor.execute(f"UPDATE Discord_DB SET money = money {math} {new_value} WHERE password = '{password}'")
    db.commit()

# update_data('3977','+','8995')
# show_entries('Discord_DB')


def delete_db():
    mycursor.execute("DROP TABLE Discord_DB")
    db.commit()

# delete_db()


def show_balance(password):
    mycursor.execute(f"SELECT * FROM Discord_db WHERE password = '{password}'")
    result=mycursor.fetchall()

    for i in result:
        # print(i)
        return f"You have ${i[2]}"
# show_balance('3977')

def balance_check(password):
    mycursor.execute(f"SELECT * FROM Discord_db WHERE password = '{password}'")
    result=mycursor.fetchall()

    for i in result:

        if i[2] >=500:
            print('Welcome to the slots')
            return True

# balance_check('3977')
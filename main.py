from modules.classes import User
from psycopg2 import connect
from random import randint

cnx = connect(user='postgres', password='Coderslab',
                      host='localhost', database='workshop_db')
cnx.autocommit = True
cursor = cnx.cursor()

# test modyfikacji danych

print(f'User o id to: {User.load_user_by_id(cursor, 96)}')
b = User.load_user_by_id(cursor, 96)
b.username = f'Nowa6'
b.email = f'nowymail668@yahoo.pl'
b.set_password(f'xyz46')
b.save_to_db(cursor)
print(f'User o id to: {User.load_user_by_id(cursor, 96)}')

cnx.close()


'testy'
'''
rand = randint(45,150)
a = User()
a.username = f'John{rand}'
a.email = f'asddd{rand}@yahoo.pl'
a.set_password(f'malabuba2{rand}')
a.save_to_db(cursor)

all_users = User.load_all_users(cursor)
for row in all_users:
    print(row)
print(f'Tablica ma {len(all_users)} obiekty/ów')

print(f'User o id {rand} to: {User.load_user_by_id(cursor, rand)}')


test usuwania:

print(f'User o id to: {User.load_user_by_id(cursor, 92)}')
b = User.load_user_by_id(cursor, 92)
b.delete(cursor)
print(b)
all_users = User.load_all_users(cursor)
print(f'Tablica ma {len(all_users)} obiekty/ów')
'''

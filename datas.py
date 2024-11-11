import sqlite3

db = sqlite3.connect('foods.db')
cursor = db.cursor()

async def start_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS foods(
                   type TEXT,
                   price TEXT,
                   name TEXT,
                   photo TEXT,
                   ingridients TEXT)

''')


def add_to_db(type,price,name,photo,ingri):
    cursor.execute('''
INSERT INTO foods(type,price,name,photo,ingridients)
                   VALUES(?,?,?,?,?)
''',(type,price,name,photo,ingri)
    )
    db.commit()


# add_to_db(type='Fast food',price='20000 swm',name='Lavash',
#           photo='AgACAgIAAxkBAAPNZyG67UovZGUjRKi4Fx9L8LwYU5QAArrhMRt80hFJPVbAtP-UCCsBAAMCAANzAAM2BA',
#           ingri='chicken, cheese')

def show_foods():
    cursor.execute('SELECT * FROM foods')
    datas = cursor.fetchall()
    return datas

def add_user():
    pass








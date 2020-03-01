

import psycopg2


conn = psycopg2.connect(user='redmine', password='q1w2', database='redmine', host='192.168.1.3')

cursor = conn.cursor()
cursor.execute('select id, login, firstname, lastname from users;')
r = cursor.fetchall()
print(r)
# conn.commit()
cursor.close()
conn.close



import sqlite3
import csv

conn = sqlite3.connect('jarvis.db') # connect to the database or create a new one
cursor = conn.cursor() # create a cursor object

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# # for opening an application which runs on browser
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Prime Video', '/Applications/Prime Video.app')"  
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'LinkedIn', 'https://www.linkedin.com/feed/')"
# cursor.execute(query)
# conn.commit()  

# query = "INSERT INTO web_command VALUES (null,'whatsapp web', 'https://web.whatsapp.com/')"  
# cursor.execute(query)
# conn.commit()


# for creating table named contacts
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name VARCHAR(200), phone VARCHAR(255), email  VARCHAR(255) NULL) ''')

# for adding contacts in database

# desired_column_indices = [0,15]

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_column_indices]
#         cursor.execute ('''INSERT INTO contacts (id, 'name', 'phone') VALUES (null, ?,? );''', tuple(selected_data) )

# # commit changes and close connection
# conn.commit()
# conn.close()  


# for fetching a single contact from database

# query = "Name"
# query = query.strip().lower()

# cursor.execute("SELECT phone FROM contacts WHERE LOWER(name) LIKE ?", ('%' + query + '%',))
# result = cursor.fetchall()
# print(result[0][0])

import pymysql
# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Aa258258', db='users')
conn.autocommit(True)
# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
# cursor.execute("INSERT into users.players (name, id) VALUES ('john', 5)")
# cursor.execute("INSERT into users.players (name, id) VALUES ('smit', 1)")
# cursor.execute("INSERT into users.players (name, id) VALUES ('Dan', 2)")

# Deleting data into table
# cursor.execute("DELETE FROM users.players WHERE name = 'john'")

# Updating data inside the table
cursor.execute("UPDATE users.players SET id = '10' WHERE name = 'john'")

# Getting all data from table “users”
cursor.execute("SELECT * FROM users.players;")

# Iterating table and printing all users
for row in cursor:
    print(row)
# Must 
cursor.close()
conn.close()
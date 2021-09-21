import sqlite3

conn = sqlite3.connect('DB_new.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()
more_users = [
    ('001', 'Maryna', 'Belokonieva', 'F'), ('002', 'Anatoliy', 'Vasilenko', 'M'), ('003', 'Pavel', 'Gordeichuk', 'M'),
    ('004', 'Ludmyla', 'Denisenko', 'F'), ('005', 'Oleksandr', 'Detenuk', 'M'), ('006', 'Anastasia', 'Dyachenko', 'F'),
    ('007', 'Arthur', 'Kolomiets', 'M'), ('008', 'Nataly', 'Kurylo', 'F'), ('009', 'Vlad', "lyho", 'M'),
    ('010', 'Elen', 'Malisheva', 'F'), ('011', "Tatiana", 'Osadcha', 'F'), ('014', 'Ruslan', "Rusanov", 'M'),
    ('015', "Dmitrii", "Sankov", 'M'), ('016', 'Oleksandr', 'Sologub', 'M'), ('017', 'Oleg', "Foya", 'M'),
    ('018', 'Oleksii', 'Hitsuk', 'M'), ('019', 'Anna', 'Homenko', 'F'), ('020', 'Igor', "Cheketov", 'M'),
    ('021', 'Nazar', 'Shostak', 'M'), ('022', 'Evgen', 'Yarmusevich', 'M'), ('012', 'Anton', 'Pyatigorec', 'M'),
    ('013', 'Olga', 'Puzik', 'F'), ('023', 'Oleksandra', 'Bespala', 'F')
]
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
conn.commit()
cur.execute("SELECT * FROM users;")
result = cur.fetchall()
print(result)
def cr_md():
    import sqlite3
    conn = sqlite3.connect('DB_pbook.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    fname TEXT,
    lname TEXT,
    phone INT PRIMARY KEY);
""")

    conn.commit()
    f_name = str(input("Введите имя: "))
    l_name = str(input("Введите фимилию: "))
    phn_raw = input("Введите номер телефона: ")

    while len(phn_raw) != 10 or not phn_raw.isnumeric():
        if len(phn_raw) != 10 or phn_raw != '':
            print("Номер должен быть в формате - код оператора, телефон ('0676707070') и состоять из 10 цифр")
        phn_raw = input("Введите номер телефона: ")
    phn = int(str(38) + phn_raw)

    user = [(f_name), (l_name), (phn)]
    print(user)

    cur.execute("INSERT INTO users VALUES(?, ?, ?);", user)
    conn.commit()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    print(result)

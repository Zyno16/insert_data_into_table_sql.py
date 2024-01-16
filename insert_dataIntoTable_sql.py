import mysql.connector
try:
    conn = mysql.connector.connect(
        host ="localhost",
        user ="userpython",
        passwd ="123456",
        database ="arabicinfo"
   )
    cur =conn.cursor()
    cur.execute("""insert into emp values (1,'adel')""")
    conn.commit()

except mysql.connector.Error as e:
    print(e)

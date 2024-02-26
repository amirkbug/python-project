import sqlite3



class database():
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS contactss (id INTEGER PRIMARY KEY,name text,lastname text,city text,tell text)""")
        self.con.commit()



    def insert(self,name,lastname,city,tell):
        self.cur.execute("""INSERT INTO contactss VALUES(NULL,?,?,?,?)""",(name,lastname,city,tell))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM contactss")
        rows = self.cur.fetchall()
        return rows

    def remove(self,id):
        self.cur.execute('DELETE FROM contactss WHERE id = ?',(id,))
        self.con.commit()
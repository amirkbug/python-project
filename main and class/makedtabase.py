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


    def update(self,id,name,lastname,city,tell):
        self.cur.execute("""UPDATE contactss SET name = ?, lastname = ? , city = ? , tell = ? WHERE id = ?""",(name,lastname,city,tell,id))
        self.con.commit()


    def search(self,search_variable):
        self.cur.execute('SELECT * FROM contactss WHERE id = ? or name = ? or lastname = ? or city = ? or tell = ?',(search_variable,search_variable,search_variable,search_variable,search_variable))
        search_resault = self.cur.fetchall()
        return search_resault
import sqlite3


class database():
    def __init__(self,db):
        self.con = sqlite3.connect(db)      
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS contact (name text , lastname text , tell integer , city text)')
        self.con.commit()


    def insertcontact(self,name,lastname,tell,city):
        self.cur.execute("""INSERT INTO contact VALUES(?,?,?,?)""",(name,lastname,tell,city))
        self.con.commit()
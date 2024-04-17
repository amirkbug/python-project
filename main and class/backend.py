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

    
    def search_name(self,search_variable):
        self.cur.execute('SELECT * FROM contactss WHERE name = ?',(search_variable,))
        search_resault = self.cur.fetchall()
        return search_resault
    
    def search_lastname(self,search_variable):
        self.cur.execute('SELECT * FROM contactss WHERE lastname = ?',(search_variable,))
        search_resault = self.cur.fetchall()
        return search_resault
    
    def search_city(self,search_variable):
        self.cur.execute('SELECT * FROM contactss WHERE city = ?',(search_variable,))
        search_resault = self.cur.fetchall()
        return search_resault
    
    def search_tell(self,search_variable):
        self.cur.execute('SELECT * FROM contactss WHERE tell = ?',(search_variable,))
        search_resault = self.cur.fetchall()
        return search_resault

    
    def search_with_name(self,search_variable : str):
        search_variable = search_variable.replace('?','_').replace('*','%')
        self.cur.execute('SELECT * FROM contactss WHERE name like ?',(search_variable,))
        search_resault_underscore = self.cur.fetchall()
        return search_resault_underscore
    
    def search_with_lastname(self,search_variable):
        search_variable = search_variable.replace('?','_').replace('*','%')
        self.cur.execute('SELECT * FROM contactss WHERE lastname like ?',(search_variable,))
        search_resault_underscore = self.cur.fetchall()
        return search_resault_underscore
    
    def search_with_city(self,search_variable):
        search_variable = search_variable.replace('?','_').replace('*','%')
        self.cur.execute('SELECT * FROM contactss WHERE city like ?',(search_variable,))
        search_resault_underscore = self.cur.fetchall()
        return search_resault_underscore
    
    

    
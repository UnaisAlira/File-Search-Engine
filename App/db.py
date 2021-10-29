from tkinter.constants import TRUE
import psycopg2
import logging
logging.basicConfig(filename="e.log",level=logging.ERROR) #error logger

class database:
    #creating connection
    def conn(self):
        self.con=psycopg2.connect(host="localhost",database="searchEngine",user="postgres",password="admin")
        return self.con
    #adding record
    def addrecord(self,data):
        self.table()
        con=self.conn()
        cur=con.cursor()
        query="insert into records(history) values('{}')"
        cur.execute(query.format(data))
        con.commit()
    #creating table
    def table(self):
        con=self.conn()
        cur=con.cursor()
        try:
            ##cur.execute("drop table records")
            cur.execute("create table records(history varchar(200))")
            con.commit()
        except Exception:
            logging.exception(Exception) #writing error onto log file
    #searching record in database
    def search_db(self,values):
        data=values['term'].strip() # removing trailing and leading spaces
        self.table()
        con=self.conn()
        cur=con.cursor()
        if values['term'].replace(" ","") == "":
            return TRUE
        # We are using exceptional handler to check whether the user have chhosen a choice  
        # You can default a choice and avoid using exception handler
        try:
            if(values['contains']):
                query="select history from records where history ~* '/*{}' " #file that contains given search term
                cur.execute(query.format(data))
                con.commit()
                rows = cur.fetchall()
            elif(values['endswith']):
                query="select history from records where history ~* '/*{}$' "#file that ends with given search term
                cur.execute(query.format(data))
                con.commit()
                rows = cur.fetchall()
            elif(values['beginswith']):
                query="select history from records where history ~* '/{}' " #file that begins with given search term
                cur.execute(query.format(data))
                con.commit()
                rows = cur.fetchall()
            elif(values['file']):
                query="select history from records where history ~* '/{}$' " #file with given search term
                cur.execute(query.format(data))
                con.commit()
                rows = cur.fetchall()
            if rows:
                self.show_db_results(rows)
                return TRUE
        except Exception:
            print("Enter the choice")
            return TRUE

    def show_db_results(self,rows):
        print("-----From database-----")
        for row in rows:
            print(row[0])


import sqlite3

class Escale:
    def __init__(self,IDESC,APORTESC,HARRESC,DURESC,NOORD,NUMVOL):
        self.IDESC=IDESC
        self.APORTESC=APORTESC
        self.HARRESC=HARRESC
        self.DURESC=DURESC
        self.NOORD=NOORD
        self.NUMVOL=NUMVOL

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn
    
    @staticmethod
    def get_all_escale(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM escale WHERE IDESC=?",(idesc,))
        row = cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_escale_by_numvol(numvol):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM escale WHERE NUMVOL=?",(numvol,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_heure_arrive(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT HARRESC FROM escale WHERE IDESC = ?",(idesc,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row["HARRESC"]
        return None
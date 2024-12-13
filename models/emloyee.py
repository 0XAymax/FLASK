import sqlite3

class Employee:
    def __init__(self,NUMEMP,NOM,prenom,email,password,tel,ville,adresse,salaire,FONCTION,datemb,NBMHV,NBTHV):
        self.NUMEMP = NUMEMP
        self.NOM = NOM
        self.prenom = prenom
        self.email = email
        self.password = password
        self.tel = tel
        self.ville = ville
        self.adresse = adresse
        self.salaire = salaire
        self.FONCTION = FONCTION
        self.datemb = datemb
        self.NBMHV = NBMHV
        self.NBTHV = NBTHV
    
    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn    

    @staticmethod
    def get_all():
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees ")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_by_id(employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_by_full_name(self, last_name, first_name):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE NOM = ? AND prenom = ?", (last_name, first_name))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None

    def get_by_email(self, email):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE email = ?", (email,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_by_city(self, city):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE ville = ?", (city,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None

    def get_by_function(self, function):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE FONCTION = ?", (function,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None

    def get_by_salary_range(self, min_salary, max_salary):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE salaire BETWEEN ? AND ?", (min_salary, max_salary))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None

    def get_full_name_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NOM, prenom FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_email_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT email FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_password_hash_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT password FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_phone_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT tel FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_address_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT adresse FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def get_salary_by_id(self, employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT salaire FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def set_full_name(self, employee_id, last_name, first_name):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET NOM = ?, prenom = ? WHERE NUMEMP = ?", (last_name, first_name, employee_id))
        conn.commit()
        conn.close()

    def set_email(self, employee_id, email):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET email = ? WHERE NUMEMP = ?", (email, employee_id))
        conn.commit()
        conn.close()
        
    def set_password_hash(self, employee_id, password_hash):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET password = ? WHERE NUMEMP = ?", (password_hash, employee_id))
        conn.commit()
        conn.close()

    def set_phone(self, employee_id, phone):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET tel = ? WHERE NUMEMP = ?", (phone, employee_id))
        conn.commit()
        conn.close()

    def set_address(self, employee_id, address):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET adresse = ? WHERE NUMEMP = ?", (address, employee_id))
        conn.commit()
        conn.close()

    def set_salary(self, employee_id, salary):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET salaire = ? WHERE NUMEMP = ?", (salary, employee_id))
        conn.commit()
        conn.close()

    def set_city(self, employee_id, city):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET ville = ? WHERE NUMEMP = ?", (city, employee_id))
        conn.commit()
        conn.close()

    def set_function(self, employee_id, function):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET FONCTION = ? WHERE NUMEMP = ?", (function, employee_id))
        conn.commit()
        conn.close()

    def create(self, email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO employees (email, password, NOM, prenom, tel, ville, adresse, salaire, FONCTION, datemb)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb))
        conn.commit()
        conn.close()

class FL_Employee(Employee):
    def get_NBMHV(self,id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NBMHV FROM employees WHERE NUMEMP=?",(id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    def get_NBTHV(self,id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NBTHV FROM employees WHERE NUMEMP=?",(id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    def set_NBMHV(self, employee_id, NBMHV):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET NBMHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))
        conn.commit()
        conn.close()

    def set_NBTHV(self, employee_id, NBMHV):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET NBTHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))
        conn.commit()
        conn.close()

    def create(self, email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):
        super().create(email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb)
        employee = self.get_by_email(email)
        if employee:
            employee_id = employee[0][0]
            self.set_NBMHV(employee_id, 0)
            self.set_NBTHV(employee_id, 0)
        else:
            raise ValueError(f"Employee with email {email} not found.")

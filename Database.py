import mysql.connector as cnn
class Database :
    def __init__(self , host ,user, password  , database):
        self.host = host 
        self.user = user 
        self.password = password 
        self.database = database
        self.connection = None
        self.cursor = None

    
    def connect(self):
        self.connection  = cnn.connect(
            host = self.host, 
            user = self.user,
            password = self.password, 
            database = self.database
        )
        self.cursor = self.connection.cursor()


    def disconnect(self):
        if self.connection.is_connected:
            self.cursor.close()
            self.connection.close()
    

    def employees_table(self):
        self.connect()
        query = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
                MATRICULE VARCHAR(20) PRIMARY KEY,
                NOM VARCHAR(20) NOT NULL,
                PRENOM VARCHAR(20) NOT NULL,
                SALAIRE_MENSUEL FLOAT NOT NULL
            );
            """
        self.cursor.execute(query)
        self.disconnect()
        
    def paiements_table(self):
        self.connect()
        query = """CREATE TABLE IF NOT EXISTS PAIEMENTS (
                ID INT AUTO_INCREMENT ,
                MATRICULE VARCHAR(20)  NOT NULL,
                ANNEE INT NOT NULL ,
                MOIS VARCHAR(20) NOT NULL,
                JOUR INT NOT NULL,
                MONTANT FLOAT NOT NULL ,
                PRIMARY KEY (ID ,MATRICULE),
                CONSTRAINT FK_MATR FOREIGN KEY (MATRICULE) REFERENCES EMPLOYEE(MATRICULE) ON DELETE CASCADE
                );

            """
        self.cursor.execute(query)
        self.disconnect()

    def fetch_employees(self):
        self.connect()
        query = """SELECT * FROM EMPLOYEE"""
        self.cursor.execute(query)
        employee = self.cursor.fetchall()
        self.disconnect()
        return employee
    
    def fetch_paiements(self):
        self.connect()
        query = """SELECT * FROM PAIEMENTS"""
        self.cursor.execute(query)
        employee = self.cursor.fetchall()
        self.disconnect()
        return employee
    def history (self):
        self.connect()
        query = """SELECT E.MATRICULE , NOM ,PRENOM , ANNEE , MOIS ,JOUR ,  MONTANT , SALAIRE_MENSUEL - MONTANT AS RESTE
        FROM EMPLOYEE E , PAIEMENTS P WHERE P.MATRICULE = E.MATRICULE"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    

    def matricule_exists(self, matricule):
        self.connect()
        query = "SELECT COUNT(*) FROM EMPLOYEE WHERE MATRICULE= %s"
        self.cursor.execute(query ,(matricule,))
        matric = self.cursor.fetchone()[0]
        self.disconnect()
        return matric > 0
    
    def insert_employee(self, matricule, nom , prenom , salaire):
        self.connect()
        query = """INSERT INTO EMPLOYEE VALUES (%s , %s ,%s, %s)"""
        self.cursor.execute(query, (matricule, nom , prenom , salaire ,))
        self.connection.commit()
        self.disconnect()

    def insert_paiements(self, matricule, annee , mois, jour , montant):
        self.connect()
        query = """INSERT INTO PAIEMENTS (MATRICULE, ANNEE, MOIS, JOUR, MONTANT) VALUES (%s , %s ,%s, %s , %s)"""
        self.cursor.execute(query, (matricule,  annee , mois, jour , montant ,))
        self.connection.commit()
        self.disconnect()

    def delete_employee(self, matricule):
        self.connect()
        query = " DELETE FROM EMPLOYEE WHERE MATRICULE = %s"
        self.cursor.execute(query,(matricule,))
        self.connection.commit()
        self.disconnect()

    def delete_paiements(self, matricule):
        self.connect()
        query = " DELETE FROM PAIEMENTS WHERE MATRICULE = %s"
        self.cursor.execute(query,(matricule,))
        self.connection.commit()
        self.disconnect()


    def search_by_emp(self , matricule  , annee , mois ):
        self.connect()
        if not (matricule):
            query = """SELECT E.MATRICULE , NOM ,PRENOM , ANNEE , MOIS ,JOUR ,  MONTANT , SALAIRE_MENSUEL - MONTANT AS RESTE
            FROM EMPLOYEE E , PAIEMENTS P WHERE P.MATRICULE = E.MATRICULE AND ANNEE = %s AND MOIS = %s"""
            self.cursor.execute(query ,(annee , mois ,))
        else :
            query = """SELECT E.MATRICULE , NOM ,PRENOM , ANNEE , MOIS ,JOUR ,  MONTANT , SALAIRE_MENSUEL - MONTANT AS RESTE
            FROM EMPLOYEE E , PAIEMENTS P WHERE P.MATRICULE = E.MATRICULE  AND E.MATRICULE = %s AND ANNEE = %s AND MOIS = %s"""
            self.cursor.execute(query ,( matricule ,annee , mois ,))
        result = self.cursor.fetchall()
        self.disconnect()
        return result
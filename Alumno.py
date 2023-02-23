import mysql.connector

class Alumnos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="db4free.net", user="adminmiyazato", 
        passwd="gonzalezdojo", database="gonzalezdojodb")

    def __str__(self):
        datos=self.consulta_alumno()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_alumno(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Alumno")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_alumno(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM Alumno WHERE id_alumno = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_alumno(self,nombre, apellido, edad, categoria):
        cur = self.cnn.cursor()
        sql='''INSERT INTO Alumno (nombre, apellido, edad, categoria) 
        VALUES('{}', '{}', '{}', '{}')'''.format(nombre, apellido, edad, categoria)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_alumno(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Alumno WHERE id_alumno = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_alumno(self,Id, nombre, apellido, edad, categoria):
        cur = self.cnn.cursor()
        sql='''UPDATE Alumno SET nombre='{}', apellido='{}', edad='{}',
        categoria='{}' WHERE id_alumno={}'''.format(nombre, apellido, edad, categoria,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n

    def busca_users(self, users):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM Usuario WHERE Usuario = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM Usuario WHERE contraseña = {}".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx 

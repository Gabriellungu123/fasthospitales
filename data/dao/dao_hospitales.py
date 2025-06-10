from data.modelo.hospitales import hospitales

class Daohospitales:
    #hacer el select 
    def get_all(self, db) -> list[hospitales]:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hospitales")
        hospitales_en_db= cursor.fetchall()
        lista_hospitales : list[hospitales]=[]
        for hospital in hospitales_en_db:
            obj = hospitales(hospital[0], hospital[1], hospital[2],)
            lista_hospitales.append(obj)
        cursor.close()
        return lista_hospitales
    #Hacer el Añadir

    def insert(self, db, id : int, nombre:str, numero_pacientes: int):
        cursor= db.cursor()
        sql = "INSERT INTO hospitales (id, nombre, numero_pacientes) VALUES (%s,%s,%s) "
        data = ( id, nombre, numero_pacientes)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()

    #Hacer el borrar 

    def delete(self, db, nombre : str):
        cursor = db.cursor()
        sql = "DELETE FROM hospitales WHERE nombre = %s"
        data = (nombre)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()


    #Hacer el actualizar 
    def update(self, db , id: int, nombre:str, numero_pacientes: int):
        cursor=db.cursor()
        sql = "UPDATE hospitales id = %s, numero_pacientes = %s WHERE nombre = %s "
        data= (id, nombre, numero_pacientes )
        cursor.execute(sql, data)
        db.commit()
        cursor.close()
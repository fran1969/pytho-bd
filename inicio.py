import sqlite3
def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)


def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO Contratos(Cod_Tec, Anno, Tipo_Cont, Nombre_Largo, Nombre_Corto) VALUES(?, ?, ?, ?, ?)', entities)
    
    con.commit()

#def sql_update(con):

#    cursorObj = con.cursor()

#    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

#    con.commit()

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

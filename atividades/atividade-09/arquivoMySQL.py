import mysql.connector

def ifPassarInDb(id, N1, N2, faltas):
    aprovado_sn = not ((faltas >= 20) or (((N1+N2)/2) < 6)) #define se o aluno passou ou não
    
    mycursor.execute('UPDATE TB_ALUNOS SET Aprovado_SN = %s WHERE id = %s;', (aprovado_sn, id))

    
mydb = mysql.connector.connect(
  host="localhost",
  user="myuser",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_ALUNOS (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT,
  nota_N1 DECIMAL(4,2),
  nota_N2 DECIMAL(4,2),
  faltas INT,
  Aprovado_SN BOOLEAN
);""")

mycursor.executemany('INSERT INTO TB_ALUNOS (nome, nota_N1, nota_N2, faltas) VALUES (%s, %s, %s, %s);', [
    ("Arthur de Araujo", 8, 5, 15),
    ("Vitória Oliveira", 10, 10, 0),
    ("Lucas Costa", 10, 2, 1),
    ("Sabrinna do Nascimento", 7, 0, 30)
])

mydb.commit()

mycursor.execute("SELECT * FROM TB_ALUNOS")
meuresultado = mycursor.fetchall()

for item in meuresultado:
    id, nome, nota_N1, nota_N2, faltas, aprovado_sn = item

    ifPassarInDb(id, nota_N1, nota_N2, faltas)

mydb.commit()

mycursor.execute("SELECT * FROM TB_ALUNOS")
meuresultado = mycursor.fetchall()

print()

for item in meuresultado:
    print(item)

mycursor.close()
mydb.close()
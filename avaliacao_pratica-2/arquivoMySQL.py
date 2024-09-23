import mysql.connector
import time

def ifPassarInDb(id_matricula, N1, N2, faltas, cursor):
    aprovado_sn = not ((faltas >= 20) or (((2*N1 + 3*N2) / 5) < 6))  # Define se o aluno passou ou não
    cursor.execute('UPDATE TB_MATRICULA SET aprovado_SN = %s WHERE id_matricula = %s;', ("APROVADO" if aprovado_sn else "REPROVADO", id_matricula))

# Conexão com o banco de dados
i = 1
while True:
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="myuser",
            password="mypassword",
            database="mydatabase"
        )
    except:
        notInit = True
        print("\r             ", end='')
        print(f"\rCarregando{'.' * ((i % 3) + 1)}", end='')
        i+=1
        time.sleep(0.5)
    else:
        print("\nO servidor MySQL foi iniciado!")
        break

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_ALUNO (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT,
        nome_aluno TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_DISCIPLINA (
        id_disciplina INT PRIMARY KEY AUTO_INCREMENT,
        nome_disciplina TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_PROFESSOR (
        id_professor INT PRIMARY KEY AUTO_INCREMENT,
        nome_professor TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_MATRICULA (
        id_matricula INT PRIMARY KEY AUTO_INCREMENT,
        id_aluno INT NOT NULL,
        id_disciplina INT NOT NULL,
        id_professor INT,
        nota_N1 DECIMAL(4,2),
        nota_N2 DECIMAL(4,2),
        faltas INT,
        aprovado_SN varchar(9),
        FOREIGN KEY (id_aluno) REFERENCES TB_ALUNO(id_aluno),
        FOREIGN KEY (id_professor) REFERENCES TB_PROFESSOR(id_professor),
        FOREIGN KEY (id_disciplina) REFERENCES TB_DISCIPLINA(id_disciplina)
    )
""")


conn.commit()


cursor.executemany('INSERT INTO TB_ALUNO (nome_aluno) VALUES (%s);', [
    ("Arthur de Araujo",),
    ("Vitória Oliveira",),
    ("Lucas Costa",),
    ("Sabrinna do Nascimento",)
])

cursor.executemany('INSERT INTO TB_DISCIPLINA (nome_disciplina) VALUES (%s);', [
    ("Cálculo I",),
    ("POO",),
    ("Engenharia de Software",)
])

cursor.executemany('INSERT INTO TB_PROFESSOR (nome_professor) VALUES (%s);', [
    ("Gêvane",),
    ("Roger",),
    ("Taveira",)
])

cursor.executemany('INSERT INTO TB_MATRICULA (id_aluno, id_disciplina, id_professor, nota_N1, nota_N2, faltas) VALUES (%s, %s, %s, %s, %s, %s);', [
    (1, 1, 1, 8, 5, 15),
    (1, 2, 2, 8, 5, 15),
    (2, 2, 2, 10, 10, 0),
    (3, 3, 3, 10, 2, 1),
    (4, 3, 3, 7, 0, 30)
])

conn.commit()


cursor.execute("SELECT id_matricula, nota_N1, nota_N2, faltas FROM TB_MATRICULA")
matriculas = cursor.fetchall()

for matricula in matriculas:
    id_matricula, nota_N1, nota_N2, faltas = matricula
    ifPassarInDb(id_matricula, nota_N1, nota_N2, faltas, cursor)

conn.commit()


cursor.execute("""
    SELECT A.nome_aluno, D.nome_disciplina, M.aprovado_SN
    FROM TB_MATRICULA M
    JOIN TB_ALUNO A ON M.id_aluno = A.id_aluno
    JOIN TB_DISCIPLINA D ON M.id_disciplina = D.id_disciplina
""")
matriculas = cursor.fetchall()

print()
for matricula in matriculas:
    print(matricula)

cursor.close()
conn.close()
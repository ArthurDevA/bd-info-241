import mysql.connector

def tipoRerov(id_matricula, faltas):
    if faltas >= 20:
        return "Reprovado por Falta"
    else:
        return "Reprovado por Média"

# Conexão com o banco de dados
conn = mysql.connector.connect(
  host="localhost",
  user="myuser",
  password="mypassword",
  database="mydatabase"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT M.id_matricula, A.nome_aluno, D.nome_disciplina, P.nome_professor, M.nota_N1, M.nota_N2, M.faltas, M.aprovado_SN
    FROM TB_MATRICULA M
    JOIN TB_ALUNO A ON M.id_aluno = A.id_aluno
    JOIN TB_DISCIPLINA D ON M.id_disciplina = D.id_disciplina
    JOIN TB_PROFESSOR P ON M.id_professor = P.id_professor
    WHERE M.aprovado_SN = "REPROVADO"
""")
matriculas = cursor.fetchall()


print("\nAlunos reporovados:")
for matricula in matriculas:
    id_matricula, nome_aluno, nome_disciplina, nome_professor, nota_N1, nota_N2, faltas, aprovado_SN = matricula
    tipoR = tipoRerov(id_matricula, faltas)
    print("ID: %s, Aluno: %s, Disciplina: %s, Professor: %s, Nota_N1: %s, Nota_N2: %s, Faltas: %s, Status: %s" % (id_matricula, nome_aluno, nome_disciplina, nome_professor, nota_N1, nota_N2, faltas, tipoR))
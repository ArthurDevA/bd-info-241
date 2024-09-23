import mysql.connector

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
    WHERE M.aprovado_SN = "APROVADO"
""")
matriculas = cursor.fetchall()
tipoR = "Aprovado por Média"

print("\nAlunos reporovados:")
for matricula in matriculas:
    id_matricula, nome_aluno, nome_disciplina, nome_professor, nota_N1, nota_N2, faltas, aprovado_SN = matricula
    
    print((nome_aluno, nome_disciplina, nome_professor, nota_N1, nota_N2, faltas, tipoR))
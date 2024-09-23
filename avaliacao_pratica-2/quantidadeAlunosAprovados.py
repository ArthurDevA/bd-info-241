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
    SELECT * FROM TB_MATRICULA
    WHERE aprovado_SN = "APROVADO"
""")
matriculas = cursor.fetchall()
qtdAprov = len(matriculas)

print("\nQuantidade de alunos aprovados:", qtdAprov)
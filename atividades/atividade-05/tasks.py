import sqlite3

def create_connection():
    connection = sqlite3.connect('example.db')
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    ''')
    
    connection.commit()
    connection.close()

def create_user(name, age):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
    ''', (name, age))
    
    connection.commit()
    connection.close()

def read_users():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    
    connection.close()
    return rows

def update_user(user_id, name, age):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    UPDATE users
    SET name = ?, age = ?
    WHERE id = ?
    ''', (name, age, user_id))
    
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    DELETE FROM users
    WHERE id = ?
    ''', (user_id,))
    
    connection.commit()
    connection.close()

def delete_table(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute(f'''
    DROP TABLE IF EXISTS {table_name}
    ''')
    
    connection.commit()
    connection.close()

# Exemplo de uso de todas as funções

# Criação da tabela
create_table()

# Inserção de usuários
create_user('Alice', 30)
create_user('Bob', 25)
create_user('Charlie', 35)

# Leitura de todos os usuários
print("Usuários após inserção:")
users = read_users()
for user in users:
    print(user)

# Atualização de um usuário
update_user(1, 'Alice Smith', 31)

# Leitura de todos os usuários após atualização
print("\nUsuários após atualização:")
users = read_users()
for user in users:
    print(user)

# Deleção de um usuário
delete_user(2)

# Leitura de todos os usuários após deleção
print("\nUsuários após deleção:")
users = read_users()
for user in users:
    print(user)

# Deleção da tabela
delete_table('users')

# Tentativa de leitura após deleção da tabela (deve falhar se a tabela não existir mais)
print("\nTentativa de leitura após deleção da tabela:")
try:
    users = read_users()
    for user in users:
        print(user)
except sqlite3.OperationalError as e:
    print(f"Erro: {e}")
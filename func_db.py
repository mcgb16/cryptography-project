import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pswdhere',
    database='dbcryptography'
)

cursor = conn.cursor()

def save_text_on_db(key, name, text, cpf):
    insert_command = f"""INSERT INTO encrypted_texts (`Key`, Name, Decrypted_Text, Cpf) VALUES ('{key}', '{name}', '{text}', '{cpf}')"""
    cursor.execute(insert_command)
    conn.commit()
    return 'Informações inseridas no banco de dados.'

def save_file_on_db():
    pass

def deactivate_db_connection():
    cursor.close()
    conn.close()
    return 'Conexão desativada com o banco de dados.'

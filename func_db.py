import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pswdhere',
    database='dbcryptography'
)

cursor = conn.cursor()

def save_text_on_db(key, name, text, cpf):
    insert_command = f"""INSERT INTO encrypted_texts (Decryp_Key, Name, Decrypted_Text, Cpf) VALUES ('{key}', '{name}', '{text}', '{cpf}')"""
    cursor.execute(insert_command)
    conn.commit()
    return 'Informações inseridas no banco de dados.'

def save_file_on_db(key, name, cpf, file_name, file_dir):
    insert_command = f"""INSERT INTO encrypted_files (Decryp_Key, Name, Cpf, File_Name, File_Dir) VALUES ('{key}', '{name}', '{cpf}', '{file_name}', '{file_dir}')"""
    cursor.execute(insert_command)
    conn.commit()
    return 'Informações inseridas no banco de dados.'

def search_text_on_db(key, cpf):
    select_command = f"""SELECT Name, Decrypted_Text FROM encrypted_texts WHERE Decryp_Key='{key}' AND Cpf = '{cpf}'"""
    cursor.execute(select_command)
    
    result = cursor.fetchone()
    if result == None:
        return 'not found', 'Não foram encontrados registros no banco de dados com os dados informados.'
    else:
        return 'found', result

def search_file_on_db(key, cpf):
    select_command = f"""SELECT Name, File_Name, File_Dir FROM encrypted_files WHERE Decryp_Key='{key}' AND Cpf = '{cpf}'"""
    cursor.execute(select_command)
    
    result = cursor.fetchone()
    if result == None:
        return 'not found', 'Não foram encontrados registros no banco de dados com os dados informados.'
    else:
        return 'found', result

def deactivate_db_connection():
    cursor.close()
    conn.close()
    return 'Conexão desativada com o banco de dados.'

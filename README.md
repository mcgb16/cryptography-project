# Overview Geral do Projeto

- Linguagem de programação: Python
- Banco de Dados: MySQL
- Biblioteca para GUI: TKinter

# Funcionalidades

Em progresso...

# Overview das Classes e Funções/Métodos

## main.py
- Page
    - __init__(self, title)
    - show_pages(self)
- MainPage(Page)
    - show_pages(self)
    - open_next_page(self,title)
    - check_data(self, cryp_type)
    - validate_input_len(self, P, input_type)
    - update_label_when_digit(self, event)
    - create_common_widgets(self, cryp_type)
    - create_common_fields(self, cryp_type)
    - generate_pdf_file(self, encrypted_text, key, user_name, cryp_type)
    - search_file(self)
    - check_decryp(self, cryp_type)
    - check_picklist_selection(self, selection)

## func.py
- verify_cpf(user_cpf)
- verify_len_input_cryp(cpf, name, text_to_encrypt)
- generate_encrypted_data(text_to_crypt)
- generate_unique_key()
- generate_pdf_files(main_txt, pdf_type, user_name, file_name)
- pdf_files_controller(encrypted_text, key, user_name, cryp_type, file_name='')
- send_text_to_db(key, name, text, cpf)
- search_file()
- generate_encrypted_file(encrypted_data, file_name, file_dir)
- move_file_to_server(file_dir, file_name)
- send_file_to_db(key, name, cpf, file_name, file_dir)
- search_on_db(key, cpf, decryp_type)
- verify_len_input_decryp(cpf, key, picklist)
- save_decrypted_file(file_name, file_dir)

## func_db.py
- save_text_on_db(key, name, text, cpf)
- save_file_on_db(key, name, cpf, file_name, file_dir)
- search_text_on_db(key, cpf)
- search_file_on_db(key, cpf)
- deactivate_db_connection()
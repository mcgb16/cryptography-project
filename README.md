# Overview Geral do Projeto

- Linguagem de programação: Python
- Banco de Dados: MySQL
- Biblioteca para GUI: TKinter

# Funcionalidades

Em progresso...

# Overview das Classes e Funções/Métodos

## main.py
- Page [Classe]
    - __init__(self, title)
        - Método init padrão de classes, o qual foi utilizado para setar alguns valores que serão comuns entre todas as páginas a serem criadas.
    - show_pages(self)
        - Método vazio que será melhor desenvolvido nas classes que herdarem de Page.
- MainPage(Page) [Classe]
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
    - Função que irá receber o CPF digitado pelo usuário na tela e irá efetuar a validação se o CPF é válido ou não.
- verify_len_input_cryp(cpf, name, text_to_encrypt)
    - Função que verifica se todos os campos, nos layouts de criptografia (textos ou arquivos), foram preenchidos.
- generate_encrypted_data(text_to_crypt)
    - Função que executa a criptografia do que foi escrito pelo usuário, na criptografia de textos.
    - Função que executa a criptografia do path do arquivo selecionado pelo usuário, a qual será inserida no conteúdo do arquivo.
- generate_unique_key()
    - Função que gera a key única para descriptografia.
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
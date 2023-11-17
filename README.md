# Overview Geral do Projeto

- Linguagem de programação: Python
- Banco de Dados: MySQL
- Biblioteca para GUI: TKinter

# Funcionalidades

**OBSERVAÇÃO: Não levar em consideração o design do layout, o intuito do projeto não era se preocupar com o design.**

### Criptografia de Textos
1. Na primeira tela, selecionar a opção "Criptografar Textos".
2. Preencher todos os campos de Nome, CPF e Texto para Criptografar. Lembrando que temos as seguintes validações:
    1. Todos os campos precisam estar preenchidos.
    2. O CPF precisa ser válido.
    3. O texto precisa ter 255 caracteres ou menos.
3. Ao clicar em criptografar, irá abrir os dois componentes de Texto Criptografado e Key para Descriptografia.
4. Caso opte, é possível gerar dois arquivos PDF, com um contendo o texto criptografado e o outro a key.
5. Caso queira resetar a tela, clique em Reset no canto inferior direito.
6. Caso queira voltar a tela inicial, clique em Página Inicial no canto inferior direito.

### Criptografia de Arquivos

### Descriptografia

# Overview das Classes e Funções/Métodos

### main.py
- Page [Classe]
    - __init__(self, title)
        - Método init padrão de classes, o qual foi utilizado para setar alguns valores que serão comuns entre todas as páginas a serem criadas.
    - show_pages(self)
        - Método vazio que será melhor desenvolvido nas classes que herdarem de Page.
- MainPage(Page) [Classe]
    - show_pages(self)
        - Método responsável por abrir as 4 páginas disponíveis no aplicativo (inicial, criptografia de textos, criptografia de arquivos e descriptografia.).
        - A partir deste método outros serão chamados de acordo com os cliques dos botões e alguns até mesmo automaticamente após abrir a página.
    - open_next_page(self,title)
        - Método responsável por abrir uma das páginas do método anterior, se baseando em seu parâmetro "title".
    - check_data(self, cryp_type)
        - Método que chama todas as funções necessárias, automaticamente, no processo de criptografia.
        - Principal método utilizado na página de criptografia, pois todo o fluxo acaba passando por ele.
    - validate_input_len(self, P, input_type)
        - Método que verifica o comprimento dos dois campos de Nome e CPF das páginas que os possuem.
        - Ele verifica em tempo real o comprimento desses campos conforme o usuário digita, para que não seja possível inserir mais caracteres do que é aceito.
    - update_label_when_digit(self, event)
        - Método que modifica a label de contagem de caracteres do campo de inserir texto a ser criptografado.
    - create_common_widgets(self, cryp_type)
        - Método que cria widgets/campos padrão para as páginas, assim o código pode ser reutilizado quando preciso.
    - create_common_fields(self, cryp_type)
        - Método que cria campos/widgets padrão para as páginas, assim o código pode ser reutilizado quando preciso.
    - generate_pdf_file(self, encrypted_text, key, user_name, cryp_type)
        - Método que chama as funções do arquivo "func.py" referentes a criação dos arquivos PDF.
    - search_file(self)
        - Método que chama a função "search_file()" do arquivo "func.py".
    - check_decryp(self, cryp_type)
        - Método que chama todas as funções necessárias, automaticamente, no processo de descriptografia.
        - Principal método utilizado na página de descriptografia, pois todo o fluxo acaba passando por ele.
    - check_picklist_selection(self, selection)
        - Método que verifica qual opção foi escolhida na lista de valores da página de descriptografia.

### func.py
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
    - Função que cria (sendo possível escolher onde ele será salvo no sistema) e formata um PDF de acordo com a finalidade dele (para armazenar o texto criptografado, para armazenar a chave de descriptografia, para criptografar um arquivo PDF).
- pdf_files_controller(encrypted_text, key, user_name, cryp_type, file_name='')
    - Função que serve de controladora da função "generate_pdf_files". É nela que os valores enviados para a outra função são setados com mais precisão.
- send_text_to_db(key, name, text, cpf)
    - Função que aciona a função do arquivo "func_db", a qual é utilizada para salvar o texto descriptografado no banco de dados, o nome do usuário, o CPF e a chave de descriptografia.
- search_file()
    - Função que é utilizada para efetuar a busca por arquivos no sistema.
- generate_encrypted_file(encrypted_data, file_name, file_dir)
    - Função que efetua a criptografia do arquivo de acordo com sua extensão.
    - As extensões permitidas são: docx, xlsx, pdf, md, txt.
- move_file_to_server(file_dir, file_name)
    - Função que move o arquivo original de seu diretório para o diretório do servidor, o qual servirá para armazenas os arquivos originais para serem buscados depois.
- send_file_to_db(key, name, cpf, file_name, file_dir)
    - Função que aciona a função do arquivo "func_db", a qual é utilizada para salvar o diretório do arquivo descriptografado no banco de dados, o nome do arquivo, o nome do usuário, o CPF e a chave de descriptografia.
- search_on_db(key, cpf, decryp_type)
    - Função que aciona as funções do arquivo "func_db", as quais efetuam a busca no banco de dados pelos textos ou arquivos descriptografados.
    - O parâmetro "decryp_type" é utilizado para que o sistema saiba se ele precisa efetuar a busca na tabela de textos ou na tabela de arquivos.
- verify_len_input_decryp(cpf, key, picklist)
    - Função que verifica se todos os campos, no layout de descriptografia, foram preenchidos.
- save_decrypted_file(file_name, file_dir)
    - Função que seleciona onde será salvo o arquivo descriptografado no sistema (após ser buscado no banco de dados/servidor).

### func_db.py
- save_text_on_db(key, name, text, cpf)
    - Função que efetua o salvamento do texto descriptografado no banco de dados.
    - Todos os parâmetros são referentes às colunas da tabela, sendo a "Key" a primary key.
- save_file_on_db(key, name, cpf, file_name, file_dir)
    - Função que efetua o salvamento do diretório do arquivo descriptografado, no servidor, no banco de dados.
    - Todos os parâmetros são referentes às colunas da tabela, sendo a "Key" a primary key.
- search_text_on_db(key, cpf)
    - Função que efetua a busca pela tabela de textos descriptografados a partir da Key juntamente com o CPF.
    - OBS: Ambos precisam estar condizentes para ser encontrado o resultado.
- search_file_on_db(key, cpf)
    - Função que efetua a busca pela tabela de arquivos descriptografados a partir da Key juntamente com o CPF.
    - OBS: Ambos precisam estar condizentes para ser encontrado o resultado.
- deactivate_db_connection()
    - Função utilizada para finalizar a conexão com o banco de dados.
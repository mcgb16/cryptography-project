import func
import tkinter

class Page:
    def __init__(self, title):
        self.title = title
        self.root = tkinter.Tk()
        x = (self.root.winfo_screenwidth() - 800)//2
        y = (self.root.winfo_screenheight() - 600)//2
        self.geometry = f'800x600+{x}+{y}'
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.show_pages()

    def show_pages(self):
        pass

class MainPage(Page):
    def show_pages(self):
        if self.title == 'Cryptography App':
            encrypt_text_button = tkinter.Button(self.root, text="Criptografar Textos", command=lambda: self.open_next_page('Criptografar Textos'))
            encrypt_text_button.pack()
            encrypt_text_button = tkinter.Button(self.root, text="Criptografar Arquivos", command=lambda: self.open_next_page('Criptografar Arquivos'))
            encrypt_text_button.pack()
        elif self.title == 'Criptografar Textos':
            cryp_type = 'text'
            self.create_common_fields()
            
            self.label_var_per_digit = tkinter.StringVar()
            self.label_var_per_digit.set(255)
            self.text_to_encrypt_label = tkinter.Label(self.root, text='Insira o texto para criptografar. Quantidade de caracteres digitados: ')
            self.text_to_encrypt_label.pack()
            self.text_to_encrypt_label_var = tkinter.Label(self.root, textvariable=self.label_var_per_digit)
            self.text_to_encrypt_label_var.pack()
            self.insert_text_to_encrypt=tkinter.Text(self.root,wrap='word',height=4)
            self.insert_text_to_encrypt.pack()
            self.insert_text_to_encrypt.bind("<KeyRelease>",self.update_label_when_digit)

            buttons_frame_text_page = tkinter.Frame(self.root)
            buttons_frame_text_page.pack()

            save_button = tkinter.Button(buttons_frame_text_page, text="Criptografar", command=lambda: self.check_data(cryp_type))
            save_button.pack(side="left")
            self.pdf_button = tkinter.Button(buttons_frame_text_page, text="Gerar Arquivos PDF")
            self.pdf_button.pack(side="left")
            self.pdf_button.config(state='disabled')
        elif self.title == 'Criptografar Arquivos':
            cryp_type = 'file'

            self.create_common_fields()
            
            buttons_frame_files_page = tkinter.Frame(self.root)
            buttons_frame_files_page.pack()
            
            save_button = tkinter.Button(buttons_frame_files_page, text="Criptografar", command=lambda: self.check_data(cryp_type))
            save_button.pack(side="left")
            search_file_button = tkinter.Button(buttons_frame_files_page, text="Procurar Arquivo", command=lambda: self.search_file())
            search_file_button.pack(side="left")

    def open_next_page(self,title):
        self.root.destroy()
        next_page = MainPage(title)
        next_page.root.mainloop()

    def check_data(self, cryp_type):
        self.count += 1
        data_name = self.insert_name.get()
        data_cpf = self.insert_cpf.get()
        
        if cryp_type == 'text':
            try:
                data_text_to_encrypt = self.current_text
            except:
                data_text_to_encrypt = ''
            
            if self.count == 1:
                self.create_common_widgets(cryp_type)

            len_validation = func.verify_len_input(data_cpf, data_name, data_text_to_encrypt)

            if len_validation == 'valid':
                cpf_validation = func.verify_cpf(data_cpf)
                
                if cpf_validation == 'cpf valid':
                    encrypted_text = func.generate_encrypted_data(data_text_to_encrypt)
                    
                    self.encrypt_text_show.insert("1.0", encrypted_text)
                    self.encrypt_text_show.config(state='disabled')
                    
                    self.encrypt_text_scroll.config(command=self.encrypt_text_show.yview)

                    unique_key = func.generate_unique_key()

                    self.unique_key_show.insert("1.0", unique_key)
                    self.unique_key_show.config(state='disabled')
                    self.unique_key_scroll.config(command=self.unique_key_show.yview)

                    save_on_db = func.send_text_to_db(unique_key, data_name, data_text_to_encrypt, data_cpf)
                    self.validation_label.config(text=save_on_db)

                    self.pdf_button.config(state='active', command=lambda: self.generate_pdf_file(encrypted_text, unique_key, data_name, cryp_type))

                else:
                    self.validation_label.config(text=cpf_validation)
                    self.pdf_button.config(state='disabled')
            else:
                self.validation_label.config(text=len_validation)
                self.pdf_button.config(state='disabled')
        elif cryp_type == 'file':
            try:
                data_text_to_encrypt = self.file_dir
            except:
                data_text_to_encrypt = 'no dir'

            if self.count == 1:
                self.create_common_widgets(cryp_type)

            len_validation = func.verify_len_input(data_cpf, data_name, data_text_to_encrypt)

            if len_validation == 'valid':
                data_file_name = self.file_name
                data_file_dir = self.file_dir

                cpf_validation = func.verify_cpf(data_cpf)

                if cpf_validation == 'cpf valid':
                    encrypted_text = func.generate_encrypted_data(data_text_to_encrypt)

                    server_file_dir = func.move_file_to_server(data_file_dir, data_file_name)

                    encrypted_file = func.generate_encrypted_file(encrypted_text, data_file_name, data_file_dir)
                    self.file_name_label.config(text=encrypted_file)

                    unique_key = func.generate_unique_key()

                    save_on_db = func.send_file_to_db(unique_key, data_name, data_cpf, data_file_name, server_file_dir)

                    generate_key_file = self.generate_pdf_file(encrypted_text, unique_key, data_name, cryp_type)

                    self.validation_label.config(text=save_on_db)

                else:
                    self.validation_label.config(text=cpf_validation)
            else:
                self.validation_label.config(text=len_validation)

    def validate_input_len(self, P, input_type):
        if input_type == 'name':
            if len(P) <= 45:
                return True
            return False
        elif input_type == 'cpf':
            if len(P) <= 11:
                return True
            return False

    def update_label_when_digit(self, event):
        self.current_text = self.insert_text_to_encrypt.get("1.0", "end-1c")
        self.label_var_per_digit.set(255 - len(self.current_text))

    def create_common_widgets(self, cryp_type):
        self.validation_label = tkinter.Label(self.root, text='')
        self.validation_label.pack()

        if cryp_type == 'text':
            self.encrypt_text_label = tkinter.Label(self.root, text='Texto criptografado:')
            self.encrypt_text_label.pack()
            self.encrypt_frame = tkinter.Frame(self.root)
            self.encrypt_frame.pack(fill="both", expand=True)

            self.encrypt_text_scroll = tkinter.Scrollbar(self.encrypt_frame)
            self.encrypt_text_scroll.pack(side="right", fill="y")

            self.encrypt_text_show = tkinter.Text(self.encrypt_frame, wrap="word", height=5, yscrollcommand=self.encrypt_text_scroll.set)
            self.encrypt_text_show.pack(fill="both", expand=True)

            self.unique_key_label = tkinter.Label(self.root, text='Key para descriptografar:')
            self.unique_key_label.pack()

            self.unique_key_frame = tkinter.Frame(self.root)
            self.unique_key_frame.pack(fill="both", expand=True)

            self.unique_key_scroll = tkinter.Scrollbar(self.unique_key_frame)
            self.unique_key_scroll.pack(side="right", fill="y")

            self.unique_key_show = tkinter.Text(self.unique_key_frame, wrap="word", height=2, yscrollcommand=self.unique_key_scroll.set)
            self.unique_key_show.pack(fill="both", expand=True)

    def create_common_fields(self):
        validate_input_len_cmd = self.root.register(self.validate_input_len)
        self.count = 0

        self.name_label = tkinter.Label(self.root, text='Insira seu nome')
        self.name_label.pack()
        self.insert_name = tkinter.Entry(self.root, justify='center',width=50, validate="key", validatecommand=(validate_input_len_cmd, "%P", "name"))
        self.insert_name.pack()
        
        self.cpf_label = tkinter.Label(self.root, text='Insira seu CPF (apenas números)')
        self.cpf_label.pack() 
        self.insert_cpf = tkinter.Entry(self.root, justify='center',width=50, validate="key", validatecommand=(validate_input_len_cmd, "%P", "cpf"))
        self.insert_cpf.pack()

    def generate_pdf_file(self, encrypted_text, key, user_name, cryp_type):
        pdf_files = func.pdf_files_controller(encrypted_text, key, user_name, cryp_type)
        self.validation_label.config(text=pdf_files)

    def search_file(self):
        self.file_dir, self.file_name = func.search_file()
        
        if self.file_dir:
            self.file_name_label = tkinter.Label(self.root, text=f'Arquivo escolhido: {self.file_name}')
            self.file_name_label.pack()


if __name__ == "__main__":
    main_page = MainPage('Cryptography App')
    main_page.root.mainloop()

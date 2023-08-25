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
        self.choose_next_step()

    def choose_next_step(self):
        pass

class MainPage(Page):
    def choose_next_step(self):
        if self.title == 'Cryptography App':
            encrypt_text_button = tkinter.Button(self.root, text="Criptografar Textos", command=lambda: self.open_next_page('Criptografar Textos'))
            encrypt_text_button.pack()
        elif self.title == 'Criptografar Textos':
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
            
            self.label_var_per_digit = tkinter.StringVar()
            self.label_var_per_digit.set(255)
            self.text_to_encrypt_label = tkinter.Label(self.root, text='Insira o texto para criptografar. Quantidade de caracteres digitados: ')
            self.text_to_encrypt_label.pack()
            self.text_to_encrypt_label_var = tkinter.Label(self.root, textvariable=self.label_var_per_digit)
            self.text_to_encrypt_label_var.pack()
            self.insert_text_to_encrypt=tkinter.Text(self.root,wrap='word',height=4)
            self.insert_text_to_encrypt.pack()
            self.insert_text_to_encrypt.bind("<KeyRelease>",self.update_label_when_digit)

            save_button = tkinter.Button(self.root, text="Criptografar", command=lambda: self.check_data())
            save_button.pack()

    def open_next_page(self,title):
        self.root.destroy()
        next_page = MainPage(title)
        next_page.root.mainloop()
    
    def check_data(self):
        self.count += 1
        data_name = self.insert_name.get()
        data_cpf = self.insert_cpf.get()
        try:
            data_text_to_encrypt = self.current_text
        except:
            data_text_to_encrypt = ''
        
        if self.count == 1:
            self.create_common_widgets()

            len_validation = func.verify_len_input(data_cpf, data_name, data_text_to_encrypt)

            if len_validation == 'valid':
                cpf_validation = func.verify_cpf(data_cpf)
                
                if cpf_validation == 'cpf valid':
                    encrypted_text = func.generate_crypt_data(data_text_to_encrypt)
                    
                    self.encrypt_text_show.insert("1.0", encrypted_text)
                    self.encrypt_text_show.config(state='disabled')
                    
                    self.encrypt_text_scroll.config(command=self.encrypt_text_show.yview)

                    unique_key = func.generate_unique_key()

                    self.unique_key_show.insert("1.0", unique_key)
                    self.unique_key_show.config(state='disabled')
                    self.unique_key_scroll.config(command=self.unique_key_show.yview)

                    save_on_db = func.send_text_to_db(unique_key, data_name, data_text_to_encrypt, data_cpf)
                    self.validation_label.config(text=save_on_db)

                else:
                    self.validation_label.config(text=cpf_validation)
            else:
                self.validation_label.config(text=len_validation)
        else:
            len_validation = func.verify_len_input(data_cpf, data_name, data_text_to_encrypt)

            if len_validation == 'valid':
                cpf_validation = func.verify_cpf(data_cpf)
                
                if cpf_validation == 'cpf valid':
                    encrypted_text = func.generate_crypt_data(data_text_to_encrypt)

                    self.encrypt_text_show.config(state='normal')
                    self.encrypt_text_show.delete("1.0", "end")
                    self.encrypt_text_show.insert("1.0", encrypted_text)
                    self.encrypt_text_show.config(state='disabled')

                    unique_key = func.generate_unique_key()

                    self.unique_key_show.config(state='normal')
                    self.unique_key_show.delete("1.0", "end")
                    self.unique_key_show.insert("1.0", unique_key)
                    self.unique_key_show.config(state='disabled')

                    save_on_db = func.send_text_to_db(unique_key, data_name, data_text_to_encrypt, data_cpf)
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

    def create_common_widgets(self):
        self.validation_label = tkinter.Label(self.root, text='')
        self.validation_label.pack()

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

if __name__ == "__main__":
    main_page = MainPage('Cryptography App')
    main_page.root.mainloop()

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

            self.name_label = tkinter.Label(self.root, text='Insira seu nome')
            self.name_label.pack()
            self.insert_name = tkinter.Entry(self.root, validate="key", validatecommand=(validate_input_len_cmd, "%P", "name"))
            self.insert_name.pack()
            
            self.cpf_label = tkinter.Label(self.root, text='Insira seu CPF (apenas números)')
            self.cpf_label.pack() 
            self.insert_cpf = tkinter.Entry(self.root, validate="key", validatecommand=(validate_input_len_cmd, "%P", "cpf"))
            self.insert_cpf.pack()
            
            self.text_to_encrypt_label = tkinter.Label(self.root, text='Insira o texto para criptografar')
            self.text_to_encrypt_label.pack() 
            self.insert_text_to_encrypt = tkinter.Entry(self.root, validate="key", validatecommand=(validate_input_len_cmd, "%P", "text_to_encrypt"))
            self.insert_text_to_encrypt.pack()

            save_button = tkinter.Button(self.root, text="Criptografar", command=lambda: self.check_data())
            save_button.pack()

    def open_next_page(self,title):
        self.root.destroy()
        next_page = MainPage(title)
        next_page.root.mainloop()
    
    def check_data(self):
        data_name = self.insert_name.get()
        data_cpf = self.insert_cpf.get()
        data_text_to_encrypt = self.insert_text_to_encrypt.get()
        
        validation_label = tkinter.Label(self.root, text='')
        validation_label.pack()
        
        null_validation = func.verify_null_input(data_cpf, data_name, data_text_to_encrypt)

        if null_validation == 'valid':
            cpf_validation = func.verify_cpf(data_cpf)
            
            if cpf_validation == 'cpf valid':
                encrypted_text = func.generate_crypt_data(data_text_to_encrypt)

                encrypt_text_label = tkinter.Label(self.root, text='Texto criptografado:')
                encrypt_text_label.pack()
                
                encrypt_frame = tkinter.Frame(self.root)
                encrypt_frame.pack(fill="both", expand=True)

                encrypt_text_scroll = tkinter.Scrollbar(encrypt_frame)
                encrypt_text_scroll.pack(side="right", fill="y")

                encrypt_text_show = tkinter.Text(encrypt_frame, wrap="word", height=5, yscrollcommand=encrypt_text_scroll.set)
                encrypt_text_show.insert("1.0", encrypted_text)
                encrypt_text_show.pack(fill="both", expand=True)
                encrypt_text_scroll.config(command=encrypt_text_show.yview)

                unique_key = func.generate_unique_key()

                unique_key_label = tkinter.Label(self.root, text='Key para descriptografar:')
                unique_key_label.pack()

                unique_key_frame = tkinter.Frame(self.root)
                unique_key_frame.pack(fill="both", expand=True)

                unique_key_scroll = tkinter.Scrollbar(unique_key_frame)
                unique_key_scroll.pack(side="right", fill="y")

                unique_key_show = tkinter.Text(unique_key_frame, wrap="word", height=2, yscrollcommand=unique_key_scroll.set)
                unique_key_show.insert("1.0", unique_key)
                unique_key_show.pack(fill="both", expand=True)
                unique_key_scroll.config(command=unique_key_show.yview)
            else:
                validation_label.config(text=cpf_validation)
        else:
            validation_label.config(text=null_validation)
        
    def validate_input_len(self, P, input_type):
        if input_type == 'name':
            if len(P) <= 45:
                return True
            return False
        elif input_type == 'cpf':
            if len(P) <= 11:
                return True
            return False
        elif input_type == 'text_to_encrypt':
            if len(P) <= 255:
                return True
            return False

if __name__ == "__main__":
    main_page = MainPage('Cryptography App')
    main_page.root.mainloop()

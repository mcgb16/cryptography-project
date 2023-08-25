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
            self.name_label = tkinter.Label(self.root, text='Insira seu nome')
            self.name_label.pack()
            self.insert_name = tkinter.Entry(self.root)
            self.insert_name.pack()
            
            self.cpf_label = tkinter.Label(self.root, text='Insira seu CPF (apenas números)')
            self.cpf_label.pack() 
            self.insert_cpf = tkinter.Entry(self.root)
            self.insert_cpf.pack()
            
            self.text_to_encrypt_label = tkinter.Label(self.root, text='Insira o texto para criptografar')
            self.text_to_encrypt_label.pack() 
            self.insert_text_to_encrypt = tkinter.Entry(self.root)
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

        cpf_validation = func.verify_cpf(data_cpf)

        if cpf_validation == 'cpf valid':
            encrypted_text = func.generate_crypt_data(data_text_to_encrypt)

            encrypt_text_label = tkinter.Label(self.root, text='Texto criptografado:')
            encrypt_text_label.pack()
            
            encrypt_text_show = tkinter.Label(self.root, text='')
            encrypt_text_show.pack()
            encrypt_text_show.config(text=encrypted_text)

            unique_key = func.generate_unique_key()

            unique_key_label = tkinter.Label(self.root, text='Key para descriptografar:')
            unique_key_label.pack()

            unique_key_show = tkinter.Label(self.root, text='')
            unique_key_show.pack()
            unique_key_show.config(text=unique_key)
        else:
            cpf_not_valid_label = tkinter.Label(self.root, text=cpf_validation)
            cpf_not_valid_label.pack()


if __name__ == "__main__":
    main_page = MainPage('Cryptography App')
    main_page.root.mainloop()

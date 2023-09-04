import random
import string
import secrets
import func_db
from fpdf import FPDF
from tkinter import filedialog

def verify_cpf(user_cpf):
    cpf_not_valid = 'CPF não é válido. Cheque a digitação e lembre-se: apenas números.'
    if user_cpf == '11111111111':
        return cpf_not_valid
    elif user_cpf == '22222222222':
        return cpf_not_valid
    if user_cpf == '33333333333':
        return cpf_not_valid
    elif user_cpf == '44444444444':
        return cpf_not_valid
    if user_cpf == '55555555555':
        return cpf_not_valid
    elif user_cpf == '66666666666':
        return cpf_not_valid
    if user_cpf == '77777777777':
        return cpf_not_valid
    elif user_cpf == '88888888888':
        return cpf_not_valid
    if user_cpf == '99999999999':
        return cpf_not_valid
    elif user_cpf == '00000000000':
        return cpf_not_valid

    cpf_digit_list = []    
    v1 = 10
    v2 = 11
    i = 0
    j = 0
    cpf_digit1_validate = 0
    cpf_digit2_validate = 0

    if len(user_cpf) != 11:
        return cpf_not_valid

    try:
        int(user_cpf)
    except:
        return cpf_not_valid
    
    for d in user_cpf:
        cpf_digit_list.append(int(d))

    while i < 9:
        cpf_digit1_validate += cpf_digit_list[i]*v1
        v1 -= 1
        i += 1

    cpf_digit1_validate = (cpf_digit1_validate*10)%11

    if cpf_digit1_validate == 10:
        cpf_digit1_validate = 0
    
    if cpf_digit1_validate == cpf_digit_list[9]:
        while j < 10:
            cpf_digit2_validate += cpf_digit_list[j]*v2
            v2 -= 1
            j += 1

        cpf_digit2_validate = (cpf_digit2_validate*10)%11

        if cpf_digit2_validate == 10:
            cpf_digit2_validate = 0
        
        if cpf_digit2_validate == cpf_digit_list[10]:
            return 'cpf valid'
        else:
            return cpf_not_valid
    else:
        return cpf_not_valid

def verify_len_input(cpf, name, text_to_encrypt):
    null_message = 'Por favor preencha todos os campos!'
    len_message_text_to_encrypt = 'O limite máximo para criptografia de textos é de 255 caracteres.'

    if cpf == '':
        return null_message
    elif name == '':
        return null_message
    elif text_to_encrypt == '':
        return null_message
    elif len(text_to_encrypt) > 255:
        return len_message_text_to_encrypt
    else:
        return 'valid'

def generate_encrypted_data(text_to_crypt):
    crypted_list = []
    crypted_data = ''
    
    for d in text_to_crypt:
        crypt_mask_len = random.randint(128,256)
        crypted_list.append(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = crypt_mask_len)))
    
    for i in crypted_list:
        crypted_data += i
    
    return crypted_data

def generate_unique_key():
    unique_key_lenght = 128
    key = ''
    for i in range(unique_key_lenght):
        key += ''.join(secrets.choice(string.ascii_letters + string.digits))
    return key

def generate_pdf_files(main_txt, pdf_type, user_name):
    pdf_file = FPDF()
    pdf_file.add_page()
    cell_x = 190
    page_h = pdf_file.h

    if pdf_type == 'key':
        header_text = f'{user_name}, muito obrigado por criptografar conosco! Segue abaixo sua Key única para descriptografia futura.'
        footer_text = 'Lembre-se: não a perca de forma alguma! Caso contrário, não será possível efetuar a descriptografia do texto gerado.'
        file_name = 'Key'
        pdf_file.set_font("courier", size=12,style="I")
        pdf_file.multi_cell(cell_x,txt=header_text, align="C")
        pdf_file.set_y(page_h/2)
        pdf_file.set_font("courier", size=11)
        pdf_file.multi_cell(cell_x,txt=main_txt, align="L")
    
    elif pdf_type == 'encrypted_text':
        footer_text = f'{user_name}, para efetuar a descriptografia, utilize a key fornecida, junto do CPF cadastrado, no aplicativo.'
        file_name = 'Encrypted_text'
        pdf_file.set_font("courier", size=11)
        pdf_file.multi_cell(cell_x,txt=main_txt, align="L")

    pdf_file.set_y(page_h - pdf_file.t_margin - pdf_file.b_margin)
    pdf_file.set_font("courier", size=12,style="I")
    pdf_file.multi_cell(cell_x,txt=footer_text, align="C")

    pdf_file.output(filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("All Files", "*.*")],initialfile=file_name))

    return 'Sucesso!'

def pdf_files_controller(encrypted_text, key, user_name):
    generate_pdf_files(encrypted_text, 'encrypted_text', user_name)
    generate_pdf_files(key, 'key', user_name)
    
    return 'Todos os pdfs criados com sucesso.' 

def send_text_to_db(key, name, text, cpf):
    send_to_db = func_db.save_text_on_db(key,name,text,cpf)
    
    return send_to_db

def get_file_information():
    file_dir = filedialog.askopenfilename(initialdir='/', filetypes=[("All Files", "*.*")])
    file_dir_list = file_dir.split('/')
    file_name_with_extension = file_dir_list[-1]
    file_name_list = file_name_with_extension.split('.')
    
    file_name = file_name_list[0]
    file_extension = file_name_list[-1]

    return file_dir, file_name, file_extension

def generate_encrypted_file(encrypted_data, file_name):
    pass

def send_file_to_db(key, name, file_data, cpf, file_name):
    send_to_db = func_db.save_file_on_db(key,name,file_data,cpf,file_name)
    
    return send_to_db

import random
import string
import secrets
import func_db

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

def generate_crypt_data(text_to_crypt):
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

def generate_key_file():
    pass

def generate_crypt_file():
    pass

def send_text_to_db(key, name, text, cpf):
    send_to_db = func_db.save_text_on_db(key,name,text,cpf)
    
    return send_to_db
import random
import string
import secrets
import func_db

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
    pass

def generate_key_file():
    pass

def generate_crypt_file():
    pass
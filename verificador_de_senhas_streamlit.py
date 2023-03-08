import streamlit as st
import requests
import hashlib

def is_password_leaked(password):
    # Hash a senha usando o algoritmo SHA1
    password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Divida o hash em duas partes: o prefixo e o sufixo
    prefix = password_hash[:5]
    suffix = password_hash[5:]
    
    # Faça uma requisição HTTP GET para a API
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    
    # Verifique se a resposta da API contém o sufixo da hash da senha
    for line in response.text.splitlines():
        if line.startswith(suffix):
            count = int(line.split(':')[1])
            return count
    
    # Se o sufixo não for encontrado na resposta, a senha não foi vazada
    return 0

# Título do aplicativo
st.title("Verificador de Senhas Vazadas")

# Campo de entrada de senha
password = st.text_input('Digite sua senha', type='password')

# Verifique se a senha foi vazada
if password:
    count = is_password_leaked(password)
    if count:
        st.warning(f'A senha foi vazada {count} vezes. Recomendamos que você escolha uma senha mais forte.')
    else:
        st.success('A senha não foi vazada. Parabéns!')



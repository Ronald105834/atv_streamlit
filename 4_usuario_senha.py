import streamlit as st 


st.title("Lacço de repetição: while") 

st.write("crie um programa que solicite ao usuario seu login")

login_salvo = "marta"
senha_salva = "123"

login = st.text_input("Digite seu login: ")
senha = st.text_input("Digite sua senha: ", type="password")

if st.button("Verificar"): 
    if login == login_salvo and senha == senha_salva:
        st.success("bem vindo!")
    else:
        st.warning("Login ou senha inválidos.")
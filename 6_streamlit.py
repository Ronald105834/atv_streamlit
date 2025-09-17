import streamlit as st 

st.title("Lacço de repetição: while") 

st.write("crie um programa que solicite ao usuario seu login")

login_salvo = "marta"
senha_salva = "123"

#variáveis internas do streamlit.
st.session_state.stedefault("campo", false)






login = st.text_input("Digite seu login: " desabled=st.session_state.campo)
senha = st.text_input("Digite sua senha: ", type="password", disable=st.session_state.campo)

if st.button("Verificar"): 
    if login == login_salvo and senha == senha_salva:
        st.success("bem vindo!")
    else:
        st.warning("Login ou senha inválidos.")
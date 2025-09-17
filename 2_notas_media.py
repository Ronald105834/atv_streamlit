import streamlit as st 

st.title("Laço de repetição")

st.write("Escreva um algoritimo que solicite duas notas paraum aluno. " \
"Caso seja menor que 0 ou maior que 10, mostre a pergunta novamnete. " \
"Calcule e mostre a média aritimética do aluno. ")



nota1 = st.number_input("Digite a primeira_nota: ", min_value=0, max_value=10)
nota2 = st.number_input("Digite a segunda_nota: ", min_value=0, max_value=10)

media = (nota1 + nota2) / 2 

if st.button("Calcular média"):
    st.info(f"Média: {media}")
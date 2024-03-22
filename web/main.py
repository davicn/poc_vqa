import streamlit as st

st.title("Nosso Prompt")


uploaded_file = st.file_uploader("Escolha uma imagem")

if uploaded_file is not None:
    st.image(uploaded_file)

    
question = st.text_input('Digite')
st.divider()
st.markdown(question)





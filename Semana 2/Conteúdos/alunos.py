import streamlit as st 

def main():
    st.title('Hello World')

    st.markdown('Botao')
    botao = st.button('Botao')
    if botao:
        st.markdown('Botão foi clicado')

    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Check foi clicado')

    st.markdown('Radio')
    radio = st.radio('Escolha as opções', ('OPÇÃO 1', 'OPÇÃO 2', 'OPÇÃO 3'))
    if radio == 'OPÇÃO 1':
        st.markdown('Opção 1 selecionada')
    if radio == 'OPÇÃO 2':
        st.markdown('Opção 2 selecionada')
    if radio == 'OPÇÃO 3':
        st.markdown('Opção 3 selecionada')
    
    st.markdown('SelectBox')
    box = st.selectbox('Escolha uma opção' , ('OPÇÃO 1', 'OPÇÃO 2', 'OPÇÃO 3'))
    if box == 'OPÇÃO 1':
        st.markdown('Opção 1 selecionada')
    if box == 'OPÇÃO 2':
        st.markdown('Opção 2 selecionada')
    if box == 'OPÇÃO 3':
        st.markdown('Opção 3 selecionada')

    st.markdown('Multi-seleção')
    multi = st.multiselect('Opções:', ('OPÇÃO 1', 'OPÇÃO 2', 'OPÇÃO 3'))
    if multi == 'OPÇÃO 1':
        st.markdown('Opção 1 selecionada')
    if multi == 'OPÇÃO 2':
        st.markdown('Opção 2 selecionada')
    if multi == 'OPÇÃO 3':
        st.markdown('Opção 3 selecionada')

    st.markdown('Upload de arquivo')
    file = st.file_uploader('Selecione seu arquivo', type = 'csv')
    if file is not None:
        st.markdown('Arquivo enviado')
    else:
        st.markdown('Arquivo ainda não enviado')
    ##########################################################
    #Estrururas que existem e podemos usar no StreamLit
        #st.header('Isto é um header')
        #st.subheader('Isto é um sub-header')
        #st.text('Isto é um texto')
        #st.image('logo.png')
        #Arquivos de audio = st.audio('record.wav)
        #Arquivos de vídeo = st.video('sentiment_motion.wav)
    ##########################################################
if __name__ == '__main__':
    main()
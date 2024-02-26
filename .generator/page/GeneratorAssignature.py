# assinatura_email.py

import streamlit as st
from base64 import b64encode

# Definição da função para criar a assinatura
def criar_assinatura(nome, cargo, empresa, telefone, ramal, endereco, imagem_base64=None):
    telefone_formatado = f'({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}'

    imagem_html = f'<img  src="data:image/png;base64,{imagem_base64}" alt="NOVA DISTRIBUIDORA DE VEÍCULOS LTDA" style="width:183px;">'
    
    assinatura = f"""
    <span style="color: #1e4792; font-family: 'Arial Black', Arial, Helvetica, sans-serif;font-size: 14px;
    font-weight: 900;">{nome}</span><br>
    <span style="color: #5f5e5e; font-family: 'Arial , sans-serif;font-size: 12px;
    font-weight: 500;">{cargo} | {empresa}</span><br>
    <span style="color: #5f5e5e; font-family: 'Arial , sans-serif;font-size: 12px;
    font-weight: 500;">Tel: {telefone_formatado} | Ramal: {ramal}</span><br>
    <span style="color: #5f5e5e; font-family: 'Arial , sans-serif;font-size: 12px;
    font-weight: 500;">{endereco}</span><br>
    {imagem_html}<br>
    """
    return assinatura

# Definição da função principal
def main():
    st.title("Gerador de Assinatura de E-mail")

    # Exibição do logo da empresa
    imagem_url = "https://www.chevroletnova.com.br/images/site/logo.svg"
    st.image(imagem_url, caption='NOVA DISTRIBUIDORA DE VEÍCULOS LTDA', use_column_width=True)

    # Solicitação de informações do usuário
    nome = st.text_input("Digite seu nome:")
    cargo = st.text_input("Digite seu cargo:")
    empresa = st.selectbox(
        'Escolha a filial:',
        ('Nova Tatuapé', 'Nova João Dias', 'Nova Belenzinho', 'Nova Rio Preto', 'Nova Campinas', 'Nova Ribeirão'))
    telefone = st.text_input("Digite seu telefone:", placeholder="Somente números...")
    ramal = st.text_input("Digite seu ramal:")

    imagem_path = "logo.jpg"
    imagem_base64 = carregar_imagem_base64(imagem_path)

    # Verificação de endereço 
    endereco = ""
    if empresa == 'Nova Belenzinho':
        endereco = 'R. São Leopoldo, 811 - Belenzinho, São Paulo - SP, 03055-000'
    elif empresa == 'Nova Campinas':
        endereco = 'Av. Dr. David Vicente, 240 - Vila Industrial (Campinas), Campinas - SP, 13070-771'
    elif empresa == 'Nova Tatuapé':
        endereco = 'Av. Condessa Elizabeth de Robiano, 2640 - Tatuapé, São Paulo - SP, 03074-000'
    elif empresa == 'Nova João Dias':
        endereco = 'Av. João Dias, 2300 - Santo Amaro, São Paulo - SP, 04724-003'
    elif empresa == 'Nova Rio Preto':
        endereco = 'Av. Cenobelino de Barro Serra, 1085 - Parque Industrial, São José do Rio Preto - SP, 15030-000'
    elif empresa == 'Nova Ribeirão':
        endereco = 'R. Dr. Hugo Fortes, 1119 - Lagoinha, Ribeirão Preto - SP, 14095-260'
    st.write(endereco)

    # Criação da assinatura
    if st.button("Gerar Assinatura"):
        assinatura = criar_assinatura(nome, cargo, empresa, telefone, ramal, endereco, imagem_base64)

        # Exibição da assinatura com HTML e CSS personalizados
        st.write("Assinatura de E-mail:")
        st.markdown(assinatura, unsafe_allow_html=True)

        # Adição do botão de download em uma coluna separada
        st.write("\n")
        st.markdown(get_download_link(assinatura), unsafe_allow_html=True)

# Definição da função para obter o link de download da assinatura
def get_download_link(assinatura):
    b64_assinatura = b64encode(assinatura.encode()).decode()
    href = f'data:text/html;charset=utf-8;base64,{b64_assinatura}'
    return f'<a href="{href}" download="assinatura_email.html"><button type="button" style="background-color: white; color: black; border-radius: 30px solid #04AA6D;">Baixar Assinatura</button></a>'

# Definição da função para carregar a imagem em base64
def carregar_imagem_base64(imagem_path):
    try:
        with open(imagem_path, "rb") as image_file:
            imagem_base64 = b64encode(image_file.read()).decode()
        return imagem_base64
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")
        return None

# Chamada para a função main
if __name__ == "__main__":
    main()

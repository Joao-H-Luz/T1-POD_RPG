import streamlit as st
from RPG import SubClass as sc

num_g = 2

# Titulo
st.header("Personagens")

# Sub-Titulo
st.write("Escolha a Classe")
# Colunas Internas

col1, col2, col3 = st.columns([5, 1.5, 5], border=False)

# --- GUERREIRO ---
with col1:
    with st.container(height=190, border=False):
        select_guerreiro = st.button(
            "Guerreiro", use_container_width=True, icon="⚔️")
        select_mago = st.button(
            "Mago", use_container_width=True, icon="🧙")
        select_Arqueiro = st.button(
            "Arqueiro", use_container_width=True, icon="🗡️")

    with st.container(height=100, border=True):
        st.write("Stats")
        sc.Guerreiro.estatus()



with col3:
    with st.container(height=550, border=False):
        if select_guerreiro:
            st.image("Imagens/Guerreiro.jpg", use_container_width=True)

            nome = st.text_input("Nome do Personagem")
        
            sel_habilit = st.multiselect(
                f"Selecione as Habilidades: {num_g} disponiveis.",
                ["Bola de Fogo", "Cura de Vida", "Disparo com Arco"],
                max_selections=2,
                accept_new_options=False)

      
    



        if select_mago:
            st.image("Imagens/Wizard.jpg", use_container_width=True)
            nome = st.text_input("Nome do Personagem")

            sel_habilit = st.multiselect(
                f"Selecione as Habilidades: {num_g} disponiveis.",
                ["Bola de Fogo", "Cura de Vida", "Disparo com Arco"],
                max_selections=5,
                accept_new_options=False)


        if select_Arqueiro:
            st.image("Imagens/Arqueiro.jpg", use_container_width=True)
            nome = st.text_input("Nome do Personagem")

            sel_habilit = st.multiselect(
                f"Selecione as Habilidades: {num_g} disponiveis.",
                ["Bola de Fogo", "Cura de Vida", "Disparo com Arco"],
                max_selections=3,
                accept_new_options=False)



    # habilidade_guerreiro = st.multiselect(
    #         "Escolha as Habilidades:",
    #         ["Teste1", "Teste2", "Teste3", "teste4", "Teste5"],
    #         max_selections=2,
    #         key="hab_guerreiro")

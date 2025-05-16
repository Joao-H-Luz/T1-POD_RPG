import streamlit as st

# Organizar as Paginas de Personagem e Arena na Lateral
pages = {"Deshbord": [
    st.Page("personagem_page.py", title="Personagens", icon="⚔️"),
    st.Page("arena_page.py", title="Arena", icon="🏟️")]}

# Navegação entre as Paginas
pg = st.navigation(pages)
pg.run()

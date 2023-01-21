import streamlit as st

st.set_page_config(page_title="Perpustakaan Wibu Jaya", page_icon=":books:")
st.title("Contact Us")

st.markdown(
    """
    <style>
        div[data-testid="column"]
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("https://avatars.githubusercontent.com/u/102802614?v=4")
    st.caption("[Krisna Wandhana](https://github.com/krisnawandhana)")
with col2:
    st.image("https://avatars.githubusercontent.com/u/72916363?v=4")
    st.caption("[Ngurah Bagus](https://github.com/BangAjus)")
with col3:
    st.image("https://avatars.githubusercontent.com/u/100138244?v=4")
    st.caption("[Agung Mahadana](https://github.com/agungmahadana)")
with col4:
    st.image("https://avatars.githubusercontent.com/u/97663926?v=4")
    st.caption("[Ryan Prana](https://github.com/prana8)")
with col5:
    st.image("https://avatars.githubusercontent.com/u/94416844?v=4")
    st.caption("[Raindra Pramathana](https://github.com/RaindraP)")
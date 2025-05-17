import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo1.jpg",width=450)
with col2:
    st.title("Mogilicharla Veerendra Sai")
    content='''Highly motivated and results-oriented professional with a strong 
    ability to learn quickly and efficiently. Adept at implementing learned skills and 
    knowledge to achieve optimal outcomes. Eager to contribute to the company's competitive edge 
    by strategically utilizing my skillset. Committed to continuous learning and improvement, 
    striving to become a key player in the company's success.'''
    st.info(content)

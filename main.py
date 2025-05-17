import pandas
import streamlit as st
st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo1.jpg",width=350)
with col2:
    st.title("Mogilicharla Veerendra Sai")
    content='''Highly motivated and results-oriented professional with a strong 
    ability to learn quickly and efficiently. Adept at implementing learned skills and 
    knowledge to achieve optimal outcomes. Eager to contribute to the company's competitive edge 
    by strategically utilizing my skillset. Committed to continuous learning and improvement, 
    striving to become a key player in the company's success.'''
    st.info(content)
c='''Below are some apps built by me . Just have a look .Feel Free to contact me!'''
st.subheader(c)
col3,col4 = st.columns(2)
df=pandas.read_csv('data.csv',sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])

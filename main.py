import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/bw_me.jpg")

with col2:
    st.title("Paul Harris")
    content = """
    I am a freelance Python programmer based in the UK. I am PCEP and PCAP certified
    and passed the Harvard CS50x and CS50 Python course exams. This web page is to showcase
    some of the Apps I have built with the skills I have learned.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=",")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

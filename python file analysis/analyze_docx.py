from docx import Document
from docx.shared import Inches
import streamlit as st

document = Document("demo.docx")
headings3 = []
headings2 = []
headings1 = []
texts = []
for paragraph in document.paragraphs:
    match paragraph.style.name:
        case "Heading 1":
            headings1.append(paragraph.text)

        case "Heading 2":
            headings2.append(paragraph.text)

        case "Heading 3":
            headings3.append(paragraph.text)

        case "Normal":
            texts.append(paragraph.text)


st.header("H1")
for h1 in zip(headings1):
    st.write(h1)

st.write("##")

st.header("H2")
for h2 in zip(headings2):
    st.write(h2)

st.write("##")

st.header("H3")
for h3 in zip(headings3):
    st.write(h3)

st.write("##")
st.header("Normal")
for txt in zip(texts):
    st.write(txt)
    
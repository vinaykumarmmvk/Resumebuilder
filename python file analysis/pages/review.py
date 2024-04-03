from docx import Document
from docx.shared import Inches
import streamlit as st
import numpy as np
from page_redirect import open_pageself
from st_pages import hide_pages

hide_pages(["review"])

full_name = st.session_state['name']
Phone_no = st.session_state['phone_no']
email = st.session_state['email']
address = st.session_state['address']
nationality = st.session_state['nationality']
dob = st.session_state['dob']
linkedin = st.session_state['linkedin']
prof_pic = st.session_state['profile_pic']

work_details = st.session_state['work_details']

edu_details = st.session_state['edu_details'] 

langs = st.session_state['langs'] 
skill_set = st.session_state['skill_set'] 
hobbies = st.session_state['hobbies'] 

st.header("Review details")

#create 3 columns - col1 for image, mid is separator, col2 for text
col1, col2 = st.columns([4,2])
with col1:
    st.write("Name: "+full_name)
    st.write("Phone_no: "+Phone_no)
    st.write("Address: "+address)
    st.write("Email: "+email)
    st.write("Nationality: "+nationality)
    st.write("date of birth: "+str(dob))
    st.write("LinkedIn: "+linkedin)

with col2:
    st.write("#") #to give space
    if prof_pic is not None:
        st.image(prof_pic, width=100)
    
st.subheader("Education Details")
st.write(edu_details)

st.subheader("Work Details")
st.write(work_details)

st.subheader("Languages")
st.write(langs)

st.subheader("Skills")
st.write(skill_set)

st.subheader("Hobbies")
st.write(hobbies)
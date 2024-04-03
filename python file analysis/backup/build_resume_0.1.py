from docx import Document
from docx.shared import Inches
from docx.shared import Cm
import streamlit as st
import numpy as np
import datetime
import calendar

def get_duration(start_year, start_month, end_year, end_month):
    if( start_year is not ''):
        duration = start_year
        if(start_month is not ''):
            duration = start_month+"/"+duration # add else flag cond. to check

    if(start_year is ''):
        duration = ''

    if( end_year is not ''):
        #duration = duration + "-"+end_year #08/2020-09/2023 or 09/2023 or 2023 or 2020-2023
        if(end_month is not ''):
                duration = duration + "-"+end_month+"/"+end_year
        else:
            if(duration is not ''):
                duration = duration + "-"+end_year
            
            else:
                duration = end_year

    return duration

st.header("Resume builder")
with st.expander('Report month'):
            this_year = datetime.date.today().year
            this_month = datetime.date.today().month
            report_year = st.selectbox('', range(this_year, this_year - 5, -1))
            month_abbr = calendar.month_abbr[1:]
            report_month_str = st.radio('', month_abbr, horizontal=True)
            report_month = month_abbr.index(report_month_str) + 1
st.text(f'{report_year} {report_month_str}')

st.subheader("Personal details")
full_name = st.text_input("Full name")
address = st.text_input("Address")
Phone_no = st.text_input("Phone No.")
dob = st.date_input("Date of Birth", value=None)
nationality = st.text_input("Nationality")
linkedin = st.text_input("LinkedIn")
#prof_pic = upload pic
prof_pic = st.file_uploader("Upload your picture")
placeholder = st.empty()

st.subheader("Language")

langs = {}

lang = st.text_input("Enter Language name")
levels = ["Fluent", "Proficient", "Conversational", "Basic"]
option = st.selectbox("Level", levels, disabled= False)   

add_lang = st.button("Add Language")
if add_lang:
    if( lang is not '' ):
        langs[lang] = option

    st.write(langs)

st.subheader("Education")

edu_details = {}
institute = st.text_input("Enter University/School name")
prog_name = st.text_input("Enter program name")
startYear = st.selectbox('Start Year', range(1990, 2023))
startMonth = st.selectbox('Start Month', range(1, 13))
endYear = st.selectbox('End Year', range(1990, 2023))
endMonth = st.selectbox('End Month', range(1, 13))

duration = get_duration(str(startYear), str(startMonth), str(endYear), str(endMonth))    
st.write(duration)

add_edu = st.button("Add")
if add_edu:
    if institute is not None:
        edu_details[institute] = {institute, prog_name, duration}
        st.write(edu_details)

st.subheader("Experience")
"""
company = st.text_input("Enter Company name")
designation = st.text_input("Enter designation")
work_startYear = st.selectbox('Start Year', range(1990, 2023))
work_startMonth = st.selectbox('Start Month', range(1, 13))
work_endYear = st.selectbox('End Year', range(1990, 2023))
work_endMonth = st.selectbox('End Month', range(1, 13))
description = st.text_area("Enter description")
#checkbox to select like current date add later
work_duration = get_duration(work_startYear, work_startMonth, work_endYear, work_endMonth)

add_work = st.button("Add Experience")
if add_work:
    if company is not None:
        edu_details[company] = {designation, work_duration, description}
        st.write(edu_details)
"""

st.subheader("Skill set")

def clear_text():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""

val = st.text_input("Enter Skill set seperated by commas", key="widget", on_change=clear_text)

st.write(st.session_state.my_text)
skills.append(st.session_state.my_text)
st.write(skills)
skill_set1 = st.text_area("Enter Skill-set seperated by commas")


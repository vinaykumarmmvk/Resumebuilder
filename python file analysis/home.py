import streamlit as st
import datetime
import calendar
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

hide_pages(["home", "review"])

st.header("Resume builder")

def init_session():
    if 'edu_details' not in st.session_state:
            st.session_state['edu_details'] = {}

    if 'work_details' not in st.session_state:
            st.session_state['work_details'] = {}

    if 'langs' not in st.session_state:
            st.session_state['langs'] = {}


def lang_form():
    lang = st.session_state["lang_name"]
    option = st.session_state["level"]
    if( lang is not ''):
                langs = {}
                langs[lang] = option
                langs_session = st.session_state['langs'] 
                langs = langs| langs_session
                st.write(langs)
                st.session_state['langs'] = langs
            
    else:
        st.error("Please enter language name.")

    st.session_state["lang_name"] = ""

global duration

def edu_form():
    edu_details = {}
    institute = st.session_state['uni_name']
    prog_name = st.session_state['prog_name'] 
    if institute == '' or institute is None:
         st.error("Please enter university/school name")
    else:
        edu_details[institute] = {institute, prog_name, duration}
        edu_details_session = st.session_state['edu_details'] 
        edu_details = edu_details| edu_details_session
        st.write(edu_details)
        st.session_state['edu_details'] = edu_details


def display_date(key1):
    with st.expander('Select Date'):
        this_year = datetime.date.today().year
        this_month = datetime.date.today().month
        report_year = st.selectbox('', range(this_year, this_year - 5, -1), key=key1)
        month_abbr = calendar.month_abbr[1:]
        report_month_str = st.radio('', month_abbr, index=this_month - 1, horizontal=True, key=key1+1)
        report_month = month_abbr.index(report_month_str) + 1
    st.text(f'{report_year} {report_month_str}')
    return str(report_year)+" "+str(report_month_str)

#def add_list():
#    st.session_state['skill_set'] += [st.session_state.widget]
#    st.session_state.widget = ""


# whitespace for increasing width of tabs
whitespace = 12

init_session()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personal Details".center(whitespace,"\u2001") , "Education".center(whitespace,"\u2001"), "Experience".center(whitespace,"\u2001"), "Language/s, Hobbies and skill/s".center(whitespace,"\u2001"), "Others".center(whitespace,"\u2001")])

with tab1:
    st.subheader("Personal details")
    full_name = st.text_input("Full name", key="name")
    address = st.text_input("Address", key="address")
    email = st.text_input("Email", key="email")
    Phone_no = st.text_input("Phone No.", key="phone_no")
    dob = st.date_input("Date of Birth", value=None, key="dob")
    nationality = st.text_input("Nationality", key="nationality")
    linkedin = st.text_input("LinkedIn",key="linkedin")
    prof_pic = st.file_uploader("Upload your picture", key="profile_pic")


with tab2:
    st.subheader("Education")
    with st.form(key="form_edu"):
        edu_details = {}
        institute = st.text_input("Enter University/School name",key="uni_name")
        prog_name = st.text_input("Enter program name",key="prog_name")
        st.write("Start Date")
        startDate = display_date(0)
        st.write("End date")
        endDate = display_date(2)
        duration = startDate+"-"+endDate

        st.form_submit_button("Add", on_click=edu_form)

with tab3:
    st.subheader("Experience")
    
    work_details = {}
    company = st.text_input("Enter Company name", key="company")
    designation = st.text_input("Enter designation", key="designation")
    st.write("Start Date")
    startDate = display_date(4)
    st.write("End date")
    work_endDate = display_date(6)
    work_duration = startDate+"-"+endDate
    description = st.text_area("Enter description")

    add_work = st.button("Add Experience")
    if add_work:
        if company is not None:
            work_details[company] = {designation, work_duration, description}
            work_details_session = st.session_state['work_details'] 
            work_details = work_details| work_details_session
            st.write(work_details)
            st.session_state['work_details'] = work_details

        else:
             st.error("Please enter company name")
    
with tab4:
    st.subheader("Language")

    with st.form(key="form_lang"):

        lang = st.text_input("Enter Language name", key="lang_name")

        levels = ["Basic", "Intermediate", "Fluent"]
        option = st.selectbox("Level", levels, placeholder="Please select", disabled= False, key="level")   

        add_lang = st.form_submit_button("Add Language", on_click=lang_form)


    st.subheader("Skill set")

    val = st.text_input("Enter Skill set seperated by commas", key="skill_set")
    
    #st.write(st.session_state['skill_set'])
    st.subheader("Hobbies")
    hobbies = st.text_input("Enter Hobbies seperated by commas", key="hobbies")

with tab5:
     st.subheader("Other details")
     st.text_input("Add field name")
     st.text_area("Add field details")
     st.button("Add Details")
     # if data added append it into session dictonary of others

#validation to be done

if st.button("Review"):
    switch_page("review")
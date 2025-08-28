import streamlit as st
import gspread
from google.oauth2.service_account import credentials
import pandas as pd

SCOPE=["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

@st.cache_resource
def init_connection():
    creds = credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=SCOPE
    )
    client = gspread.authorize(creds)
    return client

connect = init_connection()

st.header("GRADING SYSTEM")
st.subheader("these grades can not be changed")
st.text_input("enter your name")
st.text_input("enter your unique student ID")

# Biology
st.write("biology")
biology = st.number_input("enter your Biology mark", min_value=0, max_value=100)

# Chemistry
st.write("chemistry")
chemistry = st.number_input("enter your Chemistry score", min_value=0, max_value=100)

# Math
st.write("math")
math = st.selectbox("enter your Math score:", list(range(0, 101)))

# English
st.write("english")
english = st.number_input("enter your English score", min_value=0, max_value=100)

# Physics
st.write("physics")
physics = st.number_input("enter your Physics score", min_value=0, max_value=100)


# Button to show grades in table
if st.button("Show Grades in Table"):
    def get_grade(score):
        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "E"

    data = {
        "Subject": ["Biology", "Chemistry", "Math", "English", "Physics"],
        "Score": [biology, chemistry, math, english, physics],
        "Grade": [
            get_grade(biology),
            get_grade(chemistry),
            get_grade(math),
            get_grade(english),
            get_grade(physics),
        ],
    }

    df = pd.DataFrame(data)
    st.table(df)

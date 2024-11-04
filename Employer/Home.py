import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 3em;
        color: #2E478B;
        margin-top: 20px;
    }
    .instructions {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 60px;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar layout
st.sidebar.title("Menu")
st.sidebar.button("HOME")
st.sidebar.button("INPUT")
st.sidebar.button("Preference")
st.sidebar.button("CUSTOM")

# Center the title at the top of the main page
st.markdown("<h1 class='title'>Employer Homepage</h1>", unsafe_allow_html=True)

# Instructions section below the main content
st.markdown("<div class='instructions'>", unsafe_allow_html=True)
st.subheader("Instructions")
st.write("""
Welcome to the Resume Checker Powered by AI! Here, you can manage various tasks for recruitment and assessment, including:
- **Setting job requirements**: Define the specific qualifications, skills, and personality traits desired for applicants.
- **Candidate Matching**: Review AI-generated summaries of applicants, including a ranking or pass/fail rating based on set criteria.
- **Weighted Ratings**: Assign importance to job criteria, such as work experience, alignment with company values, and technical skills.

Use the sidebar on the left to navigate between sections, Enjoy!
""")
st.markdown("</div>", unsafe_allow_html=True)

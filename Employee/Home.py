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
st.sidebar.button("UPLOAD Resume")


# Center the title at the top of the main page
st.markdown("<h1 class='title'>Employee Homepage</h1>", unsafe_allow_html=True)

# Main content area
#st.write("This is where your main content will go.")

# Instructions section below the main content
st.markdown("<div class='instructions'>", unsafe_allow_html=True)
st.subheader("Instructions")
st.write("""
Welcome to Resume Checker Powered by AI! Here, you can:
- **Upload your CV**: Use AI assistance to enhance your resume with proficient formatting, rating, and content recommendations.
- **Simulated Interview**: Generate potential interview questions and receive feedback on responses.
- **Profile Management**: Potential employer will reach you out in the system.

Use the sidebar on the left to navigate through various features, Enjoy!
""")
st.markdown("</div>", unsafe_allow_html=True)

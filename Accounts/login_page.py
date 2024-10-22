import streamlit as st
import Functions as fc

# 数据库准备
st.title("Login")

email = st.text_input("Please input your email", key="login_email")
password = st.text_input("Please input your password", type="password", key="login_password")

if st.button("Login"):
    if email == "" or password == "":
        st.warning("please input your email or password")
    else:
        conn = fc.connect_DB("CV.db")
        login_result = fc.login_account(conn, "ACCOUNTS", email, password)
        if login_result == 1:
            st.success("Login successfully!")
            st.session_state.logged_in = True
            # turning to the app page
        elif login_result == 0:
            st.warning("Email or Password is wrong!")
        else:
            st.warning("Sorry for the unexpected error, please try it again.")
        conn.close()


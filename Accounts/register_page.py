import streamlit as st
import Functions as fc

st.title("Register")

name = st.text_input("Name:", key="name_input")
phone = st.text_input("Phone:", key="phone_input")
email = st.text_input("Email:", key="email_input")
password = st.text_input("Password:", type="password", key="password_input")
confirm_password = st.text_input("Confirm-password:", type="password", key="password_confirm")
country = st.selectbox("Country:", ["Chinese", "America", "England", "France", "Russia", "Other country"])
user_type = st.selectbox("Account type:", ["Employee", "Employer"])

if st.button("Register"):
    if name == "" or len(name) > 16:
        st.warning("Name cannot be empty or more than 16 Letters.")
        st.stop()
    elif phone.isdigit() is False:
        st.warning("Phone can only be numbers")
        st.stop()
    elif email == "":
        st.warning("Email cannot be empty.")
        st.stop()
    elif len(password) < 8 or len(password) > 16:
        st.warning("Password cannot be less than 8 digits and more than 16 digits.")
        st.stop()
    elif password != confirm_password:
        st.warning("Confirm-password should match the password.")
        st.stop()
    elif user_type == "":
        st.warning("Type cannot be empty!")
        st.stop()
    else:
        # 将数据存入数据库
        conn = fc.connect_DB("CV.db")
        account_register = {"id": fc.get_next_id(conn, "ACCOUNTS"), "name": name, "telephone": phone,
                            "email": email, "password": password, "country": country, "type": user_type}

        register_result = fc.insert_account(conn, "ACCOUNTS", account_register)
        if register_result == 0:
            st.warning("The account is exist")
        elif register_result == 1:
            st.success("Register successfully")
        else:
            st.warning("Sorry for the unexpect error, please try it again.")
        conn.close()


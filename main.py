#database name is CV.db, Table name is ACCOUNTS
#changing the login successfully code, let it turn to the successfully page
import streamlit as st
import Accounts.Functions as AF

prepare_state = AF.check_database_and_table()
if prepare_state == 0:
    st.warning("Sorry, there is something wrong with the app, please try it again")
else:
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    def login():
        # 数据库准备
        st.title("Login")

        email = st.text_input("Please input your email", key="login_email")
        password = st.text_input("Please input your password", type="password", key="login_password")

        if st.button("Login"):
            if email == "" or password == "":
                st.warning("please input your email or password")
            else:
                conn = AF.connect_DB("CV.db")
                login_result = AF.login_account(conn, "ACCOUNTS", email, password)
                if login_result == 1:
                    st.session_state.logged_in = True
                    # turning to the app page
                elif login_result == 0:
                    st.warning("Email or Password is wrong!")
                else:
                    st.warning("Sorry for the unexpected error, please try it again.")
                conn.close()
                st.rerun()

        if st.button("Go to register"):
            register()




    @st.dialog("Register")
    def register():
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
                conn = AF.connect_DB("CV.db")
                account_register = {"id": AF.get_next_id(conn, "ACCOUNTS"), "name": name, "telephone": phone,
                                    "email": email, "password": password, "country": country, "type": user_type}

                register_result = AF.insert_account(conn, "ACCOUNTS", account_register)
                if register_result == 0:
                    st.warning("The account is exist")
                elif register_result == 1:
                    st.success("Register successfully")
                else:
                    st.warning("Sorry for the unexpect error, please try it again.")
                conn.close()
                st.rerun()


    def logout():
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()


    login_page = st.Page(login, title="Log in", icon=":material/login:")
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

    if st.session_state.logged_in:
        pg = st.navigation(
            {
                "Account": [logout_page]
            }
        )
    else:
        pg = st.navigation([login_page])

    pg.run()
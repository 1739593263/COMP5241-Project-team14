#database name is CV.db, Table name is ACCOUNTS
#changing the login successfully code, let it turn to the successfully page
import streamlit as st
import Functions as fc

# 登录页面
def login_page():
    #数据库准备
    st.title("Login")
    
    email = st.text_input("Please input your email")
    password = st.text_input("Please input your password", type="password")

    # 创建两个并排的列
    col1, col2 = st.columns(2)
    # 在第一列中放置第一个按钮
    with col1:
        if st.button("Login"):
            if email == "" or password == "":
                st.warning("please input your email or password")
            else:
                conn = fc.connect_DB("CV.db")
                login_result = fc.login_account(conn, "ACCOUNTS", email, password)
                if login_result == 1:
                    st.success("Login successfully!")
                    # turning to the app page
                elif login_result == 0:
                    st.warning("Email or Password is wrong!")
                else:
                    st.warning("Sorry for the unexpect error, please try it again.")
                conn.close()
    with col2:
        if st.button("Register"):
            # turn to the register page
            st.session_state.page = "register"

def register_page():
    st.title("Register")
    
    st.write("Name:")
    name = st.text_input("Example: Zack", key = "name_input")
    st.write("Phone:")
    phone = st.text_input("Example: 12345678", key = "phone_input")
    st.write("Email:")
    email = st.text_input("Example:12345678@163.com", key = "email_input")
    st.write("Password:")
    password = st.text_input("",type="password", key = "password_input")
    st.write("Confirm-password:")
    confirm_password = st.text_input("", type="password", key = "password_confirm")
    st.write("country:")
    country = st.selectbox("Country", ["Chinese", "America", "England", "Other country"])
    st.write("Account type:")
    user_type = st.selectbox("Type", ["Employee", "Employer"])
    
    if st.button("Register"):
        if name == "" or len(name) > 16:
            st.warning("Name cannot be empty or more than 16 Letters.")
        elif email == "":
            st.warning("Email cannot be empty.")
        elif len(password) < 8 or len(password) > 16:
            st.warning("Password cannot be less than 8 digits and more than 16 digits.")
        elif password != confirm_password:
            st.warning("Confirm-password should match the password.")
        elif user_type == "":
            st.warning("Type cannot be empty!")
        else:
            # 将数据存入数据库
            conn = fc.connect_DB("CV.db")
            account_register = {"id": fc.get_next_id(conn, "ACCOUNTS"), "name":name, "telephone":phone, "email": email, "password":password, "country":country, "type":user_type}
            
            register_result = fc.insert_account(conn,"ACCOUNTS", account_register)
            if register_result == 0:
                st.warning("The account is exist")
            elif register_result == 1:
                st.success("Register successfully")
            else:
                st.warning("Sorry for the unexpect error, please try it again.")
            conn.close()
    
    if  st.button("Login"):
        st.session_state.page = "login"  # 注册成功后返回登录页面


# 主程序
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "login"  # 默认显示登录页面

    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()

if __name__ == "__main__":
    prepare_state = fc.check_database_and_table()
    if prepare_state == 0:
        st.warning("Sorry, there is something wrong with the app, please try it again")
    else:
        main()


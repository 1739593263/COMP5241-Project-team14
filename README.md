# COMP5241-Project-team14

## Recent work
- I updated the user's registration and login (The UI looks ugly T_T). In it, I created a sqlite database called 
CV.db with a table called ACCOUNTS to store account data.

- ACCOUNT: id(int), name(str), telephone(int), email(str), password(str), country(str), type(str)

## Test example
- pip install -r requirements.txt
- streamlit run main.py
- test account:
  - test1:
    - name: test1
    - id: 00000001
    - email: 12345678@163.com
    - password: 12345678
  - test2:
    - name: test2
    - id: 00000002
    - email:98765432@163.com
    - password: 98765432

## Environment
- python 3.12.7
- streamlit 1.39.0

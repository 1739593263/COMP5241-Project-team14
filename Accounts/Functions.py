import sqlite3
import os

#返回数据库的游标cursor
def connect_DB(name_db):
    # connect to the database(if there isn't a database, it will be created)
    conn = sqlite3.connect(f'{name_db}')
    return conn

def create_accounts_table(conn, db_name, table_name):
    # 创建一个游标对象
    cursor = conn.cursor()
    # 创建一个表
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        telephone INTEGER,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        country TEXT,
        type TEXT NOT NULL
    )
    ''')
    # 提交事务
    conn.commit()


#是否存在表，存在返回1，不存在返回0
def search_accounts_table(conn,db_name,table_name):
    # 创建一个游标对象
    cursor = conn.cursor()
    # 查询 sqlite_master 表以检查是否存在名为 'table_name' 的表
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")

    # 获取查询结果
    result = cursor.fetchone()

    if result:
        print("表存在。")
        return 1
    else:
        print("表不存在。")
        return 0

#检查是否存在数据库和table, 准备成功返回1，准备失败返回0
def check_database_and_table():
    #连接到数据库
    conn = connect_DB("CV.db")
    if search_accounts_table(conn,"CV.db","ACCOUNTS") == 0:
        create_accounts_table(conn, "CV.db", "ACCOUNTS")
        print("NO TABLE, THE TABLE WILL BE CREATED")
    elif search_accounts_table(conn,"CV.db","ACCOUNTS") == 1:
        print("SELECT THE TABLE SUCCESSFULLY")
    else:
        print("UNEXPECT ERROR")
        return 0
    print("PREPARING IS COMPLETE")
    #关闭数据库
    conn.close()
    return 1




#插入数据用户信息数据，如果存在则返回0，如果不存在则返回1
def insert_account(conn,table_name,account_dict):
    # 创建一个游标对象
    cursor = conn.cursor()
    
    # 检查用户是否存在
    cursor.execute(f"SELECT * FROM {table_name} WHERE email = '{account_dict['email']}'")
    result = cursor.fetchone()

    if result:
        # 用户已存在，返回 0
        return 0
    else:
        # 用户不存在，插入新用户
        sql=f"""INSERT INTO {table_name} (id, name, telephone, email, password, country, type) VALUES ('{account_dict["id"]}','{account_dict["name"]}','{account_dict["telephone"]}','{account_dict["email"]}','{account_dict["password"]}','{account_dict["country"]}','{account_dict["type"]}') """
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return 1

#查询登陆数据数据，正确返回1，不正确返回0
def login_account(conn,table_name,email,password):
    #获取游标
    cursor = conn.cursor()

    # 检查用户是否存在
    cursor.execute(f"SELECT * FROM {table_name} WHERE email = '{email}' AND password = '{password}'")
    result = cursor.fetchone()

    if result:
        return 1
    else:
        return 0

#查询最新数据的id
def get_next_id(conn, table_name):
    #获取游标
    cursor = conn.cursor()
    # 查询当前最大的 ID
    cursor.execute(f"SELECT MAX(id) FROM {table_name}")
    result = cursor.fetchone()[0]

    if result is None:
        # 如果没有记录，返回 '00000001'
        return '00000001'
    else:
        # 计算下一个 ID
        next_id = int(result) + 1
        return f"{next_id:08d}"  # 格式化为八位数字

# 检测是雇员还是雇主
def is_employee(conn,table_name,email,password):
    # 获取游标
    cursor = conn.cursor()
    cursor.execute(f"SELECT type FROM {table_name} WHERE email = '{email}' AND password = '{password}'")
    result = cursor.fetchone()
    return result[0]
import pymysql

# db1 =  pymysql.connect(host="localhost",user="root",password="root",database="loggerdb")
# print(db1)


def get_connection():
    try:
        return pymysql.connect(host="localhost",user="root",password="root",database="loggerdb")
        # print(db)
    except BaseException as e:
        print(e.args)

def close_resources(conn,cursor):
    try:
        if cursor:
            cursor.close()
    except BaseException as e:
        print(e.args)

    try:
        if conn:
            #conn.commit()
            conn.close()
    except BaseException as b:
        print(b.args)

conn = get_connection()
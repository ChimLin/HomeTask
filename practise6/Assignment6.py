import pymysql.cursors

def connect():
    try:
        connect = pymysql.connect(host="localhost",
                                  user='root', password='',
                                  db='employees',
                                  cursorclass=pymysql.cursors.DictCursor)

        with connect:
            cur = connect.cursor()

            cur.execute('select name, salary from employee where salary = (select min(salary) from employee)')
            rows = cur.fetchall()
            for row in rows:
                print(f"{row['name']} {row['salary']}")
            connect.commit()
    except Exception as message:
        print(message)


if __name__ == '__main__':
    connect()

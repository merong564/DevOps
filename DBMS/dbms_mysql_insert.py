import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host='localhost',        # MySQL 서버 주소 (같은 PC 사용 시 localhost(127.0.0.1))
    user='root',
    password='1234',
    database='exampledb'
    )

# 커서 생성 -> 명령어 작성
cursor = conn.cursor()

# 명령어 실행
# sql = '''INSERT INTO employees(id, name, deptid, managerid)
# values(8, 'Moonjung', 8, 101)
# '''
# cursor.execute(sql)

sql1 = '''INSERT INTO employees(id, name, deptid, managerid)
values(%s, %s, %s, %s)
'''

cursor.execute(sql1, (9, 'moonjung', 9, 101))



conn.commit()

print('데이터 삽입 완료')

# 연결 해제
conn.close()

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
sql = 'SELECT * FROM employees'
cursor.execute(sql)

employees = cursor.fetchall()       # 유의!! MySQL에서 commit한 다음에 가져와야 함
for employee in employees:
    print(employee)  

print('데이터 조회 완료')

# 연결 해제
conn.close()

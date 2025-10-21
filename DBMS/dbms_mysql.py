import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host='localhost',        # MySQL 서버 주소 (같은 PC 사용 시 localhost(127.0.0.1))
    user='root',
    password='1234',
    database='exampledb',
    charset='utf8mb4',          # 인코딩 방식
    cursorclass=pymysql.cursors.DictCursor          # 조회 결과를 Dictionary 형태로 가져와서 처리하겠다
)

# 커서 생성 -> 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute('SELECT DATABASE()')

# fetchone() : 한 번의 호출에 하나의 행을 가져올 때 사용
print("현재 데이터베이스: ", cursor.fetchone())         
# print("현재 데이터베이스: ", cursor.fetchall())         
# print("현재 데이터베이스: ", cursor.fetchmany())         

# 연결 해제
conn.close()

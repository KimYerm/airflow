from airflow import DAG
import datetime
import pendulum # datetime을 더 쉽게 쓸 수 있게 해줌
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # 화면에 보이는 dag 이름, 파일명과 일치시키는 것이 좋음 
    schedule="0 0 * * *", # 크론 스케줄. 분 / 시 / 일 / 월 / 요일. 매일 0시 0분에 돈다 
    start_date=pendulum.datetime(2021, 3, 1, tz="Asia/Seoul"), # 언제부터 돌 것인지. 2021년 1월 1일부터. Asia/Seoul - 무조건 한국시간으로 
    catchup=False, # 누락된 이전 구간 돌게 할 것인가. 순서대로가 아닌 한꺼번에 돔 -> 일반적으로 false로 해놓는 것이 좋음 
   # dagrun_timeout=datetime.timedelta(minutes=60), # dag이 60분 이상 돌면 실패하도록 
   # tags=["example", "example2"], # 제목 밑에 파란색 태그. optional
   # params={"example_key": "example_value"}, # task에 공통적으로 넣을 파라미터 
) as dag:
    bash_t1 = BashOperator( # 왼쪽은 task명 
        task_id="bash_t1", # 객체명과 task id는 동일하게 해주는 것이 찾기 좋음 
        bash_command="echo whoami", # 어떤 쉘 스크립트를 실행할 것인가. whoami라는 string을 출력해준다
    )
    
    bash_t2 = BashOperator( # 왼쪽은 task명 
        task_id="bash_t2", # 객체명과 task id는 동일하게 해주는 것이 찾기 좋음 
        bash_command="echo $HOSTNAME", # 어떤 쉘 스크립트를 실행할 것인가.
    )

    bash_t1 >> bash_t2 # task 실행 순서 
import sqlalchemy 

from sqlalchemy import create_engine, text

db_conn = "mysql+pymysql://i2n4ikof0q7heq4o9x0d:pscale_pw_9pOH1fEFdR1l3JQZKmndpGS2y1qXJSkdigIifaz1t3M@us-east.connect.psdb.cloud/jobhub?charset=utf8mb4"

engine = create_engine(
  db_conn, 
  connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    
    # print(result.all())
    jobs = []
    for row in result.all():
      dict = {
        'id': row[0],
        'title': row[1],
        'location': row[2],
        'salary': row[3],
        'currency': row[4],
        'description': row[5],
        'requirements': row[6]
      }
      jobs.append(dict)
    return jobs
    # print(result_dicts)

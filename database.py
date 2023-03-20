from sqlalchemy import create_engine, text
import os

q = os.environ.get('DB_CONN_STR')
print("var", q)
engine = create_engine(
  q, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      obj = {
        'id': row[0],
        'title': row[1],
        'location': row[2],
        'salary': row[3],
        'currency': row[4],
        'description': row[5],
        'requirements': row[6]
      }
      jobs.append((obj))
    return jobs
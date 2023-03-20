from sqlalchemy import create_engine, text
import os

conn_str = os.environ.get('DB_CONN_STR')

engine = create_engine(
  conn_str, 
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


def load_job_from_db(id):
  print("HERE IS AN ID", id)
  with engine.connect() as conn:
    stmt = text("SELECT * FROM jobs WHERE id = :x").bindparams(x=id)
    result = conn.execute(stmt).fetchall()

    if len(result) == 0:
      return None
    else:
      res = result[0]
      dict = {
        'id': res[0],
        'title': res[1],
        'location': res[2],
        'salary': res[3],
        'currency': res[4],
        'description': res[5],
        'requirements': res[6]
      }
      return dict



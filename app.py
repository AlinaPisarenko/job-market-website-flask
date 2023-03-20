from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def load_home():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name='JobHub')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found 😔"
  return render_template('jobpage.html', job = job)


if __name__ == '__main__':
  app.run(port=5555, debug=True)


import json
from fastapi import FastAPI
from ranking.job_ranker import rank_jobs_for_student
from ranking.candidate_ranker import rank_candidates_for_job

app = FastAPI()

with open('data/students.json') as f:
    students = json.load(f)
with open('data/jobs.json') as f:
    jobs = json.load(f)
with open('data/candidates.json') as f:
    candidates = json.load(f)

@app.get('/students/{student_id}/ranked-jobs')
def get_ranked_jobs(student_id: str):
    student = next(s for s in students if s['id'] == student_id)
    return rank_jobs_for_student(student, jobs)

@app.get('/jobs/{job_id}/ranked-candidates')
def get_ranked_candidates(job_id: str):
    job = next(j for j in jobs if j['id'] == job_id)
    return rank_candidates_for_job(job, candidates)

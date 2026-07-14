def score_job_for_student(student, job):
    student_skills = set(s.lower() for s in student['skills'])
    job_skills = set(s.lower() for s in job['required_skills'])

    skill_overlap = len(student_skills & job_skills) / max(len(job_skills), 1)
    location_match = 1.0 if student['location'] == job['location'] else 0.3
    exp_ok = 1.0 if student['experience_years'] >= job['min_experience'] else 0.5

    score = (0.6 * skill_overlap) + (0.25 * location_match) + (0.15 * exp_ok)
    return round(score, 3)

def rank_jobs_for_student(student, jobs):
    scored = [(job, score_job_for_student(student, job)) for job in jobs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [{'job': job, 'score': score} for job, score in scored]

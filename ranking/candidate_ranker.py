def score_candidate_for_job(candidate, job):
    candidate_skills = set(s.lower() for s in candidate['skills'])
    job_skills = set(s.lower() for s in job['required_skills'])

    skill_overlap = len(candidate_skills & job_skills) / max(len(job_skills), 1)
    location_match = 1.0 if candidate['location'] == job['location'] else 0.3
    exp_ok = 1.0 if candidate['experience_years'] >= job['min_experience'] else 0.5

    score = (0.6 * skill_overlap) + (0.25 * location_match) + (0.15 * exp_ok)
    return round(score, 3)

def rank_candidates_for_job(job, candidates):
    scored = [(c, score_candidate_for_job(c, job)) for c in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [{'candidate': c, 'score': score} for c, score in scored]

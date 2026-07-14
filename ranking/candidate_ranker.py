def explain_candidate_match(candidate, job):
    candidate_skills = set(s.lower() for s in candidate["skills"])
    job_skills = set(s.lower() for s in job["required_skills"])

    matched = sorted(candidate_skills & job_skills)
    missing = sorted(job_skills - candidate_skills)
    overlap_ratio = len(matched) / max(len(job_skills), 1)

    location_match = candidate["location"] == job["location"]
    experience_match = candidate["experience_years"] >= job["min_experience"]

    if overlap_ratio == 1.0 and location_match and experience_match:
        summary = "Strong match: all required skills present, same location, meets experience requirement."
    elif overlap_ratio == 0:
        summary = "Weak match: no overlapping skills with this job's requirements."
    elif not location_match and overlap_ratio > 0:
        summary = "Partial match: some required skills present, but different location."
    elif not experience_match:
        summary = "Partial match: skills align, but experience requirement not met."
    else:
        summary = "Partial match: some required skills present."

    return {
        "skill_match": {
            "matched": matched,
            "missing": missing,
            "overlap_ratio": round(overlap_ratio, 3)
        },
        "location_match": location_match,
        "experience_match": experience_match,
        "summary": summary
    }


def score_candidate_for_job(candidate, job):
    explanation = explain_candidate_match(candidate, job)
    skill_overlap = explanation["skill_match"]["overlap_ratio"]
    location_match = 1.0 if explanation["location_match"] else 0.3
    exp_ok = 1.0 if explanation["experience_match"] else 0.5

    score = (0.6 * skill_overlap) + (0.25 * location_match) + (0.15 * exp_ok)
    return round(score, 3), explanation


def rank_candidates_for_job(job, candidates):
    scored = []
    for candidate in candidates:
        score, explanation = score_candidate_for_job(candidate, job)
        scored.append((candidate, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return [
        {"candidate": candidate, "score": score, "explanation": explanation}
        for candidate, score, explanation in scored
    ]
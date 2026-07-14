# PlaceMux - Search & Discovery (Task 3)

## What this does
Ranks jobs for students, and ranks candidates for companies, using a
transparent feature-based scoring model (v1).

## Scoring approach
For each student-job or candidate-job pair, we compute:
- Skill overlap (60% weight): fraction of required skills the person has
- Location match (25% weight): 1.0 if same city, 0.3 otherwise
- Experience fit (15% weight): 1.0 if experience meets minimum, 0.5 otherwise

Final score = 0.6 * skill_overlap + 0.25 * location_match + 0.15 * experience_fit

This keeps the ranking explainable - useful for a v1 demo, and easy to
extend later with semantic skill matching (TF-IDF or embeddings) instead
of exact string matches.

## How to run
1. Activate the virtual environment: venv\Scripts\Activate.ps1
2. Install dependencies: pip install -r requirements.txt
3. Start the server: uvicorn api.main:app --reload
4. Open http://127.0.0.1:8000/docs to try the endpoints interactively

## Endpoints
- GET /students/{student_id}/ranked-jobs - ranked jobs for a given student
- GET /jobs/{job_id}/ranked-candidates - ranked candidates for a given job

## Example
GET /students/s1/ranked-jobs returns jobs sorted by score, highest first,
so the best-fit job for that student appears at the top.

## Next steps (v2)
- Replace exact skill-string matching with TF-IDF or embeddings so
  related terms (e.g. "ML" and "machine learning") match automatically
- Accept new student/job/candidate data via POST instead of static JSON files
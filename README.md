# Task Tracker - SRE Deployment Practice

A simple Flask web app for adding/viewing tasks. Use this to practice SRE workflows.

## Local Development
1. Install Python 3.12+.
2. `pip install -r requirements.txt`
3. `python app.py`
4. Visit `http://localhost:5000`
5. Test health: `curl http://localhost:5000/health`

## Containerized Deployment
1. Build: `docker build -t task-tracker .`
2. Run: `docker run -p 5000:5000 task-tracker`
3. Multi-container: `docker-compose up`
4. Test: `curl http://localhost:5000/ready`

## Cloud Deployment (e.g., Google Cloud Run)
1. Enable Cloud Run API and install gcloud CLI.
2. `gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/task-tracker`
3. `gcloud run deploy task-tracker --image gcr.io/YOUR_PROJECT_ID/task-tracker --platform managed --allow-unauthenticated`
4. Set env vars (e.g., PORT) in the console.

## Monitoring/SRE Tips
- Logs: Check Flask logs or integrate Prometheus.
- Scale: Add env var for DB (e.g., `DATABASE_URL`).
- CI/CD: Update `deploy.yml` secrets and push to trigger.

For Kubernetes: Use the Dockerfile as base for a Deployment YAML.

## Deployment
- Uses GitHub Actions for Docker build and image push to registry

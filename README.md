# DevOps Demo

Beginner DevOps demo project with:
- `app.py` (simple Python script)
- `Dockerfile` (container image definition)
- GitHub Actions CI/CD workflow at `.github/workflows/ci.yml`

## CI/CD behavior

- On pull requests: run CI (`python app.py`)
- On pushes to `main`: run CI, then CD publishes a Docker image to GitHub Container Registry

Published image:
- `ghcr.io/<your-github-username>/my-devops-demo2:latest`

Example pull command:

```bash
docker pull ghcr.io/<your-github-username>/my-devops-demo2:latest
```

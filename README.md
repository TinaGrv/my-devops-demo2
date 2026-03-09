# DevOps Demo

Beginner DevOps demo project with:
- `app.py` (simple Python script)
- `Dockerfile` (container image definition)
- GitHub Actions CI/CD workflow at `.github/workflows/ci.yml`
- `tests/test_app.py` (real automated tests using `unittest`)

## CI/CD behavior

- On pull requests: run CI tests + script
- On pushes to `main`: run CI, publish Docker image, then deploy to `staging` environment
- On version tags like `v1.0.0`: run CI, publish tagged image, and create a GitHub Release

Published image:
- `ghcr.io/<your-github-username>/my-devops-demo2:latest`

Example pull command:

```bash
docker pull ghcr.io/<your-github-username>/my-devops-demo2:latest
```

## Enable manual approval for staging

In your GitHub repo:
1. Go to `Settings` -> `Environments`
2. Create environment: `staging`
3. Add a protection rule: `Required reviewers`
4. Add yourself (or teammate) as reviewer

Now each push to `main` will pause before `deploy_staging` until approved.

## Create a semantic version release

From terminal:

```bash
git tag v1.0.0
git push origin v1.0.0
```

This triggers the `release_on_tag` job and creates a GitHub release.

## Monitoring add-on

The workflow `.github/workflows/health-monitor.yml` runs every 15 minutes and checks:

```bash
python app.py --health
```

If health is not `ok`, the workflow fails, which gives a basic alert-like signal in GitHub Actions.
